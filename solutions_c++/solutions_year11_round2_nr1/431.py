#include <stdio.h>
#include <string.h>

int n;
char mat[110][110];
int wpu[110],wpd[110],owpu[110],owpd[110],oowpu[110],oowpd[110];
double wp[110], owp[110], oowp[110];
double ans[110];

int main() {
	int t,c=0;
	
	scanf("%d",&t);
	while(t--) {
		scanf("%d",&n);
		for(int i=1;i<=n;++i)
			scanf("%s",mat[i]+1);
		memset(wpu,0,sizeof(wpu));
		memset(wpd,0,sizeof(wpd));
		memset(owpu,0,sizeof(owpu));
		memset(owpd,0,sizeof(owpd));
		memset(oowpu,0,sizeof(oowpu));
		memset(oowpd,0,sizeof(oowpd));
		for(int i=1;i<=n;++i) {
			//wp
			int cnt=0;
			int num=0;
			wpu[i] = 0;
			for(int j=1;j<=n;++j) 
				if(i != j && mat[i][j] != '.') {
					++cnt;
					++wpd[i];
					if(mat[i][j] == '1') {
						++num;
						++wpu[i];
					}
				}
			wp[i] = (double)num/cnt;
			//owp
			int total = 0;
			owp[i] = 0;
			for(int j=1;j<=n;++j) {
				if(mat[i][j] == '.')	continue;
				++total;
				int ss = 0;
				int ff = 0;
				double tp;
				for(int k=1;k<=n;++k)
					if(k != j && k != i && mat[j][k] != '.') {
						++ss;
						if(mat[j][k] == '1')
							++ff;
					}
				tp = (double)ff/ss;
				owp[i] += tp;
			}
			owp[i] /= total;
			
			
		}
		for(int i=1;i<=n;++i) {
			//oowp
			int cff = 0;
			oowp[i] = 0;
			for(int j=1;j<=n;++j) {
				if(mat[i][j] == '.')	continue;
				++cff;
				oowp[i] += owp[j];
			}
			oowp[i] /= (double)cff;
		}
			
		for(int i=1;i<=n;++i)
			ans[i] = 0.25*wp[i]+0.5*owp[i]+0.25*oowp[i];
		printf("Case #%d:\n",++c);
		for(int i=1;i<=n;++i)
			printf("%.6lf\n",ans[i]);
	}
	
	return 0;
}
