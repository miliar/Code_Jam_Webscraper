#include <iostream>
#include <math.h>
#include <stdlib.h>
#include <string>
#include <iomanip>

using namespace std;

string s[110];
int n,i,j,t,k;
int a[110][110],kol[110];
long double wp[110][2],owp[110],oowp[110],pri;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>t; k=1;
	while(t--)
	{
		
		cin>>n;
		for(i=0;i<n;i++) cin>>s[i];
		for(i=0;i<n;i++) 
		{
			wp[i][0]=0; wp[i][1]=0;
			for(j=0;j<n;j++) if(s[i][j]=='1') {a[i][j]=1; wp[i][0]++; wp[i][1]++;} else if(s[i][j]=='0') {a[i][j]=0; wp[i][1]++;} else a[i][j]=-1;
		}

		for(i=0;i<n;i++) 
		{ 
			owp[i]=0; kol[i]=0;
			for(j=0;j<n;j++) if(a[i][j]==1) {owp[i]+=wp[j][0]/(wp[j][1]-1); kol[i]++;} else if(a[i][j]==0) {owp[i]+=(wp[j][0]-1)/(wp[j][1]-1); kol[i]++;}
			owp[i]/=kol[i];
		}

		for(i=0;i<n;i++) 
		{
			oowp[i]=0;
			for(j=0;j<n;j++) if(a[i][j]==1||a[i][j]==0) oowp[i]+=owp[j];
			oowp[i]/=kol[i];
		}
		cout<<"Case #"<<k<<":"<<endl;
		for(i=0;i<n;i++) {pri=0.25*(wp[i][0]/wp[i][1])+0.5*owp[i]+0.25*oowp[i]; cout<<setprecision(10)<<pri<<endl;}
			k++;
		memset(a, 0, sizeof(int)*n);
	}


	fclose(stdin); fclose(stdout);
}