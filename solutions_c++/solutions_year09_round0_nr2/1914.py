//#include "stdafx.h"
#include <fstream>

std::ifstream in ("input");
std::ofstream out("output");
const int mH=100;
const int mW=100;
char c;
int mas[mH+2][mW+2];
int cmas[mH+2][mW+2];
char ch[mH+2][mW+2];
int T,H,W;

void solve(int i,int j)
{
	ch[i][j]=c;
	if(cmas[i][j]==0)
	{
		if(cmas[i+1][j]==1 && ch[i+1][j]=='_')solve(i+1,j);
		if(cmas[i][j+1]==2 && ch[i][j+1]=='_')solve(i,j+1);
		if(cmas[i][j-1]==3 && ch[i][j-1]=='_')solve(i,j-1);
		if(cmas[i-1][j]==4 && ch[i-1][j]=='_')solve(i-1,j);
	}else
	{
		if(cmas[i][j]==1 && ch[i-1][j]=='_' || cmas[i-1][j]==4 && ch[i-1][j]=='_') solve(i-1,j);
		if(cmas[i][j]==2 && ch[i][j-1]=='_' || cmas[i][j-1]==3 && ch[i][j-1]=='_') solve(i,j-1);
		if(cmas[i][j]==3 && ch[i][j+1]=='_' || cmas[i][j+1]==2 && ch[i][j+1]=='_') solve(i,j+1);
		if(cmas[i][j]==4 && ch[i+1][j]=='_' || cmas[i+1][j]==1 && ch[i+1][j]=='_') solve(i+1,j);
	}
}
int main()
{
	int i,j,k;
	in>>T;
	for(k=0;k<T;k++)
	{	
		in>>H>>W;
		for(i=1;i<=H;i++)
			for(j=1;j<=W;j++)
			{
				in>>mas[i][j];
				ch[i][j]='_';
			}
		for(i=0;i<=W+1;i++)
		{
			mas[0][i]=INT_MAX;
			mas[H+1][i]=INT_MAX;
			ch[0][i]='_';
			ch[0][W+1]='_';
		}
		for(i=0;i<=H+1;i++)
		{
			mas[i][0]=INT_MAX;
			mas[i][W+1]=INT_MAX;
			ch[i][0]='_';
			ch[H+1][0]='_';
		}
		//while(true)
		{
			for(i=1;i<=H;i++)
				for(j=1;j<=W;j++)
				{
					if(mas[i-1][j]<mas[i][j] && mas[i-1][j]<=mas[i][j-1] && mas[i-1][j]<=mas[i][j+1] && mas[i-1][j]<=mas[i+1][j])
						cmas[i][j]=1;else
						if(mas[i][j-1]<mas[i][j] && mas[i][j-1]<=mas[i][j+1] && mas[i][j-1]<=mas[i+1][j])
							cmas[i][j]=2;else
							if(mas[i][j+1]<mas[i][j] && mas[i][j+1]<=mas[i+1][j])
								cmas[i][j]=3;else 
								if(mas[i+1][j]<mas[i][j])cmas[i][j]=4;else
									cmas[i][j]=0;
				}
		}
		c='a'; 
		ch[1][1]=c;
		solve(1,1);
		c++;
		for(i=1;i<=H;i++)
			for(j=1;j<=W;j++)
				if(ch[i][j]=='_') 
				{
					solve(i,j);
					c++;
				}
		out<<"Case #"<<k+1<<":"<<'\n';
		for(i=1;i<=H;i++)
		{
			for(j=1;j<=W;j++)
			{
				out<<ch[i][j];
				if(j<W)out<<' ';
			}
			out<<'\n';
		}
	}
	in.close();
	out.close();
	return 0;
}

