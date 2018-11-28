#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
#include<set>
#include<fstream>
#include<queue>
#include<fstream>
#include<map>

using namespace std;


int main()
{
	//ifstream cin("A-small-attempt0.in");
	//ofstream cout("A-small.out");
	ifstream cin("A-large.in");
	ofstream cout("A-large.out");


	long long test;
	cin>>test;

	for(int j=0;j<test;j++)
	{
		char arr[100][100];
		long long n;
		long double wp[100],owp[100],oowp[100];
		long long wins[100],loss[100];
		cin>>n;
		for(long i=0;i<n;i++)
		{
			char c;
			double w=0,l=0;
			for(long q=0;q<n;q++)
			{
				cin>>c;
				arr[i][q]=c;
				if(c=='.')
					continue;
				if(c=='1')
					w++;
				else if(c=='0')
					l++;
			}
			wp[i]=(w/(w+l));
			wins[i]=w;
			loss[i]=l;
		
		}
		
		for(long i=0;i<n;i++)
		{
			owp[i]=0;
			long t=0;
			for(long q=0;q<n;q++)
			{
				if(arr[i][q]=='.')
					continue;
				else
				{
					if(arr[q][i]=='1')
					{
						wins[q]--;
						if((wins[q]+loss[q])!=0)
							owp[i]+=(wins[q]/(double)(wins[q]+loss[q]));
						wins[q]++;
					}
					else
					{
						loss[q]--;
						if((wins[q]+loss[q])!=0)
							owp[i]+=(wins[q]/(double)(wins[q]+loss[q]));
						loss[q]++;
					}
					t++;
				}
			}

			owp[i]/=t;
		}


		for(long i=0;i<n;i++)
		{
			oowp[i]=0;
			long t=0;
			for(int q=0;q<n;q++)
			{
				if(arr[i][q]=='.')
					continue;
				else 
				{
					oowp[i]+=owp[q];
					t++;
				}
			}
			oowp[i]/=t;
		}
		long double rpi[100];
		for(long i=0;i<n;i++)
		{
			rpi[i]=(0.25*wp[i])+(0.5*owp[i])+(0.25*oowp[i]);
		}
		cout<<"Case #"<<j+1<<":\n";
		for(long i=0;i<n;i++)
		{
			cout<<rpi[i]<<endl;
		}
	}

	//system("pause");
	return 0;
}