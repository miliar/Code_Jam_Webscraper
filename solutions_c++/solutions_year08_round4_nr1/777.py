#include<string>
#include<vector>
#include<iostream>
#include<math.h>
#include<fstream>
#include<sstream>

using namespace std;

/*void main()
{
	ifstream ff("datos.txt");
	ofstream rr("res.txt");
	int nc,cas,n,m,a,i,j;
	ff>>cas;
	for(nc=0;nc<cas;nc++)
	{
		ff>>n>>m>>a;
		for(i=0;i<=m;i++)for(j=0;j<=n;j++) if(i*j==a) {rr<<"Case #"<<nc+1<<": "<<"0 0 0 "<<i<<" "<<j<<" 0"<<endl;goto listo;}
		rr<<"Case #"<<nc+1<<": IMPOSSIBLE"<<endl;
listo:
		;
	}
}*/

int min(int a,int b) {return a<b?a:b;}
int max(int a,int b) {return a>b?a:b;}

void main()
{
	ifstream ff("datos.txt");
	ofstream rr("res.txt");
	int nc,cas,m,i,j,v,g,c;
	int tree[10000][4];
	int pd[10000][2];
	ff>>cas;
	for(nc=0;nc<cas;nc++)
	{
		ff>>m>>v;
		for(i=0;i<1000;i++)for(j=0;j<4;j++) tree[i][j]=0;
		for(i=0;i<(m-1)/2;i++) {ff>>g>>c;tree[i][0]=g;tree[i][1]=c;}
		for(i=0;i<(m+1)/2;i++) {ff>>g;tree[i+(m-1)/2][3]=g;}
		for(i=(m-1)/2-1;i>=0;i--) tree[i][3]=tree[i][0]==1?tree[2*i+2][3] && tree[2*i+1][3]:tree[2*i+2][3] || tree[2*i+1][3];
		for(i=m-1;i>=(m-1)/2;i--) {pd[i][tree[i][3]]=0;pd[i][1-tree[i][3]]=1000000;}
		for(i=(m-1)/2-1;i>=0;i--)
		{
			if(tree[i][1]==0 && tree[i][0]==0)
			{
				pd[i][0]=pd[2*i+2][0]+pd[2*i+1][0];
				pd[i][1]=min(pd[2*i+2][1],pd[2*i+1][1]);
			}
			if(tree[i][1]==0 && tree[i][0]==1)
			{
				pd[i][0]=min(pd[2*i+2][0],pd[2*i+1][0]);
				pd[i][1]=pd[2*i+2][1]+pd[2*i+1][1];
			}
			if(tree[i][1]==1 && tree[i][0]==0)
			{
				pd[i][0]=min(pd[2*i+2][0]+pd[2*i+1][0],min(pd[2*i+2][0],pd[2*i+1][0])+1);
				pd[i][1]=min(min(pd[2*i+2][1],pd[2*i+1][1]),pd[2*i+2][1]+pd[2*i+1][1]+1);
			}
			if(tree[i][1]==1 && tree[i][0]==1)
			{
				pd[i][0]=min(min(pd[2*i+2][0],pd[2*i+1][0]),pd[2*i+2][0]+pd[2*i+1][0]+1);
				pd[i][1]=min(pd[2*i+2][1]+pd[2*i+1][1],min(pd[2*i+2][1],pd[2*i+1][1])+1);
			}
		}
		if(pd[0][v]>=1000000) rr<<"Case #"<<nc+1<<": IMPOSSIBLE"<<endl; else rr<<"Case #"<<nc+1<<": "<<pd[0][v]<<endl;
	}
}