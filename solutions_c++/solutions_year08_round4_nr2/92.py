#include <cstdio>
#include <algorithm>
using namespace std;
int min3(int a,int b,int c) { return min(min(a,b),c); }
int max3(int a,int b,int c) { return max(max(a,b),c); }
int main()
{
	int T,N,M,A,t;
	scanf("%d",&T);
	for (t=1;t<=T;t++) 
	{
		scanf("%d %d %d",&N,&M,&A);
		int a,b,c,d,f=0;
		for (a=-N;a<=N;a++) for (b=-M;b<=M;b++) for (c=-N;c<=N;c++) 
		{
			if (f) continue;
			int T=A+b*c;
			if (a==0)
			{
				if (T==0) d=1;
				else d=0;
			}
			else d=T/a;
			if (a*d-b*c!=A) continue;
			int dx=max3(0,a,c)-min3(0,a,c);
			int dy=max3(0,b,d)-min3(0,b,d);
			if (dx<=N && dy<=M)
			{
				f=1;
				int px=-min3(0,a,c);
				int py=-min3(0,b,d);
				printf("Case #%d: %d %d %d %d %d %d\n",t,px,py,a+px,b+py,c+px,d+py);
			}
		}
		if (!f) printf("Case #%d: IMPOSSIBLE\n",t);
	}
}
