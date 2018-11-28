#include <iostream>
#include <stdio.h>
#include <vector>
using namespace std;
string A[1000];
double WP[1000];
double WP2[1000][1000];
double OWP[1000];
double OOWP[1000];
int main (int argc, char * const argv[]) {
    freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	cin>>T;
	for(int c=1;c<=T;c++)
	{
		int n;
		cin>>n;
		for(int i=0;i<n;i++)cin>>A[i];
		for(int i=0;i<n;i++)
		{
			int cont=0;
			WP[i]=0;
			for(int j=0;j<n;j++){
				if(A[i][j]!='.')cont++;
				if(A[i][j]=='1')WP[i]++;
			}
			if(cont!=0)WP[i]/=(double)cont;
		}
		for(int k=0;k<n;k++)
		for(int i=0;i<n;i++)
		{
			int cont=0;
			WP2[i][k]=0;
			for(int j=0;j<n;j++){
				if(j==k)continue;
				if(A[i][j]!='.')cont++;
				if(A[i][j]=='1')WP2[i][k]++;
			}
			if(cont!=0)WP2[i][k]/=(double)cont;
		}
		for(int i=0;i<n;i++)
		{
			OWP[i]=0;
			int cont=0;
			for(int j=0;j<n;j++)
			{
				if(A[i][j]=='.')continue;
				cont++;
				OWP[i]+=WP2[j][i];
			}
			if(cont!=0)OWP[i]/=(double)cont;
		}
		for(int i=0;i<n;i++)
		{
			OOWP[i]=0;
			int cont=0;
			for(int j=0;j<n;j++)
			{
				if(A[i][j]=='.')continue;
				cont++;
				OOWP[i]+=OWP[j];
			}
			if(cont!=0)OOWP[i]/=(double)cont;
		}
		cout<<"Case #"<<c<<":"<<endl;
		
		for(int i=0;i<n;i++)
		{
			double res=0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i];
			printf("%.10lf\n",res);
		}
		
	}
    return 0;
}
