#include <cstdio>
#include <vector>
#define fi first
#define se second
#define pb push_back
using namespace std;
typedef long long ll;
typedef pair<ll,ll> pi;
ll t[9];
int main()
{
	int N;
	scanf("%d",&N);
	for (int u=1; u<=N; u++)
	{
		int n,A,B,C,D,x,y,M;
		scanf("%d %d %d %d %d %d %d %d",&n,&A,&B,&C,&D,&x,&y,&M);
		ll X = x, Y = y;
		for (int i=0; i<9; i++)
			t[i]=0;
		for (int i=0; i<n; i++)
		{
			t[(X%3)*3+Y%3]++;
			//printf("%lld %lld\n",X,Y);
			X = (A * X + B) % M;
			Y = (C * Y + D) % M;	
		}
		//for (int i=0; i<9; i++)
		//	printf("%d: %lld\n",i,t[i]);
		long long wynik=0;
		for (int i=0; i<9; i++)
			for (int j=i; j<9; j++)
				for (int k=j; k<9; k++)
				{
					int p=i%3+j%3+k%3;
					int q=i/3+j/3+k/3;
					if (p%3!=0||q%3!=0) continue;
					if (i==j&&i==k) 
					{
						//printf("dodaje %lld\n",t[i]*(t[i]-1)*(t[i]-2)/6);
						wynik+=t[i]*(t[i]-1)*(t[i]-2)/6;
					}
					else wynik+=t[i]*t[j]*t[k];
					//printf("%d %d %d %lld\n",i,j,k,wynik);
				}
		printf("Case #%d: %lld\n",u,wynik);
	}
}
