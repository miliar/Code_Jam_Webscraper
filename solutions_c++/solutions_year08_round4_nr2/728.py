#include<stdio.h>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<memory>
#include<math.h>
#include<time.h>
#include<string.h>
#include<algorithm>

using namespace std;

typedef vector<int> vi; 
typedef vector<string> vs; 

#define min(i,j) ((i)<(j)?(i):(j))
#define max(i,j) ((i)>(j)?(i):(j))
#define abx(i) ((i)>0?(i):(-(i)))
#define eps 1e-9

#include<stdio.h>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<memory>
#include<math.h>
#include<time.h>
#include<string.h>
#include<algorithm>

using namespace std;

typedef vector<int> vi; 
typedef vector<string> vs; 

#define min(i,j) ((i)<(j)?(i):(j))
#define max(i,j) ((i)>(j)?(i):(j))
#define abx(i) ((i)>0?(i):(-(i)))
#define eps 1e-9

int n,m,a;
int ax1,ax2,ax3;
int ay1,ay2,ay3;

int main()
{
	int ncase,icase=1;
	int i,j,k,t;
	freopen("1.in","r",stdin);
	freopen("wqb.out","w",stdout);
	for(scanf("%d",&ncase);ncase--;)
	{
		scanf("%d%d%d",&n,&m,&a);
		printf("Case #%d: ",icase++);
	//	printf("%I64d  %I64d  %I64d\n",a,n,m);
		for(ax1=0;ax1<=n;ax1++)
			for(ax2=0;ax2<=n;ax2++)
				for(ay1=0;ay1<=m;ay1++)
					for(ay2=0;ay2<=m;ay2++)
					{
						//printf("%I64d  %I64d  %I64d  %I64d",ax1,ax2,ay1,ay2);
						if(ax1*ay2-ax2*ay1==a)
						{
							printf("0 0 %d %d %d %d\n",ax1,ay1,ax2,ay2);
							goto tt;
						}
					}
		printf("IMPOSSIBLE\n");
		tt:;
	}
	return 0;
}

