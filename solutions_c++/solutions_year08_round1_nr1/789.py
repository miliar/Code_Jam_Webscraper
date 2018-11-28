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
#define FORE(i, x) for (typeof((x).begin()) i = (x).begin(); i != (x).end(); i++)
#define SZ(x) ((int) (x).size())
 
using namespace std;

int main()
{    
    freopen("A-small-attempt0.in","r",stdin);
    freopen("salida.out","w",stdout);
    int casos;
    cin>>casos;
    FOR (cases,casos)
    {
        int n;
        long long resp=0;
        cin>>n;
        vector<int> v1(n),v2(n);
        FOR (i,n)
            cin>>v1[i];
        FOR (i,n)
            cin>>v2[i]; 
        sort(ALL(v1));
        sort(ALL(v2));
        for (int i=0,j=SZ(v1)-1;i<SZ(v1);i++,j--)
            resp+=v1[i]*v2[j];
        cout<<"Case #"<<cases+1<<": "<<resp<<endl;
    }
    return 0;
}
