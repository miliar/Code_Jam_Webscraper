#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
char anst[1000],im[1000]; 
int data[256],use[256];
long long ans,base;
int main()
{
	int in,n,m,o,r,max;
	scanf("%d",&in);
	for(n=0;n<in;n++)
	{
		max=-999;
		scanf("%s",im);
		ans=0;
		base=1;
		r=strlen(im);
		for(m=0;m<256;m++)
		{
			use[m]=0;
			data[m]=0;
		}
		
		for(m=0;m<r;m++)
		{
			if(data[im[m]]==0)
			{
				for(o='0';o<256;o++)
				{
					if(use[o]==0)
					{
						if(!(o=='0'&&m==0))
						{
							data[im[m]]=o;
							use[o]=1;
							break;
						}
					}
				}
			}
			anst[m]=data[im[m]];
			if(anst[m]>max)
				max=anst[m];
		}
		max-='0';
		max++;
		anst[r]=0;
		for(m=r-1;m>=0;m--)
		{
			ans+=base*(anst[m]-'0');
			base*=max;
		}
		printf("Case #%d: %lld\n",n+1,ans);
	}
}
