#include <iostream>
#include <vector>
#include <map>

using namespace std;

int main()
{
    int t;

    cin >> t;
    for (int it = 1; it <= t; it++)
    {
        int c;
        cin >> c;
        map<pair<char, char>, char> mapTransf;

        for (int ic = 0; ic < c; ic++)
        {
            char c1, c2, ct;
            cin >> c1 >> c2 >> ct;
            if (c1 > c2)
                mapTransf[pair<char, char>(c2,c1)] = ct;
            else
                mapTransf[pair<char, char>(c1,c2)] = ct;
        }

        int d;
        cin >> d;
        vector<pair<char, char> > vCleaner;
        for (int id = 0; id < d; id++)
        {
            char c1, c2;
            cin >> c1 >> c2;
            if (c1 > c2)
                vCleaner.push_back (pair<char,char> (c2, c1));
            else
                vCleaner.push_back (pair<char,char> (c1, c2));
        }

        int n;
        vector<char> vResult;
        char cInvoke;

        cin >> n;
        for (int i = 0; i < n; i++)
        {
            cin >> cInvoke;
            if (vResult.size() > 0)
            {
                pair<char, char> pTransf;
                if (cInvoke > vResult.back())
                {
                    pTransf = pair<char, char> (vResult.back(), cInvoke);
                }
                else
                {
                    pTransf = pair<char, char> (cInvoke, vResult.back());
                }
                if (mapTransf.count (pTransf) > 0)
                {
                    vResult.back() = mapTransf[pTransf];
                    continue;
                }

                int bCleaner = 0;
                for (int j = 0; j < vResult.size(); j++)
                {
                    pair<char, char> pCleaner;
                    if (vResult[j] > cInvoke)
                        pCleaner = pair<char, char> (cInvoke, vResult[j]);
                    else
                        pCleaner = pair<char, char> (vResult[j], cInvoke);

                    for (int k = 0; k < vCleaner.size(); k++)
                    {
                        if (vCleaner[k] == pCleaner)
                        {
                            bCleaner = 1;
                            break;
                        }
                    }
                    if (bCleaner == 1)
                        break;
                }
                if (bCleaner == 1)
                {
                    vResult.clear();
                    continue;
                }
            }
            vResult.push_back(cInvoke);
        }
        cout << "Case #" << it << ": [";
        for (int i = 0; i < vResult.size(); i++)
        {
            if (i > 0)
                cout << ", ";
            cout << vResult[i];
        }
        cout << "]" << endl;
    }
    return 0;
}
