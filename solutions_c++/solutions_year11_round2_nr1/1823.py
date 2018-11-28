#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
	long long int ttt;
	cin>>ttt;
	for(long long int tt=1;tt<=ttt;tt++)
	{

		cout<<"Case #"<<tt<<":\n";
		char d[1000][1000];
		int n;
		cin>>n;
		for(int i=0;i<n;i++)
			cin>>d[i];

		long double win[1000];
		long double ow[1000];
		long double oow[1000];
		int play[1000],w[1000];
		for(int i=0;i<n;i++)
		{
			play[i]=n;
			w[i]=0;
			for(int j=0;j<n;j++)
			{
				if(d[i][j]=='.')
					play[i]--;
				else if(d[i][j]=='1')w[i]++;
			}
			if(w[i]==0)win[i]=0;
			else win[i]=1.0*w[i]/play[i];
		}
		for(int i=0;i<n;i++)
		{
			long double avg=0;
			int count=0;
			for(int j=0;j<n;j++)
			{
				if(d[i][j]!='.')
				{

					count++;
					if(d[i][j]=='1'){
						avg+=(1.0*(w[j])/(play[j]-1)); 

					}
					else if(d[i][j]=='0'){
						avg+=(1.0*(w[j]-1)/(play[j]-1));

					}

				}
			}
			 ow[i]=avg/count;
		}
		for(int i=0;i<n;i++)
		{
			long double avg=0;
int count=0;
			for(int j=0;j<n;j++)
			{
				if(i!=j && d[i][j]!='.'){
					avg+=ow[j];
count++;			
}}
			oow[i]=avg/count;
		}

		for(int i=0;i<n;i++)
	//		cout<<oow[i]<<endl;			
		printf("%.12Lf\n",0.25*win[i]+0.5*ow[i]+0.25*oow[i]);

	}


}
