#include<stdio.h>
#include<string.h>
inline int abs(int a){
	if(a<0)return -a;
	else return a;
}
#define max(a,b) ((a>b) ? (a) : (b))
//com a[128];
int solve(){
	int n;
	char a[102][102];
	scanf("%d\n",&n);
	double wp[102];
	double owp[102];
	double oowp[102];
	int i,j;
	for(i=0;i<n;i++)
		gets(a[i]);
	double s[102];
	for(i=0;i<n;i++){
		wp[i]=0;
		s[i]=0;
		for(j=0;j<n;j++)
		{
			if(a[i][j]=='1'){
				s[i]+=1.0;
				wp[i]+=1.0;
			}
			else if(a[i][j]=='0')s[i]+=1.0;
		}
	}

	double sum;
	for(i=0;i<n;i++){
		owp[i]=0;
		sum=0;
		for(j=0;j<n;j++)
		{
			if(i!=j){
				if(a[i][j]=='1'){
					sum+=1.0;
					owp[i]+=wp[j]/(s[j]-1.0);
				}
				else if(a[i][j]=='0'){
					owp[i]+=(wp[j]-1.0)/(s[j]-1.0);
					sum+=1.0;
				}
			}
		}
		owp[i]/=sum;
	}

	for(i=0;i<n;i++){
		oowp[i]=0;
		sum=0;
		for(j=0;j<n;j++)
		if(a[i][j]!='.'){
			oowp[i]+=owp[j];
			sum+=1.0;
		}
		oowp[i]/=sum;
	}


	for(i=0;i<n;i++){
		printf("\n%.9lf",0.25*(wp[i]/s[i])+0.5*owp[i]+0.25*oowp[i]);
	}





	return  0;
}
int main(){
	int t;

	scanf("%d\n",&t);
	for(int I=1;I<=t;I++){
		printf("Case #%d: ",I);
		solve();
		putchar('\n');
	}
	return 0;
}
