//BISMILLAHIRRAHMANIRRAHIM

#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int nxt[1009];
unsigned long long dp[1009];
int g[1009];

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("Cl2.out","w",stdout);
	
	int i,j,k,n,T,I,t,r;
	unsigned long long s;
	cin>>T;
	for(I=1;I<=T;I++) {
		cin>>r>>k>>n;
		for(i=0;i<n;i++) scanf("%d",&g[i]);
		s=0;
		for(i=0;i<n;i++) {
			t=k;
			j=i;
			dp[i]=0;
			while(t>=g[j]) {
				dp[i]+=g[j];
				t-=g[j];
				j=(j+1)%n;
				if(j==i) break;
			}
			nxt[i]=j;
		}
		s=0;
		i=0;
		while(r--) {
			s+=dp[i];
			i=nxt[i];
		}
		printf("Case #%d: %Lu\n",I,s);
	}
	return 0;
}
