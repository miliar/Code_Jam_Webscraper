#include <cstring>
#include <cstdio>
#include <algorithm>
using namespace std;

/*class cl
{
	int w;
	double e;
};

bool operator < (const cl &a,const cl &b)
{
	return a.q<b.q;
}*/

int x[60];
int v[60];
int q[60];

int main ()
{
	FILE *fin=fopen ("Picking Up Chicks.in","r");
	FILE *fout=fopen ("Picking Up Chicks.out","w");
	
	int c,C;
	int n,k,b,t;
	double tt,e;
	int i,j;
	int ans;
	
	fscanf (fin,"%d",&C);
	
	for(c=1;c<=C;c++)
	{
		fscanf (fin,"%d %d %d %d",&n,&k,&b,&t);
		
		for(i=0;i<n;i++)
			fscanf (fin,"%d ",&x[i]);
		
		for(i=0;i<n;i++)
			fscanf (fin,"%d ",&v[i]);
			
		memset (q,0,sizeof q);
		
		for(i=0;i<n;i++)
		{
			if(t*v[i]<b-x[i])
			{
				q[i]=-1;
				continue;
			}
			for(j=i+1;j<n;j++)
			{
				if(v[i]>v[j])
				{
					tt=double (x[j]-x[i])/double(v[i]-v[j]);
					if(x[i]+tt*v[i]<b)
					{
						if(x[j]+v[j]*t<b)
							q[i]++;
					}
				}
			}
		}
		
		sort (q,q+n);
		j=0;
		ans=0;
		
		for(i=0;i<n;i++)
		{
			if(q[i]!=-1)
			{
				ans+=q[i];
				j++;
				if(j==k)
					break;
			}
		}
		
		if(j==k)
			fprintf (fout,"Case #%d: %d\n",c,ans);
		else
			fprintf (fout,"Case #%d: IMPOSSIBLE\n",c);
		
	}
	
	return 0;
}
