#include<cstdio>
#include<vector>
#include<algorithm>
#include<set>
#include<string>
#include<map>
#include<iostream>
using namespace std;

int tc;
int n;
char a[105][105];
double wp[105],owp[105],oowp[105],nop[105][105];

int main() {
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d",&tc);
    for (int T=1; T<=tc; T++) {
		scanf("%d",&n);
		for (int i=0; i<n; i++)	
			scanf("%s",&a[i]);
		for (int i=0; i<n; i++) {
			int c1=0,c2=0;
			for (int j=0; j<n; j++) {
				if (a[i][j]!='.') c2++;
				if (a[i][j]=='1') c1++;
			}
			wp[i]=c1*1.0/c2;
			for (int j=0; j<n; j++) {
				if (a[i][j]=='0') nop[i][j]=c1*1.0/(c2-1);
				if (a[i][j]=='1') nop[i][j]=(c1-1)*1.0/(c2-1);
			}
		}
		for (int i=0; i<n; i++) {
			int c2=0;
			double c1=0;
			for (int j=0; j<n; j++) {
				if (a[i][j]!='.') c2++,c1+=nop[j][i];
			}
			owp[i]=c1*1.0/c2;
		}
		for (int i=0; i<n; i++) {
			int c2=0;
			double c1=0;
			for (int j=0; j<n; j++) {
				if (a[i][j]!='.') c2++,c1+=owp[j];
			}
			oowp[i]=c1*1.0/c2;
		}
		printf("Case #%d:\n",T);
		for (int i=0; i<n; i++)
			printf("%.9f\n",wp[i]*.25+owp[i]*.5+oowp[i]*.25);
	}
}
