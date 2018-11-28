#include <iostream>
#include<sstream>
#include <cmath>
using namespace std;

int a[10100];


int main ()
{

	    int t;
		int n;
		int l,h;
		int sum,sum2,re;

		freopen("C:\\Users\\NAZI\\Desktop\\C-small-attempt2.in", "rt", stdin);
		freopen("C:\\Users\\NAZI\\Desktop\\C-small-attempt2.out", "wt", stdout);
	cin>>t;
	for(int i=0;i<t;i++)
	{//样例个数
		sum=0;
		cin>>n>>l>>h;
		for(int j=0;j<n;j++)
		{
			cin>>a[j];

			if(sum!=h-l+1)
			{
				for(int k=l;k<=h;k++)
				{
					if(k%a[j]!=0 && a[j]%k!=0)
					{
						sum++;
					}
				}
			}
			if(sum!=h-l+1) 
			{
				sum=0;
	
			}
		}
        if(sum==h-l+1) cout<<"Case #"<<i+1<<": NO"<<endl;
		else
		{
			sum2=0;
			for(int j=l;j<=h;j++)
			{
				for(int k=0;k<n;k++)
				{
					if(j%a[k]==0 || a[k]%j==0)
						sum2++;
				}
				if(sum2==n)
				{ 
					re=j;
					break;
				}
				else
				{
					sum2=0;
				}
			}
         if(sum2==n) 
		 {
			 cout<<"Case #"<<i+1<<": "<<re<<endl;
		 }
		 else
		 {
			 cout<<"Case #"<<i+1<<": NO"<<endl;
		 }
		}
	}//样例个数

	
	return 0;
}

