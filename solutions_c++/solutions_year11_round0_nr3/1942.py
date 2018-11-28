# include <cstdio>
using namespace std;
int main()
{
	int t,n;
	scanf("%d",&t);
	for(int test=1;test<=t;test++)
	{
		int min=0xfffffff,total=0,res=0;
		scanf("%d",&n);
		while(n--)
		{
			int tmp;
			scanf("%d",&tmp);
			res^=tmp;
			total+=tmp;
			if(tmp<min) min=tmp;
		}
		if(!res)
		  printf("Case #%d: %d\n",test,total-min);
		else printf("Case #%d: NO\n",test);
	}
	return 0;
}