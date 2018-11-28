#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cctype> 
#include <string> 
#include <cstring> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <ctime> 



using namespace std; 

template<class T> T gcd(T a,T b){return a==0?b:gcd(b%a,a);}
FILE *f;
int main()
{
	int t;
	int a[101];
	char c[101];
	int b[101];
	int k;
	b[0]=1;
	freopen("do.txt","r",stdin);
	freopen("fian.txt","w",stdout);
    cin>>t;
	for(int i=0;i<t;i++)
	{
		int sum=0;
		int so1=1,sb1=1,so2=1,sb2=1;
		int fo=1,fb=1;
		int bu;
		cin>>a[i];
		for(int j=0;j<a[i];j++)
		{
			cin>>c[j+1]>>b[j+1];

		}
		if(a[i]==1)
		{
			cout<<"Case #"<<i+1<<":"<<" "<<b[1]<<endl;
			continue;
		}
		for(int j=1;j<=a[i];j++)
		{
			if(c[j]=='B')
			{
				
				bu=abs(b[j]-sb1)+1;
				sum=sum+bu;
				sb1=b[j];

			
			if(so2!=0)
			{
				for(k=j;k<=a[i];k++)
			   {
				if(c[k]=='O')
					break;
			   }
			}
			
			if(k>a[i])
			{
				so2=0;
			}
			if(so2!=0)
			{
			if(b[k]>so1)fo=1;
			else fo=-1;
			if(fo==1)
			{
				so1=min(so1+bu,b[k]);
			}
			else
				so1=max(so1-bu,b[k]);
			
			
			}
			}
			else 
			{
				bu=abs(b[j]-so1)+1;
				sum=sum+bu;
				so1=b[j];


			
			if(sb2!=0)
			{
				for(k=j;k<=a[i];k++)
			{
				if(c[k]=='B')
					break;
			}
				if(k>a[i])
				{
					sb2=0;
					continue;
				}
			if(b[k]>=sb1)fb=1;
			else fb=-1;
			if(fb==1)
			{
				sb1=min(sb1+bu,b[k]);
			}
			else
				sb1=max(sb1-bu,b[k]);
			
			}
			}
		
		
		
		}


     cout<<"Case #"<<i+1<<":"<<" "<<sum<<endl;


	}
	return 0;
   
   

	
}