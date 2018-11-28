#include <iostream>
using namespace std;
int W,L;
int r[20];
int x[20],y[20];
int id[20];
int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int T,runs;
	cin>>T;
	for (runs=1;runs<=T;runs++)
	{
		int n;
		cin>>n>>W>>L;
		int i,j;
		for (i=0;i<n;i++)
			cin>>r[i];
		for (i=0;i<n;i++)
			id[i]=i;
		for (i=0;i<n;i++)
			for (j=i+1;j<n;j++)
				if (r[j]>r[i])
				{
					swap(r[j],r[i]);
					swap(id[j],id[i]);
				}
		bool rev=0;
		if (W>L)
		{
			swap(W,L);
			rev=1;
		}
		int lastx=0,lasty=0;
		int nexx=r[0];
		for (i=0;i<n;i++)
		{
			int k=r[i];
			if (lasty<=W)
			{
				y[id[i]]=lastx;
				x[id[i]]=lasty;
				lasty+=2*k;
			}
			else
			{
				lastx=nexx+k;
				nexx=lastx+k;
				if (lastx>L)
					break;
				lasty=0;
				i--;
			}
		}
		if (i<n)
			puts("   ERRRRRRRRRRRRRRR");
		if (rev)
			for (i=0;i<n;i++)
				swap(x[i],y[i]);
		printf("Case #%d:",runs);
		for (i=0;i<n;i++)
			printf(" %d %d",x[i],y[i]);
		puts("");
	}
	return 0;
}
			

