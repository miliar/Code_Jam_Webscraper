#include <iostream>
#include <vector>

using namespace std;

bool isbase[256] = {0};
char combine[256][256] = {'\0'};
char opposed[256] = {'\0'};

void initialise_arrays()
{
    for (int i=0; i<256; i++)
    {
        isbase[i] = 0;
        for (int j=0; j<256; j++)
            combine[i][j] = '\0';
        opposed[i] = '\0';
    }

    isbase['Q'] = 1;
    isbase['W'] = 1;
    isbase['E'] = 1;
    isbase['R'] = 1;
    isbase['A'] = 1;
    isbase['S'] = 1;
    isbase['D'] = 1;
    isbase['F'] = 1;
}

bool inlist(vector<char> &elements, char element)
{
    int i;

    for (i=0; i<elements.size(); i++)
    {
        if (elements[i] == element)
            return true;
    }

    return false;
}

vector<char> simulate_spells(vector<char> &elements)
{
    int i;
    vector<char> outelements;
    char c1, c2;
    bool c1isvalid;

    if (elements.size() == 1)
        return elements;
        
    i = 1;
    c1 = elements[0];
    while (i<elements.size())
    {
        c1isvalid = true;
        c2 = elements[i];
        // Elements can be combined
        if (combine[c1][c2] != '\0')
        {
            outelements.push_back(combine[c1][c2]);
        }
        // Elements are opposed
        else if (opposed[c2] != '\0' && 
                (inlist(outelements, opposed[c2]) || c1 == opposed[c2]))
        {
            outelements.clear();
        }
        // Add element to the list
        else
        {
            outelements.push_back(c1);
            c1 = c2;
            i++;
            continue;
        }
        i++;
        while (i<elements.size() && opposed[elements[i]] != '\0' &&
               inlist(outelements, opposed[elements[i]]))
        {
            outelements.clear();
            i++;
        }
        // Update c1
        if (i<elements.size())
        {
            c1 = elements[i];
        }
        // No more items left
        else
        {
            c1isvalid = false;
            break;
        }
        i++;
    }
    if (c1isvalid)
        outelements.push_back(c1);
    return outelements;
}

int main(void)
{
    int T, C, D, N;
    int i, j;
    char c1, c2, c3;
    vector<char> elements, outelements;

    // Get the number of test cases
    cin >> T;
    for (i=1; i<=T; i++)
    {
        initialise_arrays();
        cin >> C;
        for (j=0; j<C; j++)
        {
            cin >> c1 >> c2 >> c3;
            combine[c1][c2] = c3;
            combine[c2][c1] = c3;
        }

        cin >> D;
        for (j=0; j<D; j++)
        {
            cin >> c1 >> c2;
            opposed[c1] = c2;
            opposed[c2] = c1;
        }

        cin >> N;
        for (j=0; j<N; j++)
        {
            cin >> c1;
            elements.push_back(c1);
        }

        outelements = simulate_spells(elements);

        cout << "Case #" << i << ": [";
        for (j=0; j<(int)outelements.size()-1; j++)
        {
            cout << outelements[j] << ", ";
        }
        if (j == (int)outelements.size()-1)
        {
            cout << outelements[j];
        }
        cout << "]" << endl;
        elements.clear();
    }

    return 0;
}
