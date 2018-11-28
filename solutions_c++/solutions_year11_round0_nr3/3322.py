#include <cstdio>


using namespace std;

int t,n;
long long int c[10000];

int main(){
	freopen("candy.in","r",stdin);
	freopen("candy.out","w",stdout);
	scanf("%d",&t);
	for (int k=0;k<t;k++){
		long long int sum=0, xor=0, min=-1;
		scanf("%d",&n);
		for (int i=0;i<n;i++){
			scanf("%lld",&c[i]);
			xor=xor^c[i];
			sum=sum+c[i];
			if (min==-1)min=c[i];
			if (min>c[i]) min=c[i];
		}
		printf("Case #%d: ",k+1);
		printf((xor==0)?"%lld\n":"NO\n",sum-min);
	}
	return 0;
}