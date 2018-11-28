#include <iostream>
#include <fstream>
#include <string>

using namespace std;

ifstream fin("atc");
#define cin fin

void stuff()
{
	int N,i,j;
	char c[101][101];
	double WP[101],OWP[101],OOWP[101],temp[101][101];
	double SOWP=0;//sum OWP
	cin>>N;
	for(i=0;i<N;i++)
		for(j=0;j<N;j++)
			cin>>c[i][j];
	//WP
	for(i=0;i<N;i++)
	{
		int win=0,lose=0;
		for(j=0;j<N;j++)
		{
			if(c[i][j]=='1')
				win++;
			else if(c[i][j]=='0')
				lose++;
		}
		WP[i]=double(win)/(win+lose);
		double a,b;
		if(win+lose-1>0)
		{
			a=double(win-1)/(win-1+lose);
			b=double(win)/(win+lose-1);
		}
		else
		{a=0;b=0;}
		for(j=0;j<N;j++)
		{
			if(c[i][j]=='1')
				temp[i][j]=a;
			else if(c[i][j]=='0')
				temp[i][j]=b;
			else
				temp[i][j]=WP[i];
		}
	}
	for(i=0;i<N;i++)
	{
		double t=0,n=0;
		for(j=0;j<N;j++)
		{
			if(c[i][j]!='.')
			{
				if(j==i)
					continue;
				t+=temp[j][i];
				n++;
			}
		}
		OWP[i]=t/double(n);
		SOWP+=OWP[i];
	}
	for(i=0;i<N;i++)
	{
		SOWP=0;
		double n=0;
		for(j=0;j<N;j++)
		{
			if(c[i][j]!='.')
			{
				if(j==i)
					continue;
				SOWP+=OWP[j];
				n++;
			}
		}
		OOWP[i]=SOWP/n;
	}	
	for(i=0;i<N;i++)
		//cout<<WP[i]<<" " <<OWP[i]<<" " <<OOWP[i]<<endl;
		cout<<0.25*WP[i]+0.5*OWP[i]+0.25*OOWP[i]<<endl;
	
}

int main(void)
{
	int T;
	cin>>T;
	for(int i=0;i<T;i++)
	{
		cout<<"Case #"<<i+1<<": "<<endl;;
		stuff();
	}
	
}
