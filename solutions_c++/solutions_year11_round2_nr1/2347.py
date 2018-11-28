#include<iostream>

using namespace std;

int main(void)
{
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		int n;
		cin>>n;
		char mat[n][n];
		for(int j=0;j<n;j++)
		{
			for(int k=0;k<n;k++)
			{
				cin>>mat[j][k];			
			}	
		}
		float wp[n],owp[n],oowp[n],rpi[n];
		memset(wp,0,sizeof(wp));
		memset(owp,0,sizeof(owp));
		memset(oowp,0,sizeof(oowp));
		memset(rpi,0,sizeof(rpi));
		
		//for(int b=0;b<n;b++)
			//	cout<<rpi[b]<<endl;	
				
		//cout<<"before";
		for(int j=0;j<n;j++)
		{
			int count_1=0;
			int count_0=0;
			for(int k=0;k<n;k++)
			{
				if(mat[j][k]=='1')
					count_1++;
				
				else if(mat[j][k]=='0')
					count_0++;
			}
			wp[j]=(float)count_1/(float)(count_1+count_0);
			int z=0;
			float wpn[n];
			memset(wpn,0,sizeof(wpn));
			for(int k=0;k<n;k++)
			{
				int cnt_1=0;
				int cnt_0=0;
				if(mat[j][k]!='.')
				{
					for(int l=0;l<n;l++)
					{
						if(l!=j)
						{
							if(mat[k][l]=='1')
								cnt_1++;
				
							else if(mat[k][l]=='0')
								cnt_0++;
						}
					}
					wpn[z]=(float)cnt_1/(float)(cnt_1+cnt_0);
					z++;
				//	cout<<endl;
					//cout<<cnt_1<<"\t"<<cnt_0<<"\t"<<wpn[z]<<"\t";
				}				
			}
		//	cout<<endl<<"z"<<z<<endl;
			for(int p=0;p<z;p++)
				owp[j]+=wpn[p];
			
			owp[j]=owp[j]/(float)z;
			//cout<<endl<<"owp"<<owp[j]<<"z"<<z<<endl;
		}	
		for(int j=0;j<n;j++)
		{	
			int h=0;
			for(int m=0;m<n;m++)
			{	
				if(mat[j][m]!='.')
				{	
					oowp[j]+=owp[m];
					h++;
				}
			}
			oowp[j]=oowp[j]/h;
		//	cout<<endl<<"h"<<h<<endl;
			
			rpi[j]=0.25*wp[j]+0.50*owp[j]+0.25*oowp[j];
			//cout<<wp[j]<<"\t"<<owp[j]<<"\t"<<oowp[j]<<endl;
		//	cout<<rpi[j]<<endl;
		}
			
		cout<<"Case #"<<i+1<<":"<<endl;
			for(int b=0;b<n;b++)
				cout<<rpi[b]<<endl;	
	}
	return 0;
}
