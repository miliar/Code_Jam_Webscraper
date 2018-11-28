#include<stdio.h>
#include<math.h>
#include<stdlib.h>

int gcd(int a,int b)
{
	if(b==0) return a;
	return gcd(b,a%b);
}

int main()
{
	FILE	*fin,*fout;
	fin = fopen("\B-small-attempt2.in","r");
	fout = fopen("\B-small-attempt2.out","w");
	
	int cn,t,n,i,a[5],G;
	fscanf(fin,"%d",&t);
	for(cn=1;cn<=t;cn++)
	{
		fscanf(fin,"%d",&n);
		for(i=1;i<=n;i++)
			fscanf(fin,"%d",&a[i]);
		G = abs(a[2]-a[1]);
		for(i=3;i<=n;i++)
			G = gcd(G,abs(a[i]-a[i-1]));
		int ans=0;
		for(i=1;i<=n;i++)
			if(ceil(double(a[i])/G)*G-a[i]>ans)
				ans = ceil(double(a[i])/G)*G-a[i];
		fprintf(fout,"Case #%d: %d\n",cn,ans);
	}
}
				
