#include<stdio.h>

using namespace std;

int main()
{

 int t,a,b,i,j,k,n,r,cnt,m,x;

 scanf("%d",&t);

 x = 1;

 while(t--)
 {
	scanf("%d%d",&a,&b);

	m = a;
	cnt = 0;

	//printf("hi");

	while(m<=b)
	{
		n = m;	
		r = n;
		//printf("%d ",m);

		while(1)
		{
			if((n%10==0 && n/100==0) || (n%100==0 && n/1000==0) || (n%1000==0 && n/10000==0) || (n%10000==0 && n/100000==0) || (n%100000==0 && n/1000000==0) || (n%1000000==0))
				break;
		
			k = n%10;
	
			if(k==0)
			{
				k = n%100;
				j = n/100;
				
				if(k!=0)
				{
					if(j<10)
						n = k*10 + j;
					else if(j<100)
						n = k*100 + j;
					else if(j<1000)
						n = k*1000 + j;
					else if(j<10000)
						n = k*10000 + j;
					else
						n = k*100000 + j;
				}
				else
				{
					k = n%1000;
					j = n/1000;
		
					if(k!=0)
					{	
						if(j<10)
							n = k*10 + j;
						else if(j<100)
							n = k*100 + j;
						else if(j<1000)
							n = k*1000 + j;
						else if(j<10000)
							n = k*10000 + j;
						else
							n = k*100000 + j;
					}
					else
					{
						k = n%10000;
						j = n/10000;
	
						if(k!=0)
						{
							if(j<10)
								n = k*10 + j;
							else if(j<100)
								n = k*100 + j;
							else if(j<1000)
								n = k*1000 + j;
							else
								n = k*10000 + j;				
						}
						else
						{
							k = n%100000;
							j = n/100000;

							if(k!=0)
							{
								if(j<10)
									n = k*10 + j;
								else if(j<100)
									n = k*100 + j;
								else if(j<1000)
									n = k*1000 + j;
							}
							else
							{
								k = n%1000000;
								j = n/1000000;	

								n = k*10 + j;
							}
						}
					}

					
				}
			}
			else
			{
				j = n/10;
				if(j<10)
					n = k*10 + j; 
				else if(j<100)
					n = k*100 + j;
				else if(j<1000)
					n = k*1000 + j;
				else if(j<10000)
					n = k*10000 + j;
				else if(j<100000)
					n = k*100000 + j;
				else
					n = k*1000000 + j;
					
			}

			if(j==0 || n==r)
				break;
	
			if(n>r && n<=b)
			{
				cnt++;
				//printf("%d ",n);
			}
		}
		//printf("\n");

		m++;
	}

	printf("Case #%d: %d\n",x,cnt);
	x++;

 }

}
		


		
			

