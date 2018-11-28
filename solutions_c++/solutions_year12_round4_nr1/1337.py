#include <iostream>
#include <cmath>
#include <algorithm>
#include <string.h>
#include <cstdio>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <sstream>

//#pragma comment(linker, "/STACK:167772160")
using namespace std;

#define FOR(i,a,b) for(int i=a;i<=b;++i)
#define sz(s) (int)s.size()
#define pb push_back
#define mp make_pair
#define y1 kfjad
#define y0 fkasj
typedef long long Int;
const int inf=1000000000;
const double pi=2*acos(0.0);
const int md=30000001;

int Dist[70001],d[70001],l[70001];
set< pair<int,int> > q;
bool z[70001];

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tes;
	scanf("%d\n",&tes);
	FOR(TES,1,tes)
	{
		int n;
		cin>>n;
		
		FOR(i,1,n)cin>>d[i]>>l[i];
		int D;cin>>D;
		++n;d[n]=D;l[n]=0;

		FOR(i,1,n)Dist[i]=-1;
		q.clear();
		Dist[1]=d[1];
		q.insert(mp(-Dist[1],1));
		for(;;)
		{
			if(q.empty())break;
			int v=(*q.begin()).second;
			q.erase(*q.begin());

			FOR(i,1,n)
				if(d[i]>=d[v] && Dist[v] >= d[i]-d[v])
				{
					int len=min(l[i],d[i]-d[v]);
					if(Dist[i]>=len)continue;

					q.erase(mp(-Dist[i],i));
					Dist[i]=len;
					q.insert(mp(-Dist[i],i));
				}
		}
		string ans;
		if(Dist[n]!=-1)ans="YES";else
			ans="NO";
		cout<<"Case #"<<TES<<": ";
		cout<<ans<<endl;
	}
	return 0;
}