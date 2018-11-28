#include <stdio.h>

char b[100][101];
int n;
double twp(int i,int to){
	int w=0,a=0;
	for(int j=0;j<n;j++){
		if(j==to)
			continue;
		if(b[i][j]=='1')
			w++;
		if(b[i][j]!='.')
			a++;
	}
	return 1.0*w/a;
}

int main(){
	int T;
	scanf("%d", &T);
	for(int TT=1;TT<=T;TT++){
		
		scanf("%d", &n);
		double wp[100],owp[100],oowp[100];
		for(int i=0;i<n;i++){
			scanf("%s", b[i]);
			int w=0,a=0;
			for(int j=0;j<n;j++){
				if(b[i][j]=='1')
					w++;
				if(b[i][j]!='.')
					a++;
			}
			wp[i] = 1.0*w/a;
		}
		for(int i=0;i<n;i++){
			owp[i]=0;
			int a=0;
			for(int j=0;j<n;j++){
				if(b[i][j]!='.'){
					owp[i]+=twp(j,i);
					a++;
				}
			}
			owp[i]/=a;
		}
		for(int i=0;i<n;i++){
			oowp[i]=0;
			int a=0;
			for(int j=0;j<n;j++){
				if(b[i][j]!='.'){
					oowp[i]+=owp[j];
					a++;
				}
			}
			oowp[i]/=a;
		}
		
		printf("Case #%d:\n", TT);
		for(int i=0;i<n;i++){
			printf("%.16lf\n", 0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
		}
	}
}