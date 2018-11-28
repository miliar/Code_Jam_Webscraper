#include<iostream>
#include<vector>
using namespace std;
int main()
{
	int kases;
	scanf("%d",&kases);
	for(int i=1;i<=kases;i++)
	{
		printf("Case #%d:\n",i);
		int H,W;
		scanf("%d %d",&H,&W);
		int inp[H][W];
		char out[H][W];
		for(int j=0;j<H;j++)
			for(int k=0;k<W;k++)
			{
				scanf("%d",&inp[j][k]);
				out[j][k]='-';
			}
		char p='a';
		int X_diff[4]={-1,0,0,+1};
		int Y_diff[4]={0,-1,+1,0};
		for(int j=0;j<H;j++)
			for(int k=0;k<W;k++)
			{
				if(out[j][k]=='-')
				{
					vector< pair<int,int> > V;
					int x=j,y=k;
					bool flag=true;
					while(flag)
					{
						V.push_back(make_pair(x,y));
						out[x][y]=p;
						int xnew=-1,ynew=-1;
						int flow=inp[x][y];
						for(int s=0;s<4;s++)
							if(x+X_diff[s]>=0 && x+X_diff[s]<H && y+Y_diff[s]>=0 && y+Y_diff[s]<W && inp[x+X_diff[s]][y+Y_diff[s]]<flow)
							{
								flow=inp[x+X_diff[s]][y+Y_diff[s]];
								xnew=x+X_diff[s];
								ynew=y+Y_diff[s];
							}
						if(xnew==-1&&ynew==-1)
						{
							flag=false;
							p=p+1;
						}
						else if(out[xnew][ynew]!='-')
						{
							for(int s=0;s<V.size();s++)
								out[V[s].first][V[s].second]=out[xnew][ynew];
							flag=false;
						}
						else 
						{
							x=xnew;
							y=ynew;
						}
					}
				}
			}
		for(int j=0;j<H;j++)
		{
			for(int k=0;k<W;k++)
				cout<<out[j][k]<<" ";
			putchar(10);
		}
	}
}
