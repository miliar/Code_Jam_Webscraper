#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>

#include<cmath>
#include<iostream>
#include<fstream>

#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>
#include<iterator>
using namespace std;

#ifdef ONLINE_JUDGE
#define i64 long long
#else
#define i64 __int64
#endif
#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b) ((a)<(b)?(a):(b))
#define pi acos(-1.0)
#define inf ((i64)1<<30)
#define CLR(a) memset(a,0,sizeof(a))
#define SET(a) memset(a,-1,sizeof(a))
#define pb push_back
#define eps 1e-11

char mat[60][60];
int n,k,c[100];

void rot()
{
	char temp[60][60];
	int i,j;
	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++)
		{
			temp[j][n-i-1]=mat[i][j];
		}
	}
	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++)
		{
			mat[i][j]=temp[i][j];
		}
	}
}

void fall()
{
	int i,j,p;
	for(j=0;j<n;j++)
	{
		for(i=n-1;i>=0;i--)
		{
			if(mat[i][j]=='.')
			{
				for(p=i-1;p>=0;p--)
				{
					if(mat[p][j]!='.')
					{
						break;
					}
				}
				if(p==-1)
				{
					break;
				}
				swap(mat[i][j],mat[p][j]);
			}
		}
	}
}

int row(char color,int x,int y)
{
	int i;
	if(y+k-1>n-1)
		return 0;
	for(i=0;i<k;i++)
	{
		if(mat[x][y+i]!=color)
			return 0;
	}
	return 1;
}
int col(char color,int x,int y)
{
	int i;
	if(x+k-1>n-1)
		return 0;
	for(i=0;i<k;i++)
	{
		if(mat[x+i][y]!=color)
			return 0;
	}
	return 1;
}

int ldia(char color,int x,int y)
{
	int i;
	if(x+k-1>n-1 || y-k+1<0)
		return 0;
	for(i=0;i<k;i++)
	{
		if(mat[x+i][y-i]!=color)
			return 0;
	}
	return 1;
}

int rdia(char color,int x,int y)
{
	int i;
	if(x+k-1>n-1 || y+k-1>n-1)
		return 0;
	for(i=0;i<k;i++)
	{
		if(mat[x+i][y+i]!=color)
			return 0;
	}
	return 1;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	//freopen("in.txt","r",stdin);
	int cs,t=1,i,j;
	cin>>cs;
	while(cs--)
	{
		CLR(mat);
		cin>>n>>k;
		for(i=0;i<n;i++)
		{
			scanf("%s",mat[i]);
		}
		CLR(c);
		rot();
		fall();
		for(i=0;i<n;i++)
		{
			for(j=0;j<n;j++)
			{
				if(row(mat[i][j],i,j))
					c[mat[i][j]]++;
				if(col(mat[i][j],i,j))
					c[mat[i][j]]++;
				if(ldia(mat[i][j],i,j))
					c[mat[i][j]]++;
				if(rdia(mat[i][j],i,j))
					c[mat[i][j]]++;
			}
		}
		cout<<"Case #"<<t++<<": ";
		if(c['R']>0&&c['B']>0)
		{
			cout<<"Both";
		}
		else if(c['R']>0)
		{
			cout<<"Red";
		}
		else if(c['B']>0)
		{
			cout<<"Blue";
		}
		else
		{
			cout<<"Neither";
		}
		cout<<endl;

	}
	return 0;
}


