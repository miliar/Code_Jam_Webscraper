#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>
#include<algorithm>
#include<iterator>
#include<map>
#include<vector>
#include<list>
#include<set>
#include<queue>
#include<cassert>
#include<deque>
#include<stack>
#include<bitset>
#include<functional>
#include<numeric>
#include<utility>
#include<sstream>
#include<iomanip>
#include<string>
#include<cmath>
#include<ctime>
using namespace std;
typedef vector<int> VI; 
typedef vector<VI> VVI; 
typedef pair<int,int> II; 
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++) 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define debug 0
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define REP(i,b) FOR(i,0,b)
#define pos(a) ((int)(a)>=0?(a):-(a))
#define INF 10000000
typedef long long LL;
VI aa,ad,ba,bd;
int main()
{
	int t,cas=0;
	cin>>t;
	while(t--){
		int T;scanf("%d",&T);
		int na,nb;
		scanf("%d%d",&na,&nb);
		aa.clear();ba.clear();ad.clear();bd.clear();
		REP(i,na){
			int h1,m1,h2,m2;
			scanf("%d:%d %d:%d",&h1,&m1,&h2,&m2);
			ad.pb(h1*60+m1);aa.pb(h2*60+m2);
		}
		REP(i,nb){
			int h1,m1,h2,m2;
			scanf("%d:%d %d:%d",&h1,&m1,&h2,&m2);
			bd.pb(h1*60+m1);ba.pb(h2*60+m2);
		}
		sort(ad.begin(),ad.end());
		sort(bd.begin(),bd.end());
		sort(aa.begin(),aa.end());
		sort(ba.begin(),ba.end());
		int ans1=na,ans2=nb;
		bool visited[1000];
		memset(visited,0,sizeof(visited));
		REP(i,nb){
			REP(j,na){
				if(visited[j])continue;
				if(aa[j]>bd[i]-T)break;
				visited[j]=1;
				ans2--;
				break;
			}
		}
		memset(visited,0,sizeof(visited));
		REP(i,na){
			REP(j,nb){
				if(visited[j])continue;
				if(ba[j]>ad[i]-T)break;
				visited[j]=1;
				ans1--;
				break;
			}
		}
		cas++;
		printf("Case #%d: %d %d\n",cas,ans1,ans2);
	}
	return 0;
}
	
