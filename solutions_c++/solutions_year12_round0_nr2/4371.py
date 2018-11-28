#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
	int T,n,s,p;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>T;
	for(int j=1;j<=T;j++)
	{
		cin>>n>>s>>p;
		vector<int> arr(n,0);
		for(int i=0;i<n;i++)cin>>arr[i];
		sort(arr.begin(),arr.end());
		int ret=0;
		int i=n;
		int res=0;
		while(i)
		{
			i--;
			int t=arr[i]/3;
			if(arr[i]%3)t++;
			if(t>=p)res++;
			else
			{
				if(s && arr[i]>1 && arr[i]<29 && (arr[i]%3 != 1) )
				{
					t++;
					if(t>=p)
					{
						res++;
						s--;
					}
				}
			}
		}
		cout<<"Case #"<<j<<": "<<res<<endl;
	}
}