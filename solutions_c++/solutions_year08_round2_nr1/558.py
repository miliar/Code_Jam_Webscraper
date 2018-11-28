#include <iostream>
#define MAX 110
using namespace std;

struct pkt { long long x,y; } t[MAX];

long long n, A, B, C, D, x0, y0, M;

main()
{
    int N;
    scanf("%d",&N);
    for(int c=1;c<=N;c++)
    {
    scanf("%lld %lld %lld %lld %lld %lld %lld %lld",&n, &A, &B, &C, &D, &x0, &y0, &M);    
    t[0].x=x0;
    t[0].y=y0;
    for(int i=1;i<n;i++)
    {
	//printf("%lld %lld\n",t[i-1].x,t[i-1].y);
	t[i].x=(A * t[i-1].x + B) % M;
	t[i].y=(C * t[i-1].y + D) % M;
    }
    //for(int i=0;i<n;i++) printf("%lld %lld\n",t[i].x,t[i].y);
    //printf("de\n");
    int result=0;
    for(int i=0;i<n;i++)
    {
	for(int j=i+1;j<n;j++)
	{
	    for(int x=j+1;x<n;x++)
	    {
		if((t[i].x+t[j].x+t[x].x)%3==0)
		{
		    if((t[i].y+t[j].y+t[x].y)%3==0)
		    {
			result++;
		    }
		}
	    }
	}
    }
    printf("Case #%d: %d\n",c,result);
    }
    return 0;
}
