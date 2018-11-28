#include<iostream>
#include<algorithm>
#include<cstdio>
#include<vector>
#include<cstring>
#include<string>
#include<sstream>
#include<queue>
#include<set>
#include<map>
#include<stack>
#include<ctime>
#include<cstdlib>
#include<cmath>
#include<cassert>
using namespace std;

typedef vector<int> vi;
typedef vector< vector<int> > vvi;
typedef long long ll;

#define I ({int t;scanf("%d",&t);t;})
#define FOR(i,a,b) for(int i = a ; i <= b ; i++)
#define REV(i,a,b) for(int i = a ; i >= b ; i--)
#define REP(i,n) for(int i = 0 ; i < n ; i++)

#define INF 1000000000
#define EPS 1e-7
int cas;

void solve()
{
	double ans = 0.0;
	double X , S , R , T , N ; 
	cin>>X>>S>>R>>T>>N;
	double left = X ;
	double start , end , spd;
	vector<pair<double,double> > V;
	V.clear();
	FOR(i,1,N+1)
	{
		if(i<=N)
		{
			scanf("%lf %lf %lf",&start,&end,&spd);
			V.push_back(make_pair(spd,end-start));
			left -= (end - start);
		}
		else
		{
			V.push_back(make_pair(0,left));
		}
	}
	sort(V.begin(),V.end());
	FOR(i,0,N)
	{
		spd = V[i].first;
		start = 0;
		end = V[i].second;
		//cout<<spd<<" "<<end<<" "<<(spd+S)<<endl;
		if(T >= EPS)
		{
			//cout<<T<<endl;
			double tim = min ( (end - start) / (spd + R) , T );
			T   -= tim ; 
			ans += tim ;
			if( tim > T )
			{
				double todo = (end - start) - tim * (spd + R ) ;
				ans += todo / (spd + S);
			}
			
		}
		else
		{
			ans += (end - start) / (spd + S);
		}
		//cout<<ans<<endl;
	}
	printf("Case #%d: %lf\n",cas,ans);
}

int main()
{
	int T;
	cin>>T;
	while(T--)
	{
		cas++;
		solve();
	}
	return 0;
}
