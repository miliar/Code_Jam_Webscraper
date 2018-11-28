#include<cstdio>
#include<iostream>
using namespace std;

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int Test;
	cin>>Test;
	for (int test=0;test<Test;test++){
		int n;
		cin>>n;
		char c[100][100];
		for (int i=0;i<n;i++)
			for (int j=0;j<n;j++)
				cin>>c[i][j];
		double wp[100];
		int tot[100];
		double win[100];
		for (int i=0;i<n;i++){
			wp[i]=win[i]=tot[i]=0;
			for (int j=0;j<n;j++)
				if (c[i][j]!='.'){
					tot[i]++;
					win[i]+=c[i][j]-'0';
				}
			wp[i]=win[i]/tot[i];
		}
		double owp[100];
		for (int i=0;i<n;i++){
			owp[i]=0;
			for (int j=0;j<n;j++)
				if (c[i][j]=='1')
					owp[i]+=win[j]/(tot[j]-1);
				else if (c[i][j]=='0')
					owp[i]+=(win[j]-1)/(tot[j]-1);
			owp[i]/=tot[i];
		}
		double oowp[100];
		for (int i=0;i<n;i++){
			oowp[i]=0;
			for (int j=0;j<n;j++)
				if (c[i][j]!='.')
					oowp[i]+=owp[j];
			oowp[i]/=tot[i];
		}
		printf("Case #%d:\n",test+1);
		for (int i=0;i<n;i++)
			printf("%0.8f\n",0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
	}
}