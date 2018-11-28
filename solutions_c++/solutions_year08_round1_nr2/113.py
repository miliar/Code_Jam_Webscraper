#include<iostream>
#include<sstream>
#include<vector>
#include<string>
#include<algorithm>
#include<cmath>
#include<queue>
#include<map>
#include<set>
using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;
#define Pi acos(-1.0)
#define Eps (1e-9)
#define pb push_back
#define mp make_pair
#define MIN(a,b) ((a)<(b)?(a):(b))
#define MAX(a,b) ((a)>(b)?(a):(b))
#define sqr(a) ((a)*(a))
#define ALL(a) (a).begin(),(a).end()
#define SORT(a) sort(ALL(a))
bool nu[2001][2001];
int main()
{
	freopen("F.in","r",stdin);
	freopen("F.out","w",stdout);
	int T,ind=0;
	cin>>T;

	while(T)
	{
		T--;
		ind++;
		int N,M;
		cin>>N>>M;
		int od[2001];
		memset(od,0,sizeof(od));
		memset(nu,0,sizeof(nu));
		bool zad[2001];
		memset(zad,0,sizeof(zad));
		int res[2001];
		memset(res,0,sizeof(res));
		int kil[2001];
		memset(kil,0,sizeof(kil));
		int i,j;
		for(i=1;i<=M;i++)
		{
			int K;
			scanf("%d",&K);
			for(j=0;j<K;j++)
			{
				int t,tt;
				scanf("%d %d",&t,&tt);
				if(tt==0)
				{
					kil[i]++;
					nu[i][t]=true;
				}
				else
				{
					od[i]=t;
				}
			}
		}
		while(true)
		{
			int pot=0;
			for(i=1;i<=M;i++)
				if(!zad[i] && !kil[i])
				{
					if(od[i])pot=od[i];
					break;
				}
			if(!pot)break;
			res[pot]=1;
			for(i=1;i<=M;i++)
				if(!zad[i])
				{
					if(od[i]==pot)zad[i]=true;
					if(nu[i][pot])kil[i]--;
				}
		}
		bool f=true;
		for(i=1;i<=M;i++)
		{
			if(zad[i])continue;
			bool ff=false;
			for(j=1;j<=N;j++)
				if(nu[i][j] && !res[j])
				{
					ff=true;
					break;
				}
			if(!ff)
			{
				f=false;
				break;
			}
		}
		cout<<"Case #"<<ind<<":";
		if(!f)
		{
			cout<<" IMPOSSIBLE"<<endl;
		}
		else
		{
			for(i=1;i<=N;i++)cout<<" "<<res[i];
			cout<<endl;
		}
	}
	return 0;
}

