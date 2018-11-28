#include<iostream>
using namespace std;
int main()
{
	freopen("outt.txt","w",stdout);
	int  t;
	long long  n,k;
	int p=1;
	long long temp;
	scanf("%d",&t);
	while(t--)
	{
		cin>>n>>k; 
		temp=1<<n;
		if((k+1)%temp==0)
		{
			printf("Case #%d: ON\n",p);
		}
		else
		{
		    printf("Case #%d: OFF\n",p);
		    
		}
        p++;    
    }
}


