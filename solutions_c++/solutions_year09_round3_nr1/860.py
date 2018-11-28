#include<iostream>
#include<stdio.h>
#include<vector>
#include<algorithm>
#include<math.h>

using namespace std;

int main()
{
	int n,t,m=0;
	cin>>t;
	while(t--)
	{
		unsigned long long ans=0,temp;
		int a[50],i,j,k,len,base=0,value[50],num=2,flag=0;
		string str;
		cin>>str;
		m++;
		
		for(i=0;i<36;i++)
		{
			a[i]=0;
			value[i]=-1;
		}
		for(i=0;i<str.size();i++)
		{
			if(str[i]>='a')
			{
			     if(a[str[i]-'a'+10]==0)
				{
				   a[str[i]-'a'+10]=1;
				   base++;
				}
			}
			else
			{
			     if(a[str[i]-'0']==0)
			     {
				a[str[i]-'0']=1;
				base++;
			     }
				
			}
		
		}
		
		if(base==1)
			base=2;
		//cout<<"base "<<base<<endl;
		len=str.size();
		j=0;
		for(i=0;i<len;i++)
		{
			if(str[i]>='a')
			{
			
				if(value[str[i]-'a'+10]==-1)
				{
				    if(i==0)
				     {
				         k=1;
				         value[str[i]-'a'+10]=1;
				     }
				      else
				     {
				     	if(flag==0)
				     	{
				     	 	k=0;
				         	value[str[i]-'a'+10]=0;
				     		flag=1;
				     	}
				     	else
				    	 {
				     		 k=num;
				         	value[str[i]-'a'+10]=num;
				         	num++;
				     	 }
				     }
				}
				else
				 	k=value[str[i]-'a'+10];
			
				//cout<<i<<" "<<k<<endl;
				
				temp=pow(base,len-i-1)*k;
			}
			else
			{
				
				if(value[str[i]-'0']==-1)
				{
				    if(i==0)
				     {
				         k=1;
				         value[str[i]-'0']=1;
				     }
				     else
				     {
				     	if(flag==0)
				     	{
				     			k=0;
				     			value[str[i]-'0']=0;
				     			flag=1;
				     	}
				     	else
				     	{
				     		k=num;
				         	value[str[i]-'0']=num;
				         	num++;
				         }
				     
				     }
				}
				else
				 	k=value[str[i]-'0'];
				//cout<<i<<" "<<k<<endl;
				
				temp=pow(base,len-i-1)*k;
			}
			
			ans+=temp;
		
		}
		
		cout<<"Case #"<<m<<": "<<ans<<endl;
	}
}
