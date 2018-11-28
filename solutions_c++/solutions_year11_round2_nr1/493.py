#include<cstdio>
#include<cstring>
#include<algorithm>
#define maxn (105)
using namespace std;

int test,Case,N;
double WP[maxn],OWP[maxn],OOWP[maxn];
char s[maxn][maxn];

double calcWP(int i,int j=-1){
	int cnt=0,tot=0;
	for (int k=1;k<=N;k++) if (k!=j){
		if (s[i][k]!='.') tot++;
		if (s[i][k]=='1') cnt++;
	}
	return (double)cnt/tot;
}
int main(){
	freopen("i.txt","r",stdin);
	for (scanf("%d",&test);test--;){
		scanf("%d",&N);
		printf("Case #%d:\n",++Case);
		for (int i=1;i<=N;i++) scanf("%s",s[i]+1);
		for (int i=1;i<=N;i++){
			WP[i]=calcWP(i);
		}
		for (int i=1;i<=N;i++){
			double tot=0;
			int cnt=0;
			for (int j=1;j<=N;j++) if (j!=i && s[i][j]!='.'){
				tot+=calcWP(j,i);
				cnt++;
			}
			OWP[i]=tot/cnt;
		}
		for (int i=1;i<=N;i++){
			double tot=0;
			int cnt=0;
			for (int j=1;j<=N;j++) if (j!=i && s[i][j]!='.'){
				tot+=OWP[j];
				cnt++;
			}
			OOWP[i]=tot/cnt;
		}
		for (int i=1;i<=N;i++) printf("%.12lf\n",0.25*WP[i]+0.5*OWP[i]+0.25*OOWP[i]);
	}
	return 0;
}
