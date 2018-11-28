#include<cstdio>
#include<algorithm>
using namespace std;

int gcd(int a,int b){
	if(a<b) { int t=a; a=b; b=t; }
	if(b==0)  return a;
	return gcd(b,a%b);
}

int main(){
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	int i,c,n,t[10],f=1;
	scanf("%d",&c);
	while(c--){
		scanf("%d",&n);
		for(i=0;i<n;i++){
			scanf("%d",&t[i]);
			t[i]=-t[i];
		}		
		sort(t,t+n);
		if(n==2){
			int x=(-t[1])/(t[1]-t[0]);
			while(t[1]+x*(t[1]-t[0])<0){
				x++;
			}
			printf("Case #%d: ",f++);
			printf("%d\n",t[1]+x*(t[1]-t[0]));
		}
		else{
			int gcd1=gcd(t[1]-t[0],t[2]-t[1]);
			int x=(-t[2])/gcd1;
			while(t[2]+x*gcd1<0){
				x++;
			}
			printf("Case #%d: ",f++);
			printf("%d\n",t[2]+x*gcd1);
		}
	}
	return 0;
}
