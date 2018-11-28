// Google Code Jam - Magicka.cpp : main project file.

#include <iostream>
#include <queue>
#include <string>
#include <map>
#include <set>

using namespace std;

void combineLastTwo(string& elements, map<string, char>& baseToNonBase)
{
    string baseElement; // last two chars
    baseElement.push_back(elements[elements.size()-1]);
    baseElement.push_back(elements[elements.size()-2]);

    if (baseToNonBase.find(baseElement) != baseToNonBase.end())
    {
        // Remove last two from elements and add the nonbase
        elements.erase(elements.end()-2, elements.end());
        elements.push_back(baseToNonBase[baseElement]);
    }
}

void checkForOpposed(string& elements, set<string>& opposed)
{
    // n complexity, for each char check all others chars
    for (int i=0; i<elements.size(); i++)
    {
        for (int j=i+1; j<elements.size(); j++)
        {
            string pair;
            pair.push_back(elements[i]);
            pair.push_back(elements[j]);

            if (opposed.find(pair) != opposed.end())
            {
                elements.clear();
                return;
            }
        }
    }
}

string asList(string& elements)
{
    string list;
    list = "[";

    for (int i=0; i<elements.size(); i++)
    {
        list += elements[i];

        if (i != elements.size()-1)
            list += ", ";
    }
    list += "]";

    return list;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int cases;
    cin >> cases;

    for (int i=0; i<cases; i++)
    {
        map<string, char> baseToNonBase;
        set<string> opposed;

        int c, d, n;
        cin >> c;

        // Base to non-base
        for (int j=0; j<c; j++)
        {
            char base1, base2, nonBase;
            cin >> base1 >> base2 >> nonBase;

            // Insert normal and inverted
            string normal, inverted;
            normal.push_back(base1); normal.push_back(base2);
            inverted.push_back(base2); inverted.push_back(base1);

            baseToNonBase[normal] = nonBase;
            baseToNonBase[inverted] = nonBase;
        }

        // Opposed
        cin >> d;
        for (int j=0; j<d; j++)
        {
            string normal;
            cin >> normal;

            // Insert normal and inverted
            string inverted;
            inverted.push_back(normal[1]); inverted.push_back(normal[0]);

            opposed.insert(normal);
            opposed.insert(inverted);
        }

        // Read string
        string elements;
        cin >> n;
        for (int j=0; j<n; j++)
        {
            char element;
            cin >> element;

            // Add to our resulting string
            elements.push_back(element);

            if (elements.size() >= 2)
            {
                combineLastTwo(elements, baseToNonBase);
                checkForOpposed(elements, opposed);
            }
        }

        cout << "Case #" << (i+1) << ": " << asList(elements) << endl;
    }

    return 0;
}
