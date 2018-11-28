#include<stdio.h>
#include<stdlib.h>
#include<memory.h>
#include<iostream>
#include<memory.h>
#include<memory>
using namespace std;
char m[110][110];
double wp[110];
double owp[110];
double oowp[110];
double tmp[110];
int main()
{
	freopen("A-large.in","r",stdin); 
	freopen("A.txt","w",stdout);
	int cas=0;
	scanf("%d",&cas);
	for(int ca=1;ca<=cas;ca++)
	{
		memset(m,sizeof(m),0);		
		int n;
		scanf("%d",&n);
		for(int i=0;i<n;i++)
			scanf("%s",m[i]);
	
		for(int i=0;i<n;i++)
		{
			wp[i]=0.0;
			int cnt=0;
			for(int j=0;j<n;j++)
			{
				if(m[i][j]=='1') wp[i]++;
				if(m[i][j]=='.') cnt++;
			}
			cnt=n-cnt;
			wp[i]/=cnt;
		}
		
		for(int k=0;k<n;k++)
		{
			owp[k]=0.0;
		    for(int i=0;i<n;i++)
			{
				tmp[i]=0.0;
				int cnt=0;
				for(int j=0;j<n;j++)
				{
					if(m[i][j]=='1' && j!=k) tmp[i]++;
					if(m[i][j]!='.' && j!=k) cnt++;
				}
				tmp[i]/=cnt;
			}
			int nt=0;
			for(int j=0;j<n;j++)
			{
				if(m[k][j]!='.') {owp[k]+=tmp[j];nt++;}
			}
			owp[k]/=nt;
		}
		
		for(int i=0;i<n;i++)
		{
			oowp[i]=0.0;
			int cnt=0;
			for(int j=0;j<n;j++)
			{
				if(m[i][j]!='.') 
				{
				 oowp[i]+=owp[j];
				 cnt++;
				}
			}
			oowp[i]/=cnt;
		}

		/*
		for(int i=0;i<n;i++) printf("%.12lf\n",wp[i]);
		cout<<endl;
		for(int i=0;i<n;i++) printf("%.12lf\n",owp[i]);
		cout<<endl;		
		for(int i=0;i<n;i++) printf("%.12lf\n",oowp[i]);
		cout<<endl;
		*/
		
		cout<<"Case #"<<ca<<":"<<endl;
		for(int i=0;i<n;i++)
			printf("%.12lf\n",0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
	}
	return 0;
}

