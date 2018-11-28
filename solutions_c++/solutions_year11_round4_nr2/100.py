#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>
using namespace std;

#define FRsmall(x,y) freopen(#x"-small-attempt"#y".in","r",stdin);freopen(#x"-small-attempt"#y".out","w",stdout);
#define FRlarge(x) freopen(#x"-large.in","r",stdin);freopen(#x"-large.out","w",stdout);

typedef long long I;

int d[510][510];
I S[510][510];
I Sx[510][510];
I Sy[510][510];

int main()
{
	//freopen("B.in","r",stdin);
	//FRsmall(B,0)
	FRlarge(B)

	int T,TC=0;
	scanf("%d",&T);
	while(++TC<=T)
	{
		printf("Case #%d: ",TC);
		
		int R,C,D;
		scanf("%d %d %d",&R,&C,&D);
		int i,j,k;
		int t,tx,ty;
		for(i=1;i<=R;i++)for(j=1;j<=C;j++)scanf("%1d",&d[i][j]);
		for(j=0;j<=C;j++)S[0][j]=Sx[0][j]=Sy[0][j]=0;
		for(i=1;i<=R;i++)
		{
			t=tx=ty=0;
			for(j=1;j<=C;j++)
			{
				t+=d[i][j];
				tx+=d[i][j]*j;
				ty+=d[i][j]*i;
				S[i][j]=t+S[i-1][j];
				Sx[i][j]=tx+Sx[i-1][j];
				Sy[i][j]=ty+Sy[i-1][j];
			}
		}
		int f=0;
		for(k=min(R,C);k>=3;k--)
		{
			for(i=1;i<=R-k+1;i++)
			{
				for(j=1;j<=C-k+1;j++)
				{
					I s=S[i+k-1][j+k-1]-S[i-1][j+k-1]-S[i+k-1][j-1]+S[i-1][j-1];
					s-=d[i][j]+d[i+k-1][j]+d[i][j+k-1]+d[i+k-1][j+k-1];
					I sx=Sx[i+k-1][j+k-1]-Sx[i-1][j+k-1]-Sx[i+k-1][j-1]+Sx[i-1][j-1];
					I sy=Sy[i+k-1][j+k-1]-Sy[i-1][j+k-1]-Sy[i+k-1][j-1]+Sy[i-1][j-1];
					if((sx-(d[i][j]+d[i+k-1][j])*j-(d[i][j+k-1]+d[i+k-1][j+k-1])*(j+k-1))*2==(j+j+k-1)*s
					&& (sy-(d[i][j]+d[i][j+k-1])*i-(d[i+k-1][j]+d[i+k-1][j+k-1])*(i+k-1))*2==(i+i+k-1)*s)
					{
						printf("%d\n",k);
						f=1;
						break;
					}
				}
				if(f)break;
			}
			if(f)break;
		}
		if(!f)printf("IMPOSSIBLE\n");
	}
	return 0;
}
