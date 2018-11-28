#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>

#define MAX 32800 	// Limits acc to the  problem .



#define SMALL
//#define LARGE


using namespace std;

int main()
{

	#ifdef SMALL
		freopen("C-small-attempt2.in","rt",stdin);
    		freopen("out.txt","wt",stdout);
	#endif

	#ifdef LARGE
		freopen("","rt",stdin);
     	        freopen("large_out.txt","wt",stdout);
	#endif

	int set[MAX];

	int t;
	cin>>t;

	
	int count=1;

	while(count<=t)
	{
		int n,max=0;
		cin>>n;
		int temp=pow(2,n);
		//cout<<temp;
		
		for(int i=0;i<n;i++)
			cin>>set[i];
		

		for(int i=1;i<temp-1;i++)
		{
			int sum=0;
			int sum2=0;
			int exor=0;
			int exor2=0;

			for(int j=0;j<n;j++)
			{
			
				if((i &(1<<j)))
				{
			
					sum+=set[j];
					exor^=set[j];
				}
				else			// ELements out of the set .
				{
		
					sum2+=set[j];
					exor2^=set[j];
				}
				
			}

			if(sum == exor2 )
			{
				if(sum2 > max)
					max=sum2;

				
			}
			
			if( sum2 == exor )
			{
				if(sum > max )
					max=sum;				

			}
	
		}
		if(max == 0 )
			printf("Case #%d: NO\n",count);
		else
			printf("Case #%d: %d\n",count,max);
		count++;
	}		
	
		

	

	return 0;
}
