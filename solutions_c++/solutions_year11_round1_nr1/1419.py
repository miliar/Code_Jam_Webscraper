#include<stdio.h>
#include<math.h>
#include<algorithm>
#include<iostream>
#include<string.h>
#include<vector>
#include<stack>
#include<queue>
#define eps 1e-11
#define INF (2<<31)-1

using namespace std;

int max(int a, int b) {
	if(a>b) return a;
	return b;
}
int min(int a, int b){
	if(a<b) return a;
	return b;
}

int n, pd, pg, t, rr;
double a, b;
int A, B;



int main()
{
		freopen("aaa.in","r",stdin);
		freopen("out.txt","w",stdout);
	int i, ct=1;
	scanf("%d", &t);
	while(t--)
	{
		rr=0;
		scanf("%d %d %d", &n, &pd, &pg);
		if(pg==100 && pd<100)
			rr=0;
		else if(pg==0 && pd>0 )
			rr=0;
		else if(pd==0 && pg==0)
			rr=1;
		else if(pd==0 && pg==0 )
			rr=1;
		else
		{
			for(i=1;i<=n;i++)
			{
				a=(i*pd)/100;
				A=a;
				if( pd> 0 && ( (A*100)/pd)==i )
					rr=1;
			}
		}
		if(rr==1)
			printf("Case #%d: Possible\n", ct++);
		else
			printf("Case #%d: Broken\n", ct++);
	}
	return 0;
	
}
