#include <cstdio>
#include <cstdlib>
#include <string>
using namespace std;
int main()
{
	int T,ti,N,i,amin,p,xo,sum;
	//freopen("d:\\C-small-attempt0.in","r",stdin);
	//freopen("d:\\cout.txt","w",stdout);
	scanf("%d",&T);
	for (ti=0;ti<T;ti++)
	{
		amin=999999999;
		scanf("%d",&N);
		xo=sum=0;
		for (i=0;i<N;i++)
		{
			scanf("%d",&p);
			xo^=p;
			if (p<amin) amin=p;
			sum+=p;
		}
		printf("Case #%d: ",ti+1);
		if (xo==0) printf("%d\n",sum-amin); else printf("NO\n");
	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}

