#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
#include<cstdlib>
#include<windows.h>
#include<set>
using namespace std;

int t,n;
int a[21];
int dv[4010000];
int x[21],y[21],xx,yy;

int main(){
	int h,i,j,k,l;
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	scanf("%d",&t);
	int m=2000000;
	for(h=1;h<=t;h++){
		scanf("%d",&n);
		xx=yy=0;
		for(i=0;i<n;i++)
			scanf("%d",&a[i]);
		memset(dv,-1,sizeof(dv));
		dv[m]=0;
		for(i=0;i<n;i++){
			for(j=0;j<=m*2;j++){
				if(dv[j]!=-1 && dv[j]!=i){
					if(dv[j-a[i]]==-1){
						dv[j-a[i]]=i;
					}else if(j-a[i]==m){
						x[xx++]=a[i];
						break;
					}
				}
			}
			if(j<=m*2)break;
			for(j=m*2;j>=0;j--){
				if(dv[j]!=-1 && dv[j]!=i){
					if(dv[j+a[i]]==-1){
						dv[j+a[i]]=i;
					}else if(j+a[i]==m){
						y[yy++]=a[i];
						break;
					}
				}
			}
			if(j>=0)break;
		}
		if(i<n){
			i--;
			while(j!=m){
					if(dv[j-a[dv[j]]]<=i && dv[j-a[dv[j]]]!=-1){
						y[yy++]=a[dv[j]];
						i=dv[j-a[dv[j]]];
						j-=a[dv[j]];
					}else if(dv[j+a[dv[j]]]<=i && dv[j+a[dv[j]]]!=-1){
						x[xx++]=a[dv[j]];
						i=dv[j+a[dv[j]]];
						j+=a[dv[j]];
					}
			}
		}
		printf("Case #%d:\n",h);
		if(yy>0 || xx>0){
			for(i=0;i<xx;i++){
				printf("%d",x[i]);
				if(i==xx-1)putchar('\n');
				else putchar(' ');
			}
			for(i=0;i<yy;i++){
				printf("%d",y[i]);
				if(i==yy-1)putchar('\n');
				else putchar(' ');
			}
		}else{
			printf("Impossible\n");
		}
	}
	//Sleep(1000);
	return 0;
}