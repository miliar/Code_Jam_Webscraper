#include<iostream>
#include<vector>
#define LLD long long int
using namespace std;

int main()
{	
	vector<int>N(100);
	
	int n,t,g,S,min,sum,c=1;
	
	cin>>t;
	
	while(t--)
	{
	 		  
			   cin>>n>>S>>min;
			   vector<LLD>max(11);
			   vector<LLD>mod(11);
	 		  while(n--)
	 		  {
			   			cin>>g;
			   			
						//if(!g%3)
						//{
						//if(g%3==2)
						if(!(g%3))   		  
						max[g/3]++;
						else
						max[g/3 + 1]++;
						//else
						//max[g/3]++;
						if(g%3==1)
						mod[g/3 + 1]++;
						
						//for(int j=0;j<=10;j++)
						//cout<<max[j]<<" ";
						//system("pause");
						}
						
				//for(int j=0;j<=10;j++)
				//cout<<max[j]<<" ";
				//system("pause");		
				
				//for(int j=0;j<=10;j++)
				//cout<<mod[j]<<" ";
				//system("pause");		
				
				int i=min-1;		
				if((max[i]-mod[i])>=S && i!=0)
				max[min]+=S;
				
				else
				if(i!=0)
				max[min]+=max[i]-mod[i];
				
				
				
				i=min;
				sum=0;
				while(i<=10)
				{
				 		sum+=max[i++];
						}		 	
					
				cout<<"Case #"<<c++<<": "<<sum<<endl;
	}
	
	return 0;
}
				 	
					 						
				 		  				 					     			
