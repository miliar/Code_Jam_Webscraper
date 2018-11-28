#include<cstdio>
int main()
{
	int k,n,t,i;
	FILE *f=fopen("A-small.in","r");
	FILE *g=fopen("A-solve.out","w");
	fscanf(f,"%d",&t);
	for(i=0;i<t;i++)
	{
		fscanf(f,"%d %d",&n,&k);
		fprintf(g,"Case #%d: %s\n",(i+1),(k%(1<<n)==(1<<n)-1?"ON":"OFF"));
	}
	fclose(f);
	fclose(g);
	return 0;
}