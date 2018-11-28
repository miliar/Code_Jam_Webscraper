#include<iostream>
#include<math.h>
#include<stdlib.h>
#include<string.h>

using namespace std;

int main()
{
	int T,N,i,j,k,wins,games,count;
	char table[101][101];
	float wp[100],owp[100],oowp[100],rpi[100];
	cin>>T;
	for(int t=0;t<T;t++)
	{
		cin>>N;
		for(i=0;i<N;i++)
			cin>>table[i];
		cout<<"Case #"<<t+1<<":"<<endl;
		for(i=0;i<N;i++)
		{
			wp[i]=0;
			wins=0;games=0;
			for(j=0;j<N;j++)
			{
				if(table[i][j]!='.')
					games++;
				if(table[i][j]=='1')
					wins++;
			}
			wp[i]=(float)wins/games;
		}
		for(i=0;i<N;i++)
		{
			owp[i]=0;count=0;
			for(j=0;j<N;j++)
			{
				games=0;wins=0;
				if(j!=i && table[i][j]!='.')
				{
					for(k=0;k<N;k++)
					{
						if(k!=i)
						{	
							if(table[j][k]!='.')
								games++;
							if(table[j][k]=='1')
								wins++;
						}
					}
					count++;
					owp[i]+=(float)wins/games;
				}
			}
			owp[i]/=count;
		}
		for(i=0;i<N;i++)
		{
			count=0;
			oowp[i]=0;
			for(j=0;j<N;j++)
			{
				if(table[i][j]!='.')
				{
					count++;
					oowp[i]+=owp[j];
				}
			}
			oowp[i]/=count;
		}
		for(i=0;i<N;i++)
		{
			rpi[i]=(0.25*wp[i])+(0.5*owp[i])+(0.25*oowp[i]);
			cout<<rpi[i]<<endl;
		}
	}
	
	
	return 0;
}