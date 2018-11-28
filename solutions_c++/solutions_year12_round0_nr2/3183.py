#include<iostream>

using namespace std;
 
 
 
int main()
{
	int k=1,t;
	scanf("%d" , &t);
	while(t--)
	{
		int n,p,s,a,i,exception=0,count1=0;
		scanf("%d %d %d", &n , &s , &p);
		for(i=0;i<n;i++)
		{
			scanf("%d" , &a);
			if((!(a%3)) && ((a/3)>=p))
			{
				count1++;
			}
			else if((!((a+1)%3)) && (((a+1)/3)>=p))
			{
				count1++;
			}
			else if((!((a+2)%3)) && (((a+2)/3)>=p))
			{
				count1++;
			}
			else if(a>0 && (!((a+3)%3)) && (((a+3)/3)>=p) && exception<s)
			{
				count1++;exception++;
			}
			else if((!((a+4)%3)) && (((a+4)/3)>=p) && exception<s)
			{
				count1++;exception++;
			}
		}
		printf("Case #%d: %d\n" , k , count1);
		k++;
	}


		
		
	
	
	
 
        
        
    return 0;
}