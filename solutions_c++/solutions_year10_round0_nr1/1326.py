#include <iostream>
#include <cstdio>
using namespace std;
int t,n,k;

int main()
{
	FILE *input = fopen("a.in","r");
	FILE *output = fopen("a.out","w");
	fscanf(input,"%d",&t);
	for (int tt=1;tt<=t;tt++)
	{
		fscanf(input,"%d%d",&n,&k);
		int x=1;
		for (int i=1;i<=n;i++)
			x*=2;
		if (k%x==x-1)
			fprintf(output,"Case #%d: ON\n",tt);
		else fprintf(output,"Case #%d: OFF\n",tt);
	}
	return 0;
}