#include <cstdio>
#include <cstring>
#include <iostream>

#include <cmath>
#include <algorithm>

#include <set>
#include <queue>
#include <stack>
using namespace std;
	int a[1010],b[1000010];

int main ()
{
	FILE *fin=freopen("a.in","r",stdin);
	FILE *fout=freopen("a.out","w",stdout);

	int T,t;
	int i,ll,tt,nn,cc,j,ans,d;

	//cin>>T;
	fscanf(fin,"%d",&T);
	for(t=1;t<=T;t++)
	{
		fscanf(fin,"%d %d %d %d",&ll,&tt,&nn,&cc);
		for(i=0;i<cc;i++)
			fscanf(fin,"%d",&a[i]);

		for(j=0,i=0;j<nn;j++)
		{
			b[j]=a[i];
			i=(i+1)%cc;
		}

		d=tt/2;
		for(i=0;i<nn;i++)
		{
			if(b[i]<d)
				d-=b[i];
			else
			{
				b[i]-=d;
				break;
			}
		}
		sort(b+i,b+nn);
		ans=tt;
		for(j=nn-1;j>=i;j--)
		{
			if(ll>0)
			{
				ans+=b[j];
				ll--;
			}
			else
			{
				ans+=b[j]*2;
			}
		}
		fprintf(fout,"Case #%d: %d\n",t,ans);
	}

	return 0;
}
