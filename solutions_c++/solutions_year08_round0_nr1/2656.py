#include<iostream>
#define fr(i,a,b) for(i=a;i<=b;i++)
using namespace std;
const int maxn=102;
const int maxl=102;
int ca,i,j,n,m,t,ans,tot;
char s[maxn][maxl],tmp[maxl];
bool u[maxn];
int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d\n",&ca);
	fr(t,1,ca){
		scanf("%d\n",&n);
		fr(i,1,n)
			gets(s[i]);
		ans=0;
		scanf("%d\n",&m);
		memset(u,0,sizeof(u));
		tot=0;
		fr(i,1,m){
			gets(tmp);
			fr(j,1,n)
				if(!u[j]&&strcmp(tmp,s[j])==0){
					u[j]=true;
					tot++;
				}
			if(tot==n){
				memset(u,0,sizeof(u));
				tot=0;
				fr(j,1,n)
					if(!u[j]&&strcmp(tmp,s[j])==0){
						u[j]=true;
						tot++;
					}
				ans++;
			}
		}
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}
