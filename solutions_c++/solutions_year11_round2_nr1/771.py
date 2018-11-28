#include <cstdio>

int main() {

freopen("A.in","r",stdin);
freopen("A.out","w",stdout);

int t;

scanf("%d",&t);

for (int j=0;j<t;j++) {
	int n;        
	scanf("%d",&n);
	char a[100][100];
	char s[101];
	for (int i=0;i<n;i++) {
		scanf("%s",s);
		for (int k=0;k<n;k++)
			{
			if (s[k]=='.') a[i][k]=-1;
				else a[i][k]=s[k]-'0';
			}
		}
	double wp[100];
	int cwin[100];
	int pl[100];
	
	for (int i=0;i<n;i++) {
		pl[i]=0;
		wp[i]=.0;
		cwin[i]=0;
		for (int k=0;k<n;k++) {
			if (a[i][k]>=0) {
				pl[i]++;
				cwin[i]+=a[i][k];
				} 
			}
		wp[i]=(double)cwin[i]/pl[i];
		}

	double owp[100];
	for (int i=0;i<n;i++) {
		owp[i]=.0;
		int nops=0;
		for (int k=0;k<n;k++) {
			int tpl=pl[k];
			int tcwin=cwin[k];
			if (a[k][i]>=0) {
				tcwin-=a[k][i];
				tpl--;
				owp[i]+=(double)tcwin/tpl;
				nops++;
				}

			}
		if (nops) owp[i]/=(double)nops;
		}

	double oowp[100];
	for (int i=0;i<n;i++) {
		oowp[i]=.0;
		int nops=0;
		for (int k=0;k<n;k++) {
			if (a[k][i]>=0) {
				oowp[i]+=owp[k];
				nops++;
				}
			}
		if (nops) oowp[i]/=(double)nops;
		} 
	double rpi[100];
	for (int i=0;i<n;i++) rpi[i]=0.25*wp[i]+0.5*owp[i]+0.25*oowp[i];
	
	printf("Case #%d:\n",j+1);
	for (int i=0;i<n;i++) printf("%.10lf\n",rpi[i]);
	}

return 0;
}
