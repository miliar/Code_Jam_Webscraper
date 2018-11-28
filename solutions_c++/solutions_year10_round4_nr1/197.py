#include <stdio.h>
#include <algorithm>
#include <utility>
using namespace std;


main(){
	int tests;
	scanf("%d",&tests);
	for(int t=1;t<=tests;t++){
		int n;
		scanf("%d",&n);
		char hoge[100];
		gets(hoge);
		int a[120][120];
		for(int i=0;i<=2*n-2;i++)for(int j=0;j<=2*n-2;j++)a[i][j]=-1;
		for(int i=0;i<=2*n-2;i++){
			char buf[200];
			gets(buf);
			while(buf[strlen(buf)-1]<32)buf[strlen(buf)-1]=0;
			//for(int j=0;j<strlen(buf);j++)printf("%d ",buf[j]);puts("");
			//printf("[ %s ]\n",buf);
			int l=strlen(buf);
			for(int j=0;j<l;j++){
				if(buf[j]>='0' && buf[j]<='9')a[i][j]=buf[j]-'0';
			}
		}
		int ngx[120]={0},ngy[120]={0};
		for(int i=0;i<=2*n-2;i++){
			for(int j=0;j<=2*n-2;j++){
				for(int k=0;k<=2*n-2;k++){
					for(int l=0;l<=2*n-2;l++){
						if(a[i][j]==-1 || a[k][l]==-1 || a[i][j]==a[k][l])continue;
						if(i==k)ngy[(j+l)/2]=1;
						if(j==l)ngx[(i+k)/2]=1;
					}
				}
			}
		}
		//for(int i=0;i<=2*n-2;i++)printf("%d",ngx[i]);puts("");
		//for(int i=0;i<=2*n-2;i++)printf("%d",ngy[i]);puts("");
		int ans=999999999;
		for(int i=0;i<=2*n-2;i++){
			for(int j=0;j<=2*n-2;j++){
				if(ngx[i]==0 && ngy[j]==0){
					int siz=n+abs(i-(n-1))+abs(j-(n-1));
					ans=min(ans,siz*siz-n*n);
				}
			}
		}
		printf("Case #%d: %d\n",t,ans);
	}
}