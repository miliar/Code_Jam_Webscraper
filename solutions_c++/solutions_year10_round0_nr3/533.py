#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
typedef long long int64;
int a[1005],b[1005],d[1005];
int c[1005];
int main()
{
	int64 s,ss;
	int n,k,r,t,tt,i,j,jj,temp,l,z;
	scanf("%d",&t);
	for (tt=1;tt<=t;tt++)
	{
		scanf("%d %d %d",&r,&k,&n);
		for (i=0;i<n;i++)
			scanf("%d",a+i);
		s=0;
		memset(d,-1,sizeof(d));
		d[0]=0;
		b[0]=0;
		for (i=1;i<=r;i++)
		{
			j=b[i-1];
			jj=j;
			temp=0;
			while (1)
			{
				if (temp+a[j]<=k)
				{
					temp+=a[j];
					j=(j+1)%n;
					if (j==jj)
						break;
				}
				else
					break;
			}
			c[i-1]=temp;
			s+=temp;
			if (d[j]!=-1)
			{
				l=i-d[j];
				break;
			}
			b[i]=j;
			d[j]=i;
		}
		if (i<=r)
		{
			r=r-i;
			ss=0;
			for (z=d[j];z<i;z++)
				ss+=c[z];
			s+=(r/l)*ss;
			r%=l;
			for (z=d[j],l=0;l<r;l++,z++)
				s+=c[z];
		}
		printf("Case #%d: %I64d\n",tt,s);
	}
	return 0;
}