#include <iostream>
using namespace std;

int main()
{
	int t,i,j,n,w,k;
	int z[100];
	double wp[100],owp[100],oowp[100];
	char s[100][110];
	cin>>t;
	for(j=1;j<=t;j++)
	{
		cin>>n;
		for(i=0;i<n;i++)
		{
			cin>>s[i];
			w=z[i]=0;
			for(k=0;k<n;k++)
				if(s[i][k]=='0') z[i]++;
				else if(s[i][k]=='1') w++,z[i]++;
			wp[i]=double(w)/z[i];
		}
		for(i=0;i<n;i++)
		{
			owp[i]=0;
			for(k=0;k<n;k++)
				if(s[i][k]!='.')
				{
					owp[i]+=(wp[k]*z[k]-(s[k][i]=='1'))/(z[k]-1);
				}
			owp[i]/=z[i];
		}
		for(i=0;i<n;i++)
		{
			oowp[i]=0;
			for(k=0;k<n;k++)
				if(s[i][k]!='.')
				{
					oowp[i]+=owp[k];
				}
			oowp[i]/=z[i];
		}
		cout<<"Case #"<<j<<": "<<endl;
		for(i=0;i<n;i++)
			printf("%.12lf\n",0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
	}

}
