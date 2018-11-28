#include<iostream.h>
void main()
{
	unsigned long int r, k, g[1008],sum,total[52],num,sum1[16208],suma,sumb,sumc;
	int n,t,start[16208],flag;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		cin>>r;
		cin>>k;
		cin>>n;
		for(int j=0;j<n;j++)
			cin>>g[j];
		j=0;
		total[i]=0;
		flag=1;
		for(unsigned long int m=0;m<r;m++)
		{
			sum=0;
			for(unsigned long int p=0;p<m;p++)
			{
				if(j==start[p])
				{
					total[i]=0;
					suma=sumb=sumc=0;
					for(unsigned int q=0;q<m;q++)
					{
						if(q<p)
							suma=suma+sum1[q];
						if(q>=p&&q<p+(r-p)%(m-p))
							sumb=sumb+sum1[q];
						if(q>=p)
							sumc=sumc+sum1[q];
					}
					num =(r-p)/(m-p);
					total[i]=suma+sumb+num*sumc;
					flag=0;
				}
			}
			if(flag==1)
			{
			start[m]=j;
			while(sum+g[j]<=k)
			{
				sum=sum+g[j];
				j++;
				if(j==n)
					j=0;
				if(j==start[m])
					break;
			}
			sum1[m]=sum;
			total[i]=total[i]+sum;
			}
			else
				break;
		}
	}
	for(i=0;i<t;i++)
	{
		cout<<"Case #"<<i+1<<": "<<total[i]<<"\n";
	}
}



