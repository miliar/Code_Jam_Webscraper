

#include<iostream>
#include<cmath>
using namespace std;

int main()
{
	freopen("in.txt","r",stdin);

	freopen("out.txt","w",stdout);

	int testcases,i,t,A,B,digA=0,digB=0,ta,tb,r,s,u,max=0,j,k,l,n,sum,flag;

	int temp[8],temp1[8];

	int temp2[8];

	cin>>testcases;

	t=testcases;

	while(t)
	{
		digB=0;

		max=0;

		cin>>A>>B;

		ta=A;

		tb=B;

		if(A<10 || B<10)
		{
			printf("Case #%d: %d\n",testcases-t+1,0);

			t--;

			continue;
		}

		


		int m;

		

		for(i=A;i<=B;i++)
		{
			ta=i;

			digA=0;

		

			

		while(ta!=0)
		{
			ta=ta/10;

			digA++;
		}

		

		ta=i;

		for(k=digA;k>0;k--)
		{
			m=ta%10;

			ta=ta/10;

			temp[k-1]=m;

			
		}

	m=0;

		for(k=digA-1;k>=0;k--)
		{
			for(l=k,n=0;l<digA;n++,l++)
			{
				temp1[n]=temp[l];
				
			}
			for(l=0;l<k;l++)
			{
				temp1[n++]=temp[l];

				
			}
			if(temp1[0]!=0)
			{
				sum=0;

				for(j=0;j<n;j++)
				{
					
					sum+=temp1[n-j-1]*pow(10.0,j);
				}

				flag=0;

				for(l=0;l<m;l++)
				{
					if(temp2[l]==sum)
					{
						flag=1;

					break;
					}
				}

					


				temp2[m++]=sum;

				if(!flag)
				{

				if(sum>i && sum<=B)
				{
					
					max++;
					
				}
				}
			}
		}

		
		}
		printf("Case #%d: %d\n",testcases-t+1,max);

		t--;
	}
}

