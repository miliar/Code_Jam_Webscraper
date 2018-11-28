#include <cstdio>
#include <cstring>
using namespace std;
int g[20][2000],t,p,q,s;

int main()
{
	FILE *input=fopen("b.in","r");
	FILE *output=fopen("b.out","w");
	fscanf(input,"%d",&t);
	for (int t0=1;t0<=t;t0++)
	{
		s=0;
		fscanf(input,"%d",&p);
		q=1;
		for (int i=1;i<=p;i++) q*=2;
		for (int i=1;i<=q;i++)
		{
			fscanf(input,"%d",&g[0][i]);
			g[0][i]=p-g[0][i];
		}
		for (int i=1;i<=q-1;i++)
			fscanf(input,"%d",&g[0][0]);
		for (int i=1,k=2;i<=p;i++,k=2*k)
			for (int j=k;j<=q;j+=k)
			{
				g[i][j]=(g[i-1][j-k/2]>g[i-1][j])?g[i-1][j-k/2]:g[i-1][j];
				if (g[i][j]+i>=p+1) s++;
			}
		fprintf(output,"Case #%d: %d\n",t0,s);
	}
	fclose(input);
	fclose(output);
	return 0;
}