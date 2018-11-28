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
    int casos;
    cin >> casos;
    forn(casito,casos)
    {
        int x,s,r,n;
        long double t;
        cin >> x >> s >> r >> t >> n;
        r -= s;
        vector<pair<pair<int,int>,int> > w(n);
        forn(i,n)
            cin >> w[i].first.first >> w[i].first.second >> w[i].second;
        vector<pair<int,int> > vec;
        forn(i,n)
            vec.push_back(make_pair(w[i].second+s,w[i].first.second-w[i].first.first));
        int d = x;
        forn(i,n)
            x -= vec[i].second;
        vec.push_back(make_pair(s,x));
        sort(all(vec));
        long double res = 0;
        forn(i,n+1)
        {
            long double tiempo = (long double)(vec[i].second)/(long double)(vec[i].first+r);
            if(tiempo <= t)
            {
                t -= tiempo;
                res += tiempo;
                d -= vec[i].second;
            }
            else
            {
                long double t2 = t/tiempo, t3 = 1-t2;
                t=0;
                long double t4 = (long double)(vec[i].second)*t2/(long double)(vec[i].first+r);
                long double t5 = (long double)(vec[i].second)*t3/(long double)(vec[i].first);
                res += t4+t5;
                d -= vec[i].second;
            }
        }
        printf("Case #%d: %.8f\n",casito+1,(double)res);
    }
}
