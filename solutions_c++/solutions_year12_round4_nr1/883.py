#include<algorithm>
#include<cmath>
#include<cstdio>
#include<iostream>
#include<map>
#include<queue>
#include<set>
#include<sstream>
#include<string>
#include<vector>

#define forn(i,n) for(int i=0;i<(int)n;i++)
#define dforn(i,n) for(int i=(int)n-1;i>=0;i--)
#define all(v) v.begin(),v.end()

using namespace std;

vector<int> d,l;

int ultima[10001][10001];

int main()
{
	#ifdef ACMTUYO
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	#endif
	int casos;
	cin >> casos;
	forn(casito,casos)
	{
	    string res = "NO";
	    int n;
	    cin >> n;
	    d.resize(n+1);
	    l.resize(n+1);
	    forn(i,n)
            cin >> d[i] >> l[i];
        cin >> d[n];
        l[n] = d[n];
        queue<pair<int,int> > cola;
        cola.push(make_pair(0,0));
        while(!cola.empty())
        {
            int v = cola.front().first;
            if(v==n)
            {
                res = "YES";
                break;
            }
            int x = cola.front().second;
            cola.pop();
            for(int i=v+1;i<=n;i++)
            if(d[v]+(d[v]-x)>=d[i])
               cola.push(make_pair(i,max(d[v],d[i]-l[i])));
            else
                break;
        }
	    cout <<"Case #"<< casito+1 <<": " << res << endl;
	}
}
