#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;


int h,w;
char cell[101][101],c;

int alt[101][101];
int dirx[5],diry[5];

char f (int x,int y)
{
	if(cell[x][y]!='-')
		return cell[x][y];
	int dir,mindir=4;
	for(dir=0;dir<4;dir++)
	{
		if(x+dirx[dir]<h && y+diry[dir]<w && x+dirx[dir]>=0 && y+diry[dir]>=0)
		{
		if(alt[x+dirx[dir]][y+diry[dir]]<alt[x+dirx[mindir]][y+diry[mindir]])
			mindir=dir;
		}
	}
	if(mindir==4)
	{
		cell[x][y]=c++;
		return cell[x][y];
	}
	return f (x+dirx[mindir],y+diry[mindir]);
}

int main ()
{
	freopen ("Watersheds.in","r",stdin);
	freopen ("Watersheds.out","w",stdout);
	
	int T,t;
	cin>>T;
	
	dirx[0]=-1;
	dirx[1]=0;
	dirx[2]=0;
	dirx[3]=1;
	dirx[4]=0;

	diry[0]=0;
	diry[1]=-1;
	diry[2]=1;
	diry[3]=0;
	diry[4]=0;
	
	int i,j;
	for(t=1;t<=T;t++)
	{
		cin>>h>>w;
		for(i=0;i<h;i++)
			for(j=0;j<w;j++)
				cin>>alt[i][j];
		
		c='a';
		for(i=0;i<h;i++)
			for(j=0;j<w;j++)
				cell[i][j]='-';
				
		cout<<"Case #"<<t<<":"<<endl;
		for(i=0;i<h;i++)
		{
			cout<<f (i,0);
			for(j=1;j<w;j++)
			{
				cout<<" "<<f (i,j);
			}
			cout<<endl;
		}		
	}
	return 0;
}
