#include <cstdio>

int main()
{
	int tn,ti=0;
	FILE *in=fopen("A-large.in","r");
	FILE *out=fopen("output.txt","w");
	fscanf(in,"%d",&tn);
	while(tn--)
	{
		int n,k;
		fscanf(in,"%d %d",&n,&k);
		fprintf(out,"Case #%d: %s\n",++ti,((k&((1<<n)-1))==((1<<n)-1))?"ON":"OFF");
	}
}
