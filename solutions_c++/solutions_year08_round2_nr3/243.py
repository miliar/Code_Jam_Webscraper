#include <iostream>
using namespace std;
#define MAX 5010

bool known[MAX];
int d[110];
int posit[MAX];
int dat[151][MAX];

int main()
{
	int t,k,n,i,j,l;
	int pos;
	FILE *in=fopen("data.txt","r");

	freopen("C-small-attempt2.in","r",stdin); 
	freopen("out.txt","w",stdout);
	
	for (i=4850;i<=5000;++i)
	{
		fscanf(in,"%d",&k);
		for (j=0;j<k;++j) fscanf(in,"%d",&dat[k-4850][j]);
	}
	
	scanf("%d",&t);
	for (l=1;l<=t;++l)
	{
		scanf("%d",&k);
		scanf("%d",&n);
		for (i=0;i<n;++i) scanf("%d",&d[i]);

		if (k>=4850&&k<=5000)
		{
			printf("Case #%d:",l);
			for (i=0;i<n;++i)
			printf(" %d",dat[k-4850][d[i]-1]);
			printf("\n");
			continue;
		}

		memset(known,0,sizeof(known));
		pos=-1;
		for (i=1;i<=k;++i)
		{
			j=0;
			while (j<i)
			{
				pos=(pos+1)%k;
				if (!known[pos])
				{
					++j;
				}
			}
			known[pos]=true;
			posit[pos+1]=i;
		}
		printf("Case #%d:",l);
		for (i=0;i<n;++i)
			printf(" %d",posit[d[i]]);
		printf("\n");
	
	}

	return 0;
}


