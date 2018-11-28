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
#define dforn(i,n) for(int i = ((int)n)-1; i >= 0; i--)
#define all(v) v.begin(), v.end()
#define pb push_back

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int casos;
    cin >> casos;
    forn(casito,casos)
    {
        int n,k;
        cin >> n >> k;
        k++;
        k %= (1<<n);
        string res = "OFF";
        if(k==0)
            res = "ON";
        cout << "Case #" << casito+1 << ": " << res << endl;
    }
}
