#include<stdio.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<algorithm>
using namespace std;
#define maxn 510
char a[maxn][maxn];
int t,cas;
int n,m,cnt;
int r[maxn][maxn],l[maxn][maxn];
int max(int x,int y)
{
	return x>y?x:y;
}
int main(){
    int i,j,k,kk;
    int ans,tmp,now;
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small.out","w",stdout);
    scanf("%d",&t);
    for (cas=1;cas<=t;cas++){
        scanf("%d%d%d",&n,&m,&cnt);
        for(i=1;i<=n;i++)scanf("%s",a[i]+1);
        for(i=1;i<=n;i++)r[i][0]=0;
		for(j=1;j<=m;j++)l[0][j]=0;
        for(i=1;i<=n;i++)
            for(j=1;j<=m;j++)
                r[i][j]=r[i][j-1]+a[i][j]-'0';
        for(j=1;j<=m;j++)
            for(i=1;i<=n;i++)
            	l[i][j]=l[i-1][j]+a[i][j]-'0';
        ans=0;
        for(i=n;i>1;i--){
            for(j=m;j>1;j--){
                for(k=2;i-k>=1;k++){
                	if(k%2==0){
                    	if(k+1<=ans) continue;
                    	tmp=0;
                    	for(kk=i-k;kk<=i;kk++)
                        	tmp+=(i-k/2-kk)*(r[kk][j]-r[kk][j-k-1]);
                    	tmp-=(i-k/2-(i-k))*(a[i-k][j-k]-'0'+a[i-k][j]-'0');
                    	tmp-=(i-k/2-i)*(a[i][j-k]-'0'+a[i][j]-'0');
                    	if (tmp!=0) continue;
                    	tmp=0;
                    	for(kk=j-k;kk<=j;kk++)
                        	tmp+=(j-k/2-kk)*(l[i][kk]-l[i-k-1][kk]);
                    	tmp-=(i-k/2-(i-k))*(a[i-k][j-k]-'0'+a[i][j-k]-'0');
                    	tmp-=(i-k/2-i)*(a[i-k][j]-'0'+a[i][j]-'0');
                    	if(tmp!=0) continue;
                    	ans=max(ans,k+1);
                	}else {
                    	if(k+1<=ans) continue;
                    	tmp=0;
						now =(k+1)/2;
                    	for(kk=i-k;kk<=i;kk++,now==1?now-=2:now--)
                        	tmp+=(now)*(r[kk][j]-r[kk][j-k-1]);
                    	tmp-=((k+1)/2)*(a[i-k][j-k]-'0'+a[i-k][j]-'0');
                    	tmp-=(-(k+1)/2)*(a[i][j-k]-'0'+a[i][j]-'0');
                    	if(tmp!=0) continue;
                    	tmp=0;now=(k+1)/2;
                    	for(kk=j-k;kk<=j;kk++,now==1?now-=2:now--)
                        	tmp+=(now)*(l[i][kk]-l[i-k-1][kk]);
    	 				tmp-=((k+1)/2)*(a[i-k][j-k]-'0'+a[i][j-k]-'0');
                    	tmp-=(-(k+1)/2)*(a[i-k][j]-'0'+a[i][j]-'0');
                    	if(tmp!=0) continue;
                    	ans = max(ans,k+1);
                	}
            	}
            }
        }
     	printf("Case #%d: ",cas);
     	if (ans==0) printf("IMPOSSIBLE\n");
     	else printf("%d\n",ans);
   }
   return  0;
}

