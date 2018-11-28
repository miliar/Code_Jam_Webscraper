#include<iostream.h>
#include<conio.h>
#include<string.h>
#include<math.h>
void main()
{
	double result[100];
	int T,c,base[65],n,flag,k;
	char string[65],sym[65];
	cin>>T;
	for(int i=0;i<T;i++)
	{
		result[i]=0;
		cin>>string;
		c=0;
		n=strlen(string);
		for(int j=0;j<n;j++)
		{
			flag=0;
			for(int k=0;k<c;k++)
			{
				if(sym[k]==string[j])
					flag=1;
			}
			if(flag==0)
			{
				sym[c]=string[j];
				c++;
			}
		}
		sym[c]='\0';
		for(j=0;j<n;j++)
		{
			for(k=0;k<c;k++)
			{
				if(sym[k]==string[j])
				{
					switch(k)
					{
						case 0:base[j]=1;break;
						case 1:base[j]=0;break;
						default:base[j]=k;
					}
				}
			}
		}
		if(c==1)
			c=2;
		for(j=n-1;j>=0;j--)
		{
			result[i]=result[i]+base[j]*pow(c,n-1-j);
		}
	}
	for(i=0;i<T;i++)
	{
		cout<<"Case #"<<i+1<<": "<<result[i]<<"\n";
	}
}

