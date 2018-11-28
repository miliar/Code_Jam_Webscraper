#include <iostream>
#include <cstring>
#include <cstdio>
#include <string>
using namespace std;
#define MaxN 100
char s[MaxN+5][MaxN+5];
int n;
double owp[MaxN+5];
double wp[MaxN+5];
double oowp[MaxN+5];
void calwp(){
	int i,j;
	int cnt,win;
	for (i=0;i<n;i++){
		cnt=0;
		win=0;
		for (j=0;j<n;j++){
			if (s[i][j]!='.'){
				cnt++;
				if (s[i][j]=='1') win++;
			}
		}
		wp[i]=double(win)/cnt;
	}
}
void calowp(){
	int i,j,k;
	int cnt,win,tot;
	double tmp;
	for (i=0;i<n;i++){
		tmp=0;
		tot=0;
		for (j=0;j<n;j++){
			if (s[i][j]!='.'){
				tot++;
				cnt=0;
				win=0;
				for (k=0;k<n;k++){
					if (k!=i && s[j][k]!='.'){
						cnt++;
						if (s[j][k]=='1') win++;
					}
				}
				tmp+=double(win)/cnt;
			}
		}
		owp[i]=tmp/tot;
	}
}
void caloowp(){
	int i,j;
	int tot;
	for (i=0;i<n;i++){
		tot=0;
		oowp[i]=0;
		for (j=0;j<n;j++){
			if (s[i][j]!='.'){
				tot++;
				oowp[i]+=owp[j];
			}
		}
		oowp[i]/=tot;
	}
}
void init(){
	int i;
	scanf("%d",&n);
	for (i=0;i<n;i++){
		scanf("%s",&s[i]);
	}
}
void solve(){
	int i;
	double ans;
	calwp();
	calowp();
	caloowp();
	for (i=0;i<n;i++){
		ans=wp[i]*0.25+owp[i]*0.5+oowp[i]*0.25;
		printf("%lf\n",ans);
	}
}
int main()
{
//	freopen("data.txt","r",stdin);
//	freopen("A-small-attempt0.in","r",stdin);
//	freopen("A-small-attempt0.out","w",stdout);
	int i,t;
	scanf("%d",&t);
	for (i=1;i<=t;i++){
		printf("Case #%d:\n",i);
		init();
		solve();
	}
	return 0;
}