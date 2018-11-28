#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
#include<algorithm>

#define maxn 110

using namespace std;

int t,r,c,d;
char w[maxn][maxn];
int work(){
	int i,j,k,l;
	int ta,tb,s,m;
	int res=0;
	for(i=0;i<r;i++){
			for(j=0;j<c;j++){
				for(k=2;i+k<r && j+k<c;k++){
					ta=tb=s=0;
					for(l=i;l<=i+k;l++){
						for(m=j;m<=j+k;m++){
							if((l==i || l==i+k) && (m==j || m==j+k))continue;
							ta+=(d+w[l][m]-'0')*l;
							tb+=(d+w[l][m]-'0')*m;
							s+=d+w[l][m]-'0';
						}
					}
					if(2*ta==s*(2*i+k) && 2*tb==s*(2*j+k) && res<k)
						res=k;
				}
			}
		}
	return res;
}
int main(){
	int h,i,j,k;
	int ans;
	int cp,tn;
	for(scanf("%d",&tn),cp=1;cp<=tn;cp++){
		scanf("%d%d%d",&r,&c,&d);
		for(i=0;i<r;i++)
			scanf("%s",w[i]);
		ans=work();
		printf("Case #%d: ",cp);
		if(ans==0)printf("IMPOSSIBLE\n");
		else printf("%d\n",ans+1);
	}
	return 0;
}