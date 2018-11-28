#include<ctime>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<string>
#include<vector>
#include<sstream>
#include<iostream>
#include<algorithm>
#include<queue>
#include<stack>
#include<set>
#include<map>
#include<numeric>
#include<cmath>
#include<locale>
using namespace std;
#define all(x) (x).begin(),(x).end()
#define sz(a) (int((a).size()))
typedef istringstream iss; typedef ostringstream oss; typedef long long lli;
const double TOLL=1e-9;

int main()
{
    int t; int cn=0; cin>>t;
    while(t--)
    {
	int done[110];
	for(int i=1;i<101;i++) done[i]=1000000000;
	int n; cin>>n; int rv=0;
	char rr; int s;
	int opos=1, bpos=1;
	vector<pair<int,int> > o,b;
	for(int i=0;i<n;i++)
	{
	    cin>>rr>>s;
	    if(rr=='O') o.push_back(make_pair(s,i+1));
	    else b.push_back(make_pair(s,i+1));
	}
	done[0]=0;
	int r=0;
	for(r=1;;r++)
	{
	    if(sz(o)==0 && sz(b)==0) break;
	    if(sz(o))
	    {
		if(opos<o[0].first) opos++;
		else if(opos>o[0].first) opos--;
		else if(opos==o[0].first)
		{
		    if(done[o[0].second-1]<r)
		    {
			done[o[0].second]=r;
			o.erase(o.begin());
		    }
		}
	    }

	    if(sz(b))
	    {
		if(bpos<b[0].first) bpos++;
		else if(bpos>b[0].first) bpos--;
		else if(bpos==b[0].first)
		{
		    if(done[b[0].second-1]<r)
		    {
			done[b[0].second]=r;
			b.erase(b.begin());
		    }
		}
	    }
	}
	printf("Case #%d: %d\n",++cn,r-1);
    }

}
