#include <stdio.h>
#include <math.h>

bool gcd(int i,int j)
{
	if(i==0||j==0||i==j)
		return false;
	if(i==1||j==1)
		return true;
	if (i > j)
	{
		i ^= j; j ^= i; i ^= j;
	}
	if(j>i*2)
		return true;
	return !gcd(i,j%i);
}

const double tt = (sqrt(5.0)-1)/2;
int main()
{
	FILE	*fin,*fout;
	fin = fopen("\C-large.in","r");
	fout = fopen("\C-large.out","w");
	
	int t,z,i,j,a1,a2,b1,b2;
	long long ans;
	fscanf(fin,"%d",&t);
	for (z = 1; z <= t; z++)
	{
		fscanf(fin,"%d%d%d%d",&a1,&a2,&b1,&b2);
		ans = 0;
		for (i = a1; i <= a2; i++)
		{
			double low = i * tt;
			double high = i / tt;
			if (b2 < low)
				ans += (b2-b1+1);
			else if (b1 > high)
				ans += (b2-b1+1);
			else if (b1 > low && b2 < high)
				;
			else if (b1 < low && b2 < high)
				ans += int(low) - b1 + 1;
			else if (b1 > low && b2 > high)
				ans += b2 - int(high);
			else
				ans += b2 - int(high) + int(low) - b1 + 1;
		}
		fprintf(fout,"Case #%d: %I64d\n",z,ans);
	}
}
