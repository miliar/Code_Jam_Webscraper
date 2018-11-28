#include <cstdio>
#include <cmath>
#define nmax 1000050
FILE *in,*out;
int nr,p[nmax], v[nmax];
void ciur(int n)
{
	int i,j;
	for (i=2;i<=n;i++)
		if (!v[i])
		{
			nr++;
			p[nr]=i;
			for (j=i;j<=n;j+=i)
				v[j]=1;
		}
}

int main()
{
	int T,t,i,aux,q,radical,rez;
	long long n;
	in=fopen("c.in","r");
	out=fopen("c.out","w");

	fscanf(in,"%d",&T);
	
	ciur(1000005);

	for (t=1;t<=T;t++)
	{
		fscanf(in,"%lld",&n);
		
		radical = sqrt(n);
		rez = 0;
		for (i=1;i<=nr && p[i] <= radical ;i++)
		{
			aux = n;
			q=0;
			while (aux >= p[i])
			{
				aux /= p[i];
				q++;
			}
			q--;
			rez += q;
		}
		if ( n != 1)
			rez++;
		fprintf(out,"Case #%d: %d\n",t,rez);
	}

	fclose(in);
	fclose(out);
	return 0;
}
