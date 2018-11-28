#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#include <string.h>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <algorithm>
using namespace std;

const int inf = 1000*1000*1000;
#define CL(x,a) memset(x,a,sizeof(x));
#define ALL(v) (v).begin(),(v).end()
typedef long long LL;
int T,k;
int diagx,diagy,X,Y;
int len;
void nextDiag()
{
	if (diagy == 0)
		diagx++;
	else
		diagy--;
}
void getPoint()
{
	X=diagx+len; Y=diagy+len;
	if (X <0 || X >=k || Y <0 || Y >=k)
	{
		nextDiag();
		len = 0;
		X=diagx+len; Y=diagy+len;
	}
	len++;
}
vector< vector<int> > ar,mat;
void pushMat(int a, int b)
{
	for (int i=a;i<a+k;i++)
	{
		for (int j=b;j<b+k;j++)
		{
			mat[i][j] = ar[i-a][j-b];
		}
	}
}

LL Count()
{
	LL res = 0;
	for (int i=0;i<mat.size();i++)
	{
		for (int j=0;j<mat.size();j++)
		{
			if (mat[i][j] != -1)
				continue;
			int nx = mat.size()-j-1; int ny = mat.size()-i-1;
			int t = -1;
			t = max(t,mat[nx][ny]);
			t = max(t,mat[ny][nx]);
			t = max(t,mat[j][i]);
			if (t == -1)
			{
				mat[nx][ny] = mat[i][j]=0;
			}
			else
			{
				mat[i][j] = t;
				res += t;
			}
		}
	}
	return res;
}
bool check()
{
	LL res = 0;
	for (int i=0;i<mat.size();i++)
	{
		for (int j=0;j<mat.size();j++)
		{
			int nx = mat.size()-j-1; int ny = mat.size()-i-1;
			if (mat[nx][ny] != mat[i][j] || mat[i][j] != mat[j][i] || mat[nx][ny] != mat[ny][nx])
				return 0;
		}
	}
	return 1;
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&T);
	for (int i=0;i<T;i++)
	{
		LL res = inf;
		scanf("%d",&k);
		ar.clear();
		ar.resize(k,vector<int>(k));
		diagx=0;diagy=k-1; len =0;
		for (int j=0;j<k*k;j++)
		{
			getPoint();
			scanf("%d",&ar[X][Y]);
		}
		bool ok=1;
		for (int sz=k;sz<=4*k+5 && ok;sz++)
		{
			for (int j=0;j<=sz-k && ok;j++)
			{
				for (int z=0;z<=sz-k && ok;z++)
				{
					mat.clear();
					mat.resize(sz,vector<int>(sz,-1));
					pushMat(j,z);
					LL t = Count();
					if (check())
					{
						res=sz*sz-k*k;
						ok=0;
					}
				}
			}
		}
		printf("Case #%d: %lld\n",i+1,res);
	}
	return 0;
}