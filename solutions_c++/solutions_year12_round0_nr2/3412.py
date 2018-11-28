#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
using namespace std;
int main()
{   
	int n,s,p,k=1;
	int test;
	cin>>test;
	while(test--)
	{
	cin>>n>>s>>p;
	int a[n];
	for(int i=0;i<n;i++)
	cin>>a[i];
	int suprising_case = 0,ans=0;
	sort(a,a+n);
	for(int i = 0; i < n; i++)
	{   
		int value = a[i] % 3;
		int temp = a[i]/3;
		//cout<<"\ntemp = "<<temp<<"\n";
		int sum;
		switch(value)
		  {
			case 0: //cout<<"case 0\n";
				    sum = 3*(temp);
				    //cout<<"Sum = " <<sum<<"temp = "<<temp;
				    if(a[i] < p)
				    break;
			        if(suprising_case < s )
					{
			        if(sum == a[i] && (temp+1) >= p)
			          { 
						suprising_case++;
						ans++;
						break;
						}
					}
					 else if(sum==a[i] && temp >= p)
					 {
							ans++;
					       break;
					 }		
					 break;
		    case 1:	//cout<<"case 1\n";
		            if(a[i] < p)
				    break;
			        sum = (3 * temp) + 1;
			        if(sum == a[i] && (temp+1) >= p)
					{
						ans++;
					    break;
					} 		  
					break;
		    case 2: //cout<<"case 2\n";
			        sum = (3*temp) + 2;
			        if(a[i] < p)
				    break;
			        if(suprising_case < s)
			        { //cout<<"yes";
			         if(sum==a[i] && (temp+2) >= p)
					  {
						ans++;
						suprising_case++;
						break;
					  }
					}
					  else if(sum==a[i] && (temp+1) >= p)
					  {
						ans++;
						break;
					  }		
					break;	
				}
			//cout<<"ans = "<<ans<<"suprising = "<<suprising_case<<"\n";	
		}
		printf("Case #%d: %d\n",k,ans);
		k++;
		}	
	system("pause");
	return 0;
	
}
