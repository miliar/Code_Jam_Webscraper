#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<set>
using namespace std;

int t,a,b;
int f[2100000][2];

int main(){
	int h,i,j,k,l,v,n,ans;
	scanf("%d",&t);
	for(h=1;h<=t;h++){
		scanf("%d%d",&a,&b);
		k=a;
		for(j=0,l=1;k>0;k/=10,j++,l*=10);
		n=j;
		ans=0;
		for(i=a;i<=b;i++){
			k=i;
			for(j=0;j<n-1;j++){
				v=k/10+k%10*l/10;
				if(k%10!=0 && v>i && v<=b && v>=a){
					if(f[v][0]!=h || f[v][1]!=i)
						ans++;
					f[v][0]=h;f[v][1]=i;
				}
				k=v;
			}
		}
		printf("Case #%d: %d\n",h,ans);
	}
	return 0;
}
