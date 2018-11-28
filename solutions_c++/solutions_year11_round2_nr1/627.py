#include <cstdio>

using namespace std;

const int maxn=110;
int tr,n;
double wp[maxn],owp[maxn],oowp[maxn];
char s[maxn][maxn];

int main(){
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	
	scanf("%d",&tr);
	for (int test=0;test<tr;test++){
		scanf("%d",&n);
		for (int i=0;i<n;i++){
			scanf("%s",s[i]);
			wp[i]=0;
			int sum=0,pw=0;
		        for (int j=0;j<n;j++){
				if (s[i][j]!='.') sum++;
				if (s[i][j]=='1') pw++;
			}
			wp[i]=(double)(pw)/(double)(sum);
			//printf("%.2lf %d %d\n",wp[i],sum,pw);
			//printf("%s\n",s[i]);
		}
		for (int i=0;i<n;i++){
			double sum=0,pw=0;
		        for (int j=0;j<n;j++)
				if (s[i][j]!='.'){
					double kk=0,dd=0;
		                	for (int k=0;k<n;k++)
		                		if (k!=i){
							if (s[j][k]!='.') kk+=1.0;
							if (s[j][k]=='1') dd+=1.0;
						}
					pw+=dd/kk;
					sum+=1.0;
				}
			owp[i]=pw/sum;
			//printf("%.2lf %.2lf %.2lf\n",owp[i],sum,pw);
		}
		//printf("\n");
		for (int i=0;i<n;i++){
			double sum=0,pw=0;
		        for (int j=0;j<n;j++)
		                if (s[i][j]!='.') sum+=1.0,pw+=owp[j];
			oowp[i]=pw/sum;
		}
		printf("Case #%d:\n",test+1);
		for (int i=0;i<n;i++)
		        printf("%.6f\n",0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
	}
	return 0;
	
}
