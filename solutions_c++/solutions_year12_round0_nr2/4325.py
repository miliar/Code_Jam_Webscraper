/*Dancing With the Googlers*/

#include<cstdio>

using namespace std;

int main()
{
	int i,j,N,nscount,p,S,scount,T,ti;
	freopen("B-large.in","rt",stdin);
	freopen("B.out","wt",stdout);
	scanf("%d",&T);
	for(i=1;i<=T;i++)
	{
		scanf("%d %d %d",&N,&S,&p);
		nscount=scount=0;
		for(j=0;j<N;j++)
		{
			scanf("%d",&ti);
			switch(ti%3)
			{
			case 0:
				if(ti/3>=p)
					nscount++;
				else if((ti!=0) && ((ti/3)+1==p))
					scount++;
				break;

			case 1:
				if((ti/3)+1>=p)
					nscount++;
				break;

			case 2:
				if((ti/3)+1>=p)
					nscount++;
				else if((ti/3)+2==p)
					scount++;
				break;
			}
		}
		printf("Case #%d: %d\n",i,nscount+((scount<S)?scount:S));
	}
	return 0;
}