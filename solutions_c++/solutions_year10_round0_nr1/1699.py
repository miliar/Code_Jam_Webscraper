#include <cstdio>
#include <math.h>
using namespace std;

int main()
{
	int t;
	int c, n, k;
	FILE* inf = fopen("A-large.in","r");
	FILE* outf = fopen("output","w");
	fscanf(inf, "%d", &c);
	
	for(int i=0;i<c;i++)
	{
		fscanf(inf, "%d %d", &n, &k);
		t = pow(2, n);
		if((k+1) % t == 0)
			fprintf(outf, "Case #%d: ON\n", i+1);
		else
			fprintf(outf, "Case #%d: OFF\n", i+1);			
	}
	fclose(inf);
	fclose(outf);
	return 0;
}
