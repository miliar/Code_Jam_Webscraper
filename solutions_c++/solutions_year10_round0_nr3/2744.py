#include<iostream>
#include<algorithm>
using namespace std;

const int maxn = 1000 + 5;

int next[maxn],en[maxn];
int N,R,K;
int a[maxn];
long long sum;
int q[10*maxn];
bool vis[maxn];
int main()
{
	int T,Tn=0;
	for(cin>>T;T;T--)
	{
		Tn++;
		cin>>R>>K>>N;
		for( int i = 1;i<=N;i++ ) cin>>a[i];
		for( int i = 1;i<=N;i++ )
		{
			int &j = next[i];
			int &cur = en[i];

			j = i;cur = 0;
			while(1)
			{
				if(cur + a[j]>K) break;
				cur+=a[j];
				j = j%N + 1;
				if(j==i) break;
			}

			//cout<<next[i]<<" "<<en[i]<<endl;
		}

		long long ans = 0;
		if( R <= 10000 )
		{
			int cur = 1;
			while(R--)
			{
				ans+=en[cur];
				cur = next[cur];
			}
		}else
		{
			for(int i = 1;i<=N;i++) vis[i] = true;
			q[1] = 1;int top = 1;
			while( vis[q[top]] )
			{
				vis[ q[top] ] = false;
				q[top+1] = next[ q[top] ];
				top++;
			}
			int m = 1;while( q[m]!=q[top] ) m++;

			// 1~m-1 (m~top-1)
			for( int i=1;i<=m-1;i++) ans+=en[i];R-=(m-1);
			long long sum = 0;
			for( int i=m;i<top;i++) sum+=en[i];
			ans+=R/(top-m) * sum;
			R%=(top-m);
			for( int i=m;i<m+R;i++) ans+=en[i];
		}

		cout<<"Case #"<<Tn<<": "<<ans<<endl;
	}
	return 0;
}
