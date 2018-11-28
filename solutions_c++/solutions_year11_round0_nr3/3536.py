#include <cstdio>
#include <algorithm>

using namespace std;

int a[10000];

int main()
{
	FILE *in =fopen("C-large.in","r");
	FILE *out = fopen("output.txt","w");
	//in = stdin;
	//out = stdout;

	int tn, ti = 0;
	fscanf(in,"%d",&tn);
	while(tn--)
	{
		int i,n;
		int maxx = -1;
		fscanf(in, "%d",&n);
		int t = 0;
		int minn = 0x3FFFFFFF;
		int sum = 0;
		for(i=0;i<n;i++)
		{
			fscanf(in,"%d",&a[i]);
			t ^= a[i];
			sum += a[i];
			if(minn > a[i]) minn = a[i];
		}
		if(t)
			fprintf(out,"Case #%d: NO\n", ++ti);
		else
			fprintf(out,"Case #%d: %d\n", ++ti, sum - minn);
	}
}