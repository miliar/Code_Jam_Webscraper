#include <iostream>
using namespace std;
int m[105][105];
char c[105][105];
int h,w;
int dr[]={-1,0,0,1};
int dc[]={0,-1,1,0};
bool rec(int row,int col,char sm)
{
	c[row][col]=sm;
	int k,row0,col0,k0,best=1000000000;
	bool change=false;
	bool sink=true;
	for(k=0;k<4;k++)
	{
		row0=row+dr[k];
		col0=col+dc[k];
		if(row0<0 || col0<0 || row0>=h || col0>=w) continue;
		if(m[row0][col0]<m[row][col])
		{
			sink=false;
			if(m[row0][col0]<best)
			{
				k0=k;
				best=m[row0][col0];
			}
		}
	}
	if(sink)
	{
		c[row][col]=sm;
		return true;
	}
	row0=row+dr[k0];
	col0=col+dc[k0];
	if(!c[row0][col0])
	{
		 change=rec(row0,col0,sm);
	}
	c[row][col]=c[row0][col0];
	return change;
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tt,ii,i,j;
	cin>>tt;
	for(ii=1;ii<=tt;ii++)
	{
		cin>>h>>w;
		for(i=0;i<h;i++)
		{
			for(j=0;j<w;j++) cin>>m[i][j];
		}
		char cur='a';
		memset(c,0,sizeof(c));
		for(i=0;i<h;i++)
		{
			for(j=0;j<w;j++)
			{
				if(!c[i][j])
				{
					if(rec(i,j,cur)) cur++;
				}
			}
		}
		cout<<"Case #"<<ii<<":\n";
		for(i=0;i<h;i++)
		{
			for(j=0;j<w;j++)
			{
				cout<<c[i][j];
				if(j<w-1) cout<<' ';
			}
			cout<<endl;
		}
	}
	
	return 0;
}

