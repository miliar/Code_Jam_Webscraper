#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

struct Combine
{
    char ele1, ele2, result;
};

struct Opposite
{
    char ele1, ele2;
};

int main()
{
    ifstream input("input.dat");
    ofstream output("output.dat");

    vector<char> elements;
    vector<Combine*> combineable;
    vector<Opposite*> opposite;

    int n, cn, i;
    char currentElement;

    input >> n;
    cn = n;

    while (cn--)
    {
        elements.clear();
        combineable.clear();
        opposite.clear();

        int cmbCnt;
        input >> cmbCnt;

        for (i = 0; i < cmbCnt; i++)
        {
            Combine* cb = new Combine;
            input >> cb->ele1 >> cb->ele2 >> cb->result;
            combineable.push_back(cb);
        }

        int opCnt;
        input >> opCnt;

        for (i = 0; i < opCnt; i++)
        {
            Opposite* op = new Opposite;
            input >> op->ele1 >> op->ele2;
            opposite.push_back(op);
        }

        int elCnt;
        input >> elCnt;

        bool combined = false;

        for (i = 0; i < elCnt; i++)
        {
            input >> currentElement;
            //cout << "Invoking " << currentElement << endl;

            elements.push_back(currentElement);

            if (elements.size() == 1) continue;

            int elSize = elements.size() - 1;

            // find combineable
            combined = false;
            for (vector<Combine*>::iterator iter = combineable.begin(); iter != combineable.end(); ++iter)
            {
                if ( ((*iter)->ele1 == elements[elSize - 1] && (*iter)->ele2 == elements[elSize]) ||
                     ((*iter)->ele1 == elements[elSize] && (*iter)->ele2 == elements[elSize - 1]) )
                {
                    //cout << "I can combine " << (*iter)->ele1 << " and " << (*iter)->ele2 << "\n";

                    elements.pop_back();
                    elements[elSize - 1] = (*iter)->result;
                    combined = true;
                    break;
                }
            }

            if (combined) continue;

            // find opposable
            char toFind;
            vector<char>::iterator ele;
            for (vector<Opposite*>::iterator iter = opposite.begin(); iter != opposite.end(); ++iter)
            {
                // don't do useless checks
                // only check if the last element added opposes some of the elements in the list
                if ((*iter)->ele1 == currentElement)
                    toFind = (*iter)->ele2;
                else if ((*iter)->ele2 == currentElement)
                    toFind = (*iter)->ele1;
                else
                    continue;

                //cout << "Checking for opposite of " << currentElement << " and " << toFind << "\n";

                ele = find(elements.begin(), elements.end(), toFind);
                if (ele != elements.end())
                {
                    // found, clear elements
                    //cout << "Find opposite, clearing list.\n";
                    elements.clear();
                    break;
                }
            }
        }

        // done
        // lets print the list out
        output << "Case #" << n - cn << ": [";
        for (i = 0; i < elements.size(); i++)
        {
            output << elements[i];

            if (i != elements.size() - 1)
                output << ", ";
        }
        output << "]\n";

        // free the memory
        for (i = 0; i < combineable.size(); i++)
            delete combineable[i];

        for (i = 0; i < opposite.size(); i++)
            delete opposite[i];

    }

    input.close();
    output.close();

    //cin >> i;

    return 0;
}