#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define FOR(i, x) for (int i = 0; i < x; i++)
#define FORI(i,a, x) for (int i = a; i < x; i++)
#define ALL(x) (x).begin(), (x).end()
#define FORE(i, x) for (__typeof((x).begin()) i = (x).begin(); i != (x).end(); i++)
#define SZ(x) ((int) (x).size())

using namespace std;

int main()
{
    freopen("As.in","r",stdin);
    freopen("As.out","w",stdout);
    int L,D,N;
    scanf("%d%d%d\n",&L,&D,&N);
    string words[D];
    FOR (i,D)
        getline(cin,words[i]);
    FOR (i,N)
    {
        string cad;
        getline(cin,cad);
        int cuantos=0;
        FOR (j,D)
        {
            int pos=0;
            bool flag=1;
            FOR (k,L)
            {
                if (cad[pos]=='(')
                {
                    pos++;
                    bool flagt=0;
                    while (cad[pos]!=')')
                    {
                        flagt|=(cad[pos]==words[j][k]);
                        pos++;
                    }
                    flag&=flagt;

                }
                else
                    flag&=(cad[pos]==words[j][k]);
                pos++;
            }
            if (flag)
                cuantos++;
        }
        printf("Case #%d: %d\n",i+1,cuantos);
    }
    return 0;
}
