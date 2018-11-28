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
#define MOD 10000

using namespace std;

int main()
{
    freopen("Cs.in","r",stdin);
    freopen("Cs.out","w",stdout);
    int cases;
    string cad="welcome to code jam";
    scanf("%d\n",&cases);
    FOR (casos,cases)
    {
        int resp=0;
        string cadena;
        getline (cin,cadena);
        vector<vector<int> > matrix(SZ(cadena),vector<int>(SZ(cad),0));
        FOR (i,SZ(cadena))
            if (cadena[i]==cad[0])
                matrix[i][0]=1;
        FOR (i,SZ(cad)-1)
        {
            FOR (j,SZ(cadena))
                if (cadena[j]==cad[i])
                    FORI (k,j+1,SZ(cadena))
                        if (cadena[k]==cad[i+1])
                            matrix[k][i+1]=(matrix[k][i+1]+matrix[j][i])%MOD;
        }
        FOR (i,SZ(cadena))
            resp=(resp+matrix[i][SZ(cad)-1])%MOD;
        printf("Case #%d: %04d\n",casos+1,resp);
    }
    return 0;
}
