#include<stdio.h>

__int64 l,n,c,tt;
__int64 t;
__int64 o,la;
__int64 a[10000005];
__int64 b[10005];
__int64 b1[10005];

int main()
{
	__int64 i,j,k,p,su;
	FILE *fp1;
	FILE *fp2;
	fp1=fopen("input.in","r");
	fp2=fopen("output.out","w");
	fscanf(fp1,"%I64d",&tt);
	
	for(k=1;k<=tt;k++)
	{
		fscanf(fp1,"%I64d %I64d %I64d %I64d",&l,&t,&n,&c);
		o=la=0;
		for(i=0;i<=10000;i++)
			b[i]=b1[i]=0;
		for(i=1;i<=c;i++)
		{
			fscanf(fp1,"%I64d",&a[i]);
			b[a[i]]+=1;
			b1[a[i]]+=1;
			o+=a[i];
			la+=a[i]*2;
		}
		for(i=c+1;i<=n;i++)
		{
			p=i%c;
			if(p==0)
				p=c;
			a[i]=a[p];
			la+=a[i]*2;
			b[a[i]]+=1;
		}
		for(i=1;i<i+1;i++)
		{
			if(i*c>n)
				break;
			if(i*o*2>=t)
			{
				for(j=0;j<=10000;j++)
				{
					b[j]-=b1[j]*(i-1);
				}
				t-=o*(i-1)*2;
				su=0;
				for(j=1;j<=c;j++)
				{
					su+=a[j]*2;
					if(su>=t)
					{
						b[a[j]]--;
						b[(su-t)/2]++;
						break;
					}
					else
					{
						b[a[j]]--;
					}
				}
				break;
			}
		}
		for(i=10000;i>=0;i--)
		{
			if(l>b[i])
			{
				la-=b[i]*i;
				l-=b[i];
			}
			else
			{
				la-=l*i;
				break;
			}
		}
		fprintf(fp2,"Case #%I64d: %I64d\n",k,la);
	}
	fclose(fp1);
	fclose(fp2);
	return 0;
}