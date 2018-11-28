#pragma warning(disable:4786)
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<functional>
#include<string>
#include<cstring>
#include<cstdlib>
#include<queue>
#include<utility>
#include<fstream>
#include<sstream>
#include<cmath>
#include<stack>
#include<cstdio>
#include <iomanip>


using namespace std;

#define MEM(a,b) memset(a,(b),sizeof(a))
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b)  ((a) < (b) ? (a) : (b))
#define istr(S) istringstream sin(S)
#define MP make_pair
#define pb push_back
#define inf 1000000000

typedef pair<int,int> pi;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef vector<pi> vpi;

#define inf 1000000000

//typedef long long LL;
typedef __int64 LL;


int grid[105][105],temp[105][105];

int main()
{
	int i,j,k,l,tests,cs=0,n;
	

	//freopen("D:\\gcj\\C-small.in","r",stdin);
	freopen("D:\\gcj\\C-small.out","w",stdout);

	scanf("%d",&tests);
	while(tests--)
	{
		scanf("%d",&n);
		MEM(grid,0);

		int minr,maxc,minc,maxr;

		minr=minc=inf;
		maxr=maxc=-inf;

		for(i=0;i<n;i++)
		{
			int r1,c2,r2,c1;
			scanf("%d%d%d%d",&r1,&c1,&r2,&c2);

			minc=MIN(minc,c1);
			minr=MIN(minr,r1);

			maxr=MAX(maxr,r2);
			maxc=MAX(maxc,c2);


			for(j=r1;j<=r2;j++)
				for(k=c1;k<=c2;k++)
					grid[j][k]=1;
		}


		int ans=0;

		while(1)
		{

			int ok=0;

			
			for(i=minr;i<=maxr;i++)
				for(j=minc;j<=maxc;j++)
				{
					temp[i][j]=grid[i][j];
					if(grid[i][j] && 
						!(i-1>=0 && grid[i-1][j]) && !(j-1>=0 && grid[i][j-1]) ) temp[i][j]=0;

					if(!grid[i][j] && 
						(i-1>=0 && grid[i-1][j]) && (j-1>=0 && grid[i][j-1]) )   temp[i][j]=1;

					if(grid[i][j]) ok=1;
				}

			if(ok==0) break;
			ans++;
			for(i=minr;i<=maxr;i++)
				for(j=minc;j<=maxc;j++)
					grid[i][j]=temp[i][j];
		

		}

		printf("Case #%d: %d\n",++cs,ans);
	}

	return 0;
} 


