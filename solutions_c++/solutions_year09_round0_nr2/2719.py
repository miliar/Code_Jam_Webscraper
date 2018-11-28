#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>

using namespace std;

int elev[100][100];
int basin[100][100];
int T,H,W;

void MakeSame(int x,int y)
{
	//cout<<"\ncalling makesame for x = "<<x<<" y = "<<y<<endl;
	for(int i=0;i<H;i++)
	{
		for(int j=0;j<W;j++)
		{
			if(basin[i][j]==y)
				basin[i][j]=x;
		}
	}
}

int main()
{
	
	cin>>T;
	
	
	for(int p=0;p<T;p++)
	{
		memset(basin,0,sizeof(basin));
		memset(elev,0,sizeof(elev));
		
		cin>>H>>W;
		for(int j=0;j<H;j++)
			for(int k=0;k<W;k++)
				cin>>elev[j][k];
		
		int symbol=1;
		
		for(int i=0;i<H;i++)
		{
			for(int j=0;j<W;j++)
			{
				int n,s,w,e,o;
				
				n = (i!=0) ? elev[i-1][j]:100001;
				s = (i!=H-1) ? elev[i+1][j]:100001;
				w = (j!=0) ? elev[i][j-1]:100001;
				e = (j!=W-1) ? elev[i][j+1]:100001;
				o = elev[i][j];
				int row,col;
				//North
				if(n<=s && n<=w && n<=e && n<o)
				{
					row = i-1;
					col = j;
				}
				else
				{
					//west
					if(w<=n && w<=e && w<=s && w<o)
					{
						row = i;
						col = j-1;
					}
					else
					{
						//East
						if(e<=n && e<=w && e<=s && e<o)
						{
							row = i;
							col = j+1;
						}
						else
						{
							//South
							if(s<=n && s<=w && s<=e && s<o)
							{	
								row = i+1;
								col = j;
							}
							//Sink
							else
							{
								row=-1;
								col = -1;
							}
						}
					}
				}
				//printf("\ni,j = %d,%d, row,col = %d,%d\n n,e,w,s  = %d,%d,%d,%d ",i,j,row,col,n,e,w,s);
				if(row!=-1 && basin[row][col]!=0 && basin[i][j]!=0 && basin[i][j]!=basin[row][col])
				{
					MakeSame(basin[row][col],basin[i][j]);
				}
				else
				{
					if(row!=-1)
					{
						if(basin[row][col]==0 && basin[i][j]!=0)
						{	//cout<<"\nin r,c==0 & i,j!=0"<<" i = "<<i<<" j = "<<j<<endl;
							basin[row][col] = basin[i][j];
						}
						else
						{
							if(basin[row][col]!=0 && basin[i][j]==0)
							{
							//	cout<<"\nin r,c!=0 & i,j==0"<<" i = "<<i<<" j = "<<j<<endl;
								basin[i][j] = basin[row][col];
							}
							else
							{
								if(basin[row][col]==0 && basin[i][j]==0)
								{
							//		cout<<"\nin r,c==0 & i,j==0"<<" i = "<<i<<" j = "<<j<<endl;
									basin[i][j] = symbol;
									basin[row][col] = symbol++;
								}
							}
						}
					}
					else
					{
						if(basin[i][j]==0)
							basin[i][j]=symbol++;
					}
				}
			}
		}
		/*cout<<"\nsymbol = "<<symbol<<endl;
		for(int i=0;i<H;i++)
		{
			for(int j=0;j<W;j++)
				cout<<basin[i][j]<<" ";
			cout<<endl;
		}*/
		
		int alph = int('a');
		
		
		for(int i=0;i<H;i++)
		{
			for(int j=0;j<W;j++)
			{
				if(!(basin[i][j]>='a' && basin[i][j]<='z'))
				{
					MakeSame(alph,basin[i][j]);
					alph++;
				}
			}
		}
	
		cout<<"Case #"<<p+1<<":"<<endl;
		for(int i=0;i<H;i++)
		{
			for(int j=0;j<W;j++)
				cout<<char(basin[i][j])<<" ";
			cout<<endl;
		}
	}
	return 0;
}			
	
