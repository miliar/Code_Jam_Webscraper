#include <stdio.h>
#include <algorithm>

using namespace std;

int n;
__int64 l,h,num[102];
int check[10002],maxx;

int main()
{
	int t,tcase,re;
	int i,j,chk,cnt;

	FILE *in,*out;
	in=fopen("c.in","r");
	out=fopen("c.out","w");

	fscanf(in,"%d",&tcase);
	for(t=0;t<tcase;t++)
	{
		fscanf(in,"%I64d",&n);
		fscanf(in,"%I64d",&l);
		fscanf(in,"%I64d",&h);
		for(i=0;i<n;i++)
			fscanf(in,"%I64d",&num[i]);
		for(i=l;i<=h;i++)
			check[i]=0;

		sort(&num[0],&num[n]);

		re=-1;
		for(i=l;i<=h;i++)
		{
			chk=0;
			for(j=0;j<n;j++)
			{
				if(!(i%num[j]==0 || num[j]%i==0))
				{
					chk=1;
					break;
				}
			}
			if(chk==0)
			{
				re=i;
				break;
			}
		}
		if(re==-1)
			fprintf(out,"Case #%d: NO\n",t+1);
		else
			fprintf(out,"Case #%d: %d\n",t+1,re);
	}

	return 0;
}