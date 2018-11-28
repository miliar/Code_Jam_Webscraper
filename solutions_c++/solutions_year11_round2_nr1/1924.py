#include<cstdio>
#include<iostream>

using namespace std;
int t,n,itung;
double wp[105],owp[105],oowp[105], jum[105],win[105];
char kar[105][105];
int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	scanf("%d",&t);
	
	for (int tc=1;tc<=t;tc++){
		printf("Case #%d:\n",tc);
		scanf("%d",&n);
		for (int i=0;i<n;i++){
			jum[i]=0;
			win[i]=0;
			scanf("%s",&kar[i]);
			for (int j=0;j<n;j++){
				if (kar[i][j]!='.'){
					jum[i]++;
					if (kar[i][j]=='1')win[i]++;
				}
			}
//			printf("%g %g\n",win[i],jum[i]);
			wp[i]=win[i]/jum[i];
//			printf("%.8g\n",wp[i]);
		}
		for (int i=0;i<n;i++){
			owp[i]=0.0;
			itung=0;
			for (int j=0;j<n;j++){
				if (j==i || kar[i][j]=='.'){
					itung++;
					continue;
				}
				if (kar[j][i]=='1')owp[i]+=(win[j]-1.0)/(jum[j]-1.0);
				else if (kar[j][i]=='0')owp[i]+=(win[j])/(jum[j]-1.0);
			}
			owp[i] = owp[i]/ (jum[i]);
//			printf("%.8g %g\n",owp[i],n-itung*1.0);
			
		}
		for (int i=0;i<n;i++){
			oowp[i]=0;
			itung=0;
			for (int j=0;j<n;j++){
				if (j==i || kar[i][j]=='.'){
					itung++;
					continue;
				}
				oowp[i] +=owp[j];
			}
			oowp[i] = oowp[i]/ (n-itung*1.0);
//			printf("%.8g\n",oowp[i]);
			printf("%.8g\n",(wp[i])/4+(owp[i])/2+(oowp[i])/4);
		}
		
		//calculate wp
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
