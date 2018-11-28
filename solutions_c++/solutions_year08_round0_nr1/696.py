#include <iostream>
#include <string>
#include <algorithm>
#include <map>
#include <assert.h>
#include <limits.h>

using namespace std;

// cost for [query, engine]
int table[1001][100];

int queries[1000];

int main()
{
        int n;
        
        cin >> n;
        
        for (int c=0; c<n; ++c) {
                int s, q;
                char dummy;

                cin >> s >> dummy;
                cin.putback(dummy);

                int nengines = 0;
                map<string,int> engines;
                string line;
                for (int i=0; i<s; ++i) {
                        getline(cin,line);
                        engines[line] = nengines++;
                }
                
                assert(nengines == s);

                cin >> q >> dummy;
                cin.putback(dummy);

                //clog << "s: " << s << "  q: " << q << endl;

                for (int i=0; i<q; ++i) {
                        getline(cin, line);
                        if (engines.count(line))
                                queries[i] = engines[line];
                        else
                                queries[i] = nengines;
                }

                for (int e=0; e<s; ++e)
                        table[q][e] = 0;

                for (int i=q-1; i>=0; --i) {
                        for (int e=0; e<s; ++e) {
                                if (e != queries[i]) // no need to switch
                                        table[i][e] = table[i+1][e];
                                else {
                                        int mincost = INT_MAX;
                                        for (int j=0; j<s; ++j) {
                                                if (j==e)
                                                        continue;
                                                mincost = min(mincost, table[i+1][j]);
                                        }
                                        table[i][e] = mincost + 1;
                                }
                        }
                }

                /*for (int i=0; i<=q; ++i) {
                        if (i<q)
                                clog << char('A'+queries[i]);
                        else
                                clog << " ";
                        for (int j=0; j<s; ++j)
                                clog << " " << table[i][j];
                        clog << endl;
                }
                clog << endl;*/
                

                cout << "Case #" << c+1 << ": ";
                int mincost = table[0][0];
                for (int i=1; i<s; ++i)
                        mincost = min(mincost, table[0][i]);
                cout << mincost << endl;
                
        }
}
