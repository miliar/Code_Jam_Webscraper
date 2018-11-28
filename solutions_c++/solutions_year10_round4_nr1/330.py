#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
#include <cstring>
#include <cctype>
#include <assert.h>

using namespace std;
typedef long long ll;

const double PI=acos(-1.0);
const double eps=1e-11;

#define dump(x) cerr<<#x<<" = "<<(x)<<endl;
#define foreach(c,itr) for (__typeof( (c).begin() ) itr=(c).begin();itr!=(c).end() ;itr++ )


int countbit(int n) {return (n==0)?0:1+countbit(n&(n-1));}
int lowbit(int n) {return n&(n^(n-1));}
string toString(ll v) { ostringstream sout;sout<<v;return sout.str();}
string toString(int v) { ostringstream sout;sout<<v;return sout.str();}
int Rand16(){return rand();}
int Rand32(){return rand()*rand();}
double DRand(){return (double)rand()/RAND_MAX;}
int RandRange(int f,int r){return f+(int)(DRand()*(r-f)+0.5);}

const int MAX = 500+50;

int da[MAX][MAX];
int smo[MAX][MAX],sz;

bool ok(int x1,int y1,int x2,int y2)
{
	if (da[x1][y1]==-1 || da[x2][y2]==-1)
		return true;
	return da[x1][y1]==da[x2][y2];
}

void Output(int a[MAX][MAX],int sz)
{
	int i,j,k;
	for (i=1;i<=sz;i++,putchar('\n'))
		for (j=0;j<sz+i;j++)
		{
			if (a[i][j]==-1) putchar(' ');
			else printf("%d",a[i][j]);
		}
		for (;i<2*sz;i++,putchar('\n'))
			for (j=0;j<3*sz-i;j++)
			{
				if (a[i][j]==-1) putchar(' ');
			else printf("%d",a[i][j]);
			}
}

bool test(int k)
{
	//Output(da,k);

	int i,j;
	int i1,j1;

	for (i=1;i<=k;i++)
		for (j=k-i+1;j<k+i;j+=2)
		{
			i1=2*k-i;
			j1=2*k-j;
			//printf("i=%d,j=%d,i1=%d,j1=%d\n",i,j,i1,j1);
			if (!ok(i,j,i1,j) || !ok(i,j,i,j1)) return false;
		}

	
	for (;i<2*k;i++)
		for (j=i-k+1;j<3*k-i;j+=2)
		{
			i1=2*k-i;
			j1=2*k-j;
			//printf("i=%d,j=%d,i1=%d,j1=%d\n",i,j,i1,j1);
			if (!ok(i,j,i1,j) || !ok(i,j,i,j1)) return false;
		}		
	return true;
}

bool isPos(int x,int y,int bsz)
{
	if (x<=bsz)
		return y>=bsz-x+1 && y<bsz+x;
	else
		return y>=x-bsz+1 && y<3*bsz-x;

}



bool can(int x,int y,int bsz)
{

	if (!(isPos(x+sz-1,y-sz+1,bsz) &&
		isPos(x+sz-1,y+sz-1,bsz) &&
		isPos(x+2*sz-2,y,bsz)))
		return false;

//	printf("test x=%d,y=%d,bsz=%d\n",x,y,bsz);

	memset(da,-1,sizeof(da));
	int i,j;
	int dx,dy;
	int nx,ny;

	dx=1;
	dy=sz;

	for (i=1;i<=sz;i++)
		for (j=sz-i+1;j<sz+i;j+=2)
		{
				nx=x+i-dx;
				ny=y+j-dy;
				//printf("nx=%d,ny=%d,i=%d,j=%d v=%d\n",nx,ny,i,j,smo[i][j]);
				da[nx][ny]=smo[i][j];
		}

	for (;i<2*sz;i++)
		for (j=i-sz+1;j<3*sz-i;j+=2)
		{
				nx=x+i-dx;
				ny=y+j-dy;
				//printf("nx=%d,ny=%d,i=%d,j=%d v=%d\n",nx,ny,i,j,smo[i][j]);
				da[nx][ny]=smo[i][j];
		}

//	Output(da,bsz);

	if (test(bsz))
		return true;
	return false;
}

int main()
{
	int t,cas;
	int i,j,k;

	freopen("A-small-attempt1.in","r",stdin);
	freopen("A-small-attempt1.out","w",stdout);

	scanf("%d",&t);
	cas=0;
	while (t--)
	{
		cas++;
		scanf("%d",&k);
		memset(smo,-1,sizeof(smo));

		sz=k;
		for (i=1;i<=k;i++)
			for (j=k-i+1;j<k+i;j+=2)
			{
				scanf("%d",&smo[i][j]);
			}
		for (;i<2*k;i++)
			for (j=i-k+1;j<3*k-i;j+=2)
				scanf("%d",&smo[i][j]);


		int ans=k;
		for (;;ans++)
		{
			bool found=false;
						
			for (i=1;i<=ans;i++)
				for (j=ans-i+1;j<ans+i;j+=2)
					if (can(i,j,ans))
					{
						found=true;
						goto end;
					}

			for (;i<2*ans;i++)
				for (j=i-ans+1;j<3*ans-i;j+=2)
					if (can(i,j,ans))
					{	
						found=true;
						goto end;
					}

			end:
				if (found) break;
		}
		
		ans=ans*ans-sz*sz;

		printf("Case #%d: ",cas);
		printf("%d\n",ans);
	}
	return 0;
}
