#include <iostream>

using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
	int T,n;
	long long k;
	scanf("%d",&T);
	for (int num=1;num<=T;num++)
	{
		printf("Case #%d: ",num);
		scanf("%d%d",&n,&k);
		int x=1;
		for(int i=1;i<n;i++)
		{
		    x=x<<1;
		    x+=1;
		}
		int y=k&x;
		if(y==x)
		    printf("ON\n");
        else
            printf("OFF\n");
		fflush(stdout);
	}
	return 0;
}
