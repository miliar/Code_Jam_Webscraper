#include<iostream>
#include<vector>
#include<string>
#include<sstream>
#include<algorithm>
#include<map>
#include<list>
#include<cmath>
#include<set>

using namespace std;
#define forn(i,n) for(int i=0;i<(n);i++)
#define forsn(i,s,n) for(int i = (int)s; i< (int)(n);i++)
#define dforn(i,n) for(int i=(int)(n-1);i>=0;i--)
#define dforsn(i,s,n) for(int i = (int)n; i>= (int)(s);i--)
#define mp make_pair
#define pb push_back
#define all(v) v.begin(),v.end()
#define esta(a,c) (find(c.begin(),c.end(), a) != c.end())
#define min(a,b) (a<b?a:b)
#define max(a,b) (a>b?a:b)
#define MAX 2147483647
#define caso(x,y) "Case #"<<x<<": " <<y<<endl

double r(vector<int> &todos,long long t, int cand,long long acu)
{
    t -= acu;
    t = max(0,t);
    int x = 0;
    while(t>=0 && cand+x < todos.size())
    {
        t-= todos[cand+x]*2;
        x++;
    }
    if (t>= 0)
        return 0;
    else
        return t/(-2.0);
}

int main()
{
    freopen("b4.in","r",stdin);
    freopen("B4.out","w",stdout);
    int tr;
    cin>>tr;
    forn(cc,tr)
    {
        long long L,t,n,c;

        cin>>L>>t>>n>>c;
        vector<int> dist;
        vector<int> can;

        forn(i,c)
        {
            int a;
            cin>>a;
            dist.pb(a);
            can.pb((int)((double)n/(double)c));
        }
        vector<int> todos;
        long long res = 0;
        int lim = 0;
        long long tt = t;
        forn(i,n)
        {
            todos.pb(dist[i%c]);
            res += dist[i%c]*2;
            tt-=dist[i%c]*2;
            if (t > 0)
                lim = i;
        }
        //cout<<res<<endl;

        //int usado = 0;
        long long acu = t;
        vector<int> rest;
        forn(i,todos.size())
        {


            int aux = (acu - todos[i]*2)/-2.0;
            if (acu < 0) aux = todos[i];
            if (aux > 0)
            {
                rest.pb(aux);
            }


            acu-=todos[i];
            acu-=todos[i];
        }
        sort(rest.rbegin(),rest.rend());
        forn(k,L)
        {
            int mejora = rest[k];
            res-=mejora;
        }

        cout<<caso(cc+1,res);

    }
	return 0;

}
