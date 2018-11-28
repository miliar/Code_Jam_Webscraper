#include <cstdio>
#include <algorithm>
using namespace std;

class r
{
	public:
	int a,b;
};

r x[1010];

bool operator < (const r &a,const r &b)
{
	return a.a>b.a;
}

int main ()
{
	
	FILE *fin=fopen ("Rope Intranet.in","r");
	FILE *fout=fopen ("Rope Intranet.out","w");
	
	int t,T;
	int n;
	int i,j;
	int ans;
	
	fscanf (fin,"%d",&T);
	
	for(t=1;t<=T;t++)
	{
		fscanf (fin,"%d",&n);
		
		for(i=0;i<n;i++)
			fscanf (fin,"%d %d",&x[i].a,&x[i].b);
		
		sort (x,x+n);
		ans=0;
		for(i=1;i<n;i++)
		{
			for(j=i-1;j>=0;j--)
			{
				if(x[i].b>x[j].b)
					ans++;
			}
		}
		
		fprintf (fout,"Case #%d: %d\n",t,ans);
	}
	
	
	return 0;
}
