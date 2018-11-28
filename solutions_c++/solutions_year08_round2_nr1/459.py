#include <cstdio>

using namespace std;

int X[100001],Y[100001];
const int w[3]={0,2,1};

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int n, A, B, C, D, M;
	long long mods[9]={0};
	int N,i,m;
	long long ans,t,x0,y0;
	scanf("%d",&N);
	for(int q=1;q<=N;q++){
		scanf("%d%d%d%d%d%lld%lld%d",&n,&A,&B,&C,&D,&x0,&y0,&M);
		ans=0;
		for(i=0;i<9;i++)mods[i]=0;
		for(i=0;i<n;i++){
			mods[3*(x0%3)+y0%3]++;
			X[i]=x0;
			Y[i]=y0;
			x0 = (A * x0 + B) % M;
			y0 = (C * y0 + D) % M;
		}
		for(i=0;i<n-1;i++)
			for(int j=i+1;j<n;j++){
				m=3*(w[(X[i]+X[j])%3])+w[(Y[i]+Y[j])%3];
				ans+=mods[m];
				if(m==3*(X[i]%3)+Y[i]%3)ans--;
				if(m==3*(X[j]%3)+Y[j]%3)ans--;
			}
		printf("Case #%d: %lld\n",q,ans/3);
	}	

	return 0;
}


//compiled with Visual Studio 2005
