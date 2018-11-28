#include <cstdio>
#include <cstring>

using namespace std;

const int maxn=1100000;
int tr,tot,prime[maxn];
bool vis[maxn];
long long n;

inline void ready(){
	memset(vis,0,sizeof(vis));
	tot=0;
	for (int i=2;i<=1000000;i++){
		if (!vis[i])
			prime[tot++]=i;
		for (int j=0;j<tot&&i*prime[j]<=1000000;j++){
			vis[i*prime[j]]=true;
			if (!i%prime[j]) break;
		}
	}
}

int main(){
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	
	ready();
	scanf("%d",&tr);
	for (int test=0;test<tr;test++){
		scanf("%I64d",&n);
		printf("Case #%d: ",test+1);
		if (n==1) printf("0\n");
		else{
			int ans=0;
			for (int i=0;i<tot;i++)
				if (prime[i]<=n){
					int p=0;
					long long f=1;
					while (f*(long long)(prime[i])<=n)
						f*=(long long)(prime[i]),p++;
					ans+=p-1;
				}
				else break;
			printf("%d\n",ans+1);
		}
	}
	return 0;
}
