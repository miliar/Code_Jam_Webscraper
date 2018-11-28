#include <iostream>
#include <string>
using namespace std;
int main()
{
	int n,m,i,j,T,test=1,a,b,c,d,A,flag;
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B.out","w",stdout);
	scanf("%d", &T);
	while (T --)
	{
		scanf("%d%d%d",&n,&m,&A);
		flag=0;
		printf("Case #%d:", test++);
		for (a=0;a<=n;a++)
			for (b=0;b<=n;b++)
				for (c=0;c<=m;c++)
					for (d=0;d<=m;d++)
						if (abs(a*d-b*c) == A)
						{
							flag=1;
							printf(" 0 0 %d %d %d %d\n",a,c,b,d);
							goto loop;
						}
loop:
		if (flag == 0)
			printf(" IMPOSSIBLE\n");
	}
	return 0;
}