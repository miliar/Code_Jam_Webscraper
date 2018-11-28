#include<iostream>
#include<vector>
#include<string>
#include<utility>
#include<algorithm>
#include<cmath>
 using namespace std;
int GCD(int a, int b)
{
   if (b==0) return a;
   return GCD(b,a%b);
}

int LCM(int a, int b)
{
   return b*a/GCD(a,b);
}


 int main()
{
	int t,n,l,h,ar[10000],flag;
	
	cin>>t;
	for(int i=0;i<t;i++)
	{
		cin>>n>>l>>h;
		for(int j=0;j<n;j++)
		{
			cin>>ar[j];
		}
		flag=0;
		for(int j=l;j<=h;j++)
		{
			for(int k=0;k<n;k++)
			{
				if(ar[k]%j!=0&&j%ar[k]!=0)
					break;
				if(k==n-1){flag=j;break;}
			}
			if(flag)break;
		}
		if(flag)
		{
			cout<<"Case #"<<i+1<<": "<<flag<<endl;
		}
		else
		{
			cout<<"Case #"<<i+1<<": NO"<<endl;
		}
	}
	return 0;
}
