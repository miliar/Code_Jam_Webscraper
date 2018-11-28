#include <cstdio>
#include <cstring>
#include <iostream>

#include <cmath>
#include <algorithm>

#include <set>
#include <queue>
#include <stack>
using namespace std;

int main ()
{
	FILE *fin=freopen("a.in","r",stdin);
	FILE *fout=freopen("a.out","w",stdout);

	int T,t;
	int i,j,n,l,h,f[1000];
	bool b;

	//cin>>T;
	fscanf(fin,"%d",&T);
	for(t=1;t<=T;t++)
	{
		fscanf(fin,"%d %d %d",&n,&l,&h);
		for(i=0;i<n;i++)
			fscanf(fin,"%d",&f[i]);
		
		b=true;
		for(i=l;i<=h;i++)
		{
			for(j=0;j<n;j++)
			{
				if(f[j]%i!=0 && i%f[j]!=0)
					break;
			}
			if(j==n)
			{
				fprintf(fout,"Case #%d: %d\n",t,i);
				b=false;
				break;
			}
		}
		if(b)
		{
			fprintf(fout,"Case #%d: NO\n",t,i);
		}
	}

	return 0;
}
