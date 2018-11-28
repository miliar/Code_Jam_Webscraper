#include<fstream>
#define dmax 110
using namespace std;
ifstream in("watersheds.in");
ofstream out("watersheds.out");
int n,m,t,mat[dmax][dmax];
char mt[dmax][dmax],crt='a'-1;
const int dx[]={99,-1,0,0,1};
const int dy[]={99,0,-1,1,0};
int bune(int i,int j)
{	return ((i>0)&&(i<=n)&&(j>0)&&(j<=m));
}
void fb(int i,int j,char val1,char val2)
{	int ii,jj,k;
	for(k=1;k<=4;k++)
	{	ii=i+dx[k];
		jj=j+dy[k];
		if(bune(ii,jj))
			if(mt[ii][jj]==val1)
			{	mt[ii][jj]=val2;
				fb(ii,jj,val1,val2);
			}
	}		
}
void fill(int i,int j)
{	int ii,jj,k,mn=-1,bun;
	for(k=1;k<=4;k++)
	{	ii=i+dx[k];
		jj=j+dy[k];
		if(bune(ii,jj))
		{	if(mat[ii][jj]<mat[i][j])
			{	if((mat[ii][jj]<mn)||(mn==-1))
				{	mn=mat[ii][jj];
					bun=k;
				}	
			}
		}	
	}
	if(mn!=-1)
	{	ii=i+dx[bun];
		jj=j+dy[bun];
		if(mt[ii][jj]!='0')
		{	
			fb(i,j,mt[i][j],mt[ii][jj]);
			crt--;
			mt[i][j]=mt[ii][jj];
		}	
		else 
		{	mt[ii][jj]=crt;
			fill(ii,jj);
		}
	}	
}
void get()
{	int i,j;
	for(i=1;i<=n;i++)
		for(j=1;j<=m;j++)
			if(mt[i][j]=='0')
			{	crt++;
				mt[i][j]=crt;	
				fill(i,j);			
			}	
}
int main()
{	int i,j,k;
	in>>t;
	for(k=1;k<=t;k++)
	{	in>>n>>m;
		for(i=1;i<=n;i++)
			for(j=1;j<=m;j++)
				in>>mat[i][j];
		for(i=1;i<=n;i++)
			for(j=1;j<=m;j++)
				mt[i][j]='0';	
		get();
		out<<"Case #"<<k<<":"<<'\n';
		for(i=1;i<=n;i++)
		{	for(j=1;j<=m;j++)
				out<<mt[i][j]<<" ";
			out<<'\n';
		}
		for(i=1;i<=n;i++)
			for(j=1;j<=n;j++)
				mt[i][j]='0';
		crt='a'-1;	
	}
	in.close();
	out.close();
	return 0;
}	