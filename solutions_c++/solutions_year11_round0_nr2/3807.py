#include <iostream>
#include <map>
#include <algorithm>

using namespace std;


int main(int argc, char** argv)
{
    int t,c,d,n;
    cin >> t;
    for (int i = 1; i <= t; i++)
    {
        map<char,char> comps;
        map<string,char> remps;
        map<char, int> cants;

        cin >> c;

        string aux1;

        for (int j = 1; j <= c; j++)
        {
            cin >> aux1;
            remps[aux1.substr(0, 2)] = aux1[2];
            reverse(aux1.begin(), aux1.end());
            remps[aux1.substr(1)] = aux1[0];
        }

        cin >> d;
        for (int j = 1; j <= d; j++)
        {
            cin >> aux1;
            comps[aux1[0]] = aux1[1];
            comps[aux1[1]] = aux1[0];
        }
        cin >> n;
        cin >> aux1;
        for (int j = 0; j < n; j++)
        {
            if(j == 0)
            {
                cants[aux1[j]]++;
            }else{
                if(remps.find(string(1,aux1[j-1]) + string(1,aux1[j])) != remps.end())
                {
                    cants[aux1[j-1]]--;
                    aux1 = aux1.substr(0, j-1) + remps[string(1,aux1[j-1]) + string(1,aux1[j])] + aux1.substr(j+1);
                    n--;
                    j-=2;
                }else if(comps.find(aux1[j]) != comps.end())
                {
                    if(cants[comps[aux1[j]]] > 0)
                    {
                        cants.clear();
                        aux1 = aux1.substr(j+1);
                        j = -1;
                        n = aux1.size();
                    }else{
                        cants[aux1[j]]++;
                    }
                }else{
                    cants[aux1[j]]++;
                }
            }
        }

        cout << "Case #" << i << ": [";
        for (int j = 0; j < n; ++j)
        {
            if(j)
            {
                cout << ", ";
            }
            cout << aux1[j];
        }
        cout << "]" << endl;
    }
}

