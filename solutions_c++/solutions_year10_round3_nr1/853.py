#include <cstdio>
FILE *in,*out;
int a[1005],b[1005];
int intersect(int x,int y)
{
	if ((a[x]<a[y]&&b[x]>b[y])||(a[x]>a[y]&&b[x]<b[y]))
		return 1;
	return 0;
}
int main()
{
	int t,T,i,j,n,nr;
	in=fopen("rope.in","r");
	out=fopen("rope.out","w");
	fscanf(in,"%d",&T);
	for (t=1;t<=T;t++)
	{
		fscanf(in,"%d",&n);
		nr=0;
		for (i=1;i<=n;i++)
		{
			fscanf(in,"%d%d",&a[i],&b[i]);
			for (j=1;j<i;j++)
				if (intersect(i,j))
					nr++;
		}
		fprintf(out,"Case #%d: %d\n",t,nr);
	}
	fclose(in);
	fclose(out);
	return 0;
}
