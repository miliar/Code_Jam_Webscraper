#include<stdio.h>

int main()
{
	int t,j=0,len,a,b,i,k,n,n1,sum,mm,yi,tt;
	int bei[7]={1,10,100,1000,10000,100000,1000000};
	int m[10],o[10];
	int yiyang[10];
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		j++;
		sum=0;
		scanf("%d%d",&a,&b);
		for(n=a;n<b;n++)
		{
			len=0;
			i=0;
			n1=n;
			yi=0;
			while(n1!=0)
			{
				m[i]=n1%10;
				i++;
				n1=n1/10;
			}
			len=i;
			for(k=0;k<len;k++)
			{
				o[k]=m[len-1-k];
			}
			for(i=1;i<len;i++)
			{
				mm=0;
				if(o[i]==0)continue;
				for(k=i;k<len+i;k++)
				{
					mm=mm+o[k%len]*bei[len-k+i-1];
				}
				if(mm<=b && mm>n)
				{
					sum++;
					yiyang[yi]=mm;
					yi++;
				}
			}
			for(i=0;i<yi;i++)
			{
				for(k=i+1;k<yi;k++)
				{
					if(yiyang[i]>yiyang[k])
					{
						tt=yiyang[i];
						yiyang[i]=yiyang[k];
						yiyang[k]=tt;
					}
				}
			}
			for(i=0;i<yi-1;i++)
			{
				if(yiyang[i]==yiyang[i+1])sum--;
			}
		}
		printf("Case #%d: %d\n",j,sum);

	}
}