
#include<iostream>

using namespace std;

int main()
{
	int t,n,s,*out,i,j,tempi,count=0,p,tempf,*scores;
		
	cin>>t;	
	out=new int[t];
	
	for(int i=0;i<t;i++)
	{
		count=0;
		cin>>n>>s>>p;
		scores=new int[n];
		
		for(j=0;j<n;j++)
		{
			cin>>scores[j];
		}
		
		for(j=0;j<n;j++)
		{
			if(scores[j]>=2&&scores[j]<=28)
			{
				tempf=scores[j];
				tempi=scores[j]%3;
				
				if(tempi==2)
				{
					++tempf;
				}
				
				else if(tempi==1)
				{
					if(scores[j]<10)
					{
						--tempf;
					}
					else
					{
						tempf+=2;
					}
				}
				
				tempf/=3;
			
				if(tempf>=p)
				{
					count++;
				}
				
				else if((s>0)&&(tempi!=1))
				{
					tempf++;
					if(tempf>=p)
					{
						count++;
						s--;
					}
				}			
			}
			
			else 
			{
				if(scores[j]==0)
				{
					tempf=0;
				}
				
				else if(scores[j]==1)
				{
					tempf=1;
				}
				
				else if(scores[j]>=29)
				{
					tempf=10;
				}
				
				if(tempf>=p)
				{
					count++;
				}
			}	
		}
		
		out[i]=count;
	}
	
	cout<<endl;
	
	for(i=0;i<t;i++)
	{
		cout<<"Case #"<<i+1<<": "<<out[i]<<endl;
	}

	return 0;
	
}
		
