#include<algorithm>
#include<cmath>
#include<fstream>
#include<iomanip>
#include<iostream>
#include<map>
#include<queue>
#include<set>
#include<sstream>
#include<stack>
#include<vector>

using namespace std;

#define forn(i,n) for(int i = 0; i < (n); i++)
#define dforn(i,n) for(int i = (int)(n-1); i >= 0; i--)
#define all(v) v.begin(), v.end()
#define pb push_back

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    long long n;
    int t, e, casos;
    cin >> casos;
    forn(casito,casos)
    {
        cin >> n >> t >> e;
        cout << "Case #" << casito+1 << ": ";
        if(n>100)
            n = 100;
        bool b = false;
        for(int i=1;i<=n;i++)
        {
            forn(j,i+1)
            {
                if(j*100==i*t)
                    b = true;
            }
        }
        if(t<100&&e==100)
            b = false;
        if(t>0&&e==0)
            b = false;
        if(b==true)
            cout << "Possible" << endl;
        else
            cout << "Broken" << endl;
    }
}
