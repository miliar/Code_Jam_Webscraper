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
typedef long long tint;

pair<int,int> calc(vector<int> vec, int pos, int k, int n)
{
    int res = vec[pos];
    int pos2 =(pos+1)%n;
    while(res+vec[pos2]<=k&&pos2!=pos)
    {
        res += vec[pos2];
        pos2++;
        pos2%=n;
    }
    return make_pair(res,pos2);
}

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int casos;
    cin >> casos;
    tint res;
    forn(casito,casos)
    {
        int r, k, n;
        cin >>r >> k >> n;
        vector<int> vec(n);
        forn(i,n)
            cin >> vec[i];
        vector<pair<int,int> > grupos(n);
        forn(i,n)
            grupos[i] = calc(vec,i,k,n);
        res = 0;
        int pos = 0;
        forn(i,r)
        {
            res+=grupos[pos].first;
            pos = grupos[pos].second;
        }
        cout << "Case #" << casito+1 << ": " << res << endl;
    }
}
