#include <cstdio>
#include <string>
#include <iostream>
#include <map>
#include <algorithm>
#include <vector>
#include <cmath>
#include <queue>
#include <vector>
#include <ctime>
#include <iostream>
#include <sstream>
#define eps 1.0e-9
#define Lim 1000000
using namespace std;

int a[100][100],b[100][100];
int main()
{
	int test,TestN;
	int i,j,k,l;
	int N,M;
	int H,W,R,x,y;
	scanf("%d",&TestN);
	for (test=1;test<=TestN;test++)
	{
		memset(b,0,sizeof(b));
		memset(a,0,sizeof(a));
		scanf("%d %d %d",&H,&W,&R);
		for (i=0;i<R;i++)
		{
			scanf("%d %d",&x,&y);
			b[x-1][y-1]=1;
		}
		a[0][0]=1;
		for (i=0;i<H;i++)
		{	for (j=0;j<W;j++)
			
			if (!b[i][j])
			{
				if (i-2>=0&&j-1>=0) a[i][j]=(a[i][j]+a[i-2][j-1])%10007;
				if (i-1>=0&&j-2>=0) a[i][j]=(a[i][j]+a[i-1][j-2])%10007;
			//	printf("%d ", a[i][j]);
			}
		//	else printf("x ");
		//	printf("\n");
		}
		
//		if (notfound)
//			printf("Case #%d: IMPOSSIBLE\n",test);
//		else
		printf("Case #%d: %d\n",test,a[H-1][W-1]);
		//fprintf(stderr,"%d\n",test);
	}
  	return 0;
}
