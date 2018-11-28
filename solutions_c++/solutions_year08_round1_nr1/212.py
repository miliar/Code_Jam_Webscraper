#include<stdio.h>
#include<algorithm>
using namespace std;
typedef long long ll;
int cs,z;
FILE*in=fopen("prod1.in","r");
FILE*out=fopen("prod1.out","w");
int v1[900];
int v2[900];
int n;
int main()
{
	int i,j,k;
	ll best,cur;
	fscanf(in,"%d",&cs);
	for(z=0;z<cs;z++)
	{
		best=1LL<<60;
		fscanf(in,"%d",&n);
		for(i=0;i<n;i++)
			fscanf(in,"%d",&v1[i]);
		for(i=0;i<n;i++)
			fscanf(in,"%d",&v2[i]);
		sort(v1,v1+n);
		do
		{
			cur=0;
			for(i=0;i<n;i++)
				cur+=v1[i]*v2[i];
			best=min(best,cur);
		}while(next_permutation(v1,v1+n));

		fprintf(out,"Case #%d: %lld\n",z+1,best);
	}
	return 0;
}