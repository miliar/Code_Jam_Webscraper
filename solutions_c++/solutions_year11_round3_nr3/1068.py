#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<string.h>
#include<math.h>
#include<algorithm>

/////////////--------------stl library------------------///////////
#include<stack>

using namespace std;

typedef long long int int64;
typedef long double float64;
#define shift(x)  (1<<(x));
#define shift64(x) (((int64)(1))<<(x))

int max(int a,int b)
{
	if(a>=b)
		return a;
	else 
		return b;
}
int main()
{
	int ch;
	cin>>ch;
	for(int z=1;z<=ch;z++)
	{
		int n,l,u;
		cin>>n>>l>>u;
		int arr[200];
		for(int i=0;i<n;i++)
			cin>>arr[i];
		int ans=0;
		int flag=0;
		for(int i=l;i<=u;i++)
		{
			flag=0;
			for(int j=0;j<n;j++)
			{
				if(arr[j]%i==0 || i%arr[j]==0)
				{	
				}
				else
				{
					flag=1;
					break;
				}
			}
			if(flag==0)
			{	cout<<"Case #"<<z<<": "<<i<<endl;
				ans=1;
				break;
			}
		}
		if(ans==0)
			cout<<"Case #"<<z<<": NO\n";
		
	}
	return 0;
}
