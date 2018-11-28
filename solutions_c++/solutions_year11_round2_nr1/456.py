#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>

using namespace std;

char a[200][200];
int win[200],all[200];
double wp[200],owp[200],oowp[200];

int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int T;
	scanf("%d\n",&T);
	for (int tt=1;tt<=T;tt++){
		int n;
		scanf("%d\n",&n);
		for (int i=1;i<=n;i++) {
			for (int j=1;j<=n;j++)	scanf("%c",&a[i][j]);
			scanf("\n");
		}	
		for (int i=1;i<=n;i++){
			all[i]=0;
			win[i]=0;
			for (int j=1;j<=n;j++) if (a[i][j]=='.') continue; else {
				all[i]++;
				if (a[i][j]=='1') win[i]++;
			} 
			wp[i]=(double) win[i]/all[i];
		}
		for (int i=1;i<=n;i++){
			owp[i]=0;
			for (int j=1;j<=n;j++) if (a[i][j]!='.') {
				owp[i]+=(double) (win[j]-(a[j][i]=='1'))/(all[j]-1);
			}
			owp[i]/=all[i];
		}
		for (int i=1;i<=n;i++){
			oowp[i]=0;
			for (int j=1;j<=n;j++) if (a[i][j]!='.') {
				oowp[i]+=owp[j];
			}
			oowp[i]/=all[i];			
		}


		cout <<"Case #"<<tt<<':' ;
		cout <<endl;
		for (int i=1;i<=n;i++) {
			printf("%.8lf\n",0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
		}
	}
	
	return 0;
}
