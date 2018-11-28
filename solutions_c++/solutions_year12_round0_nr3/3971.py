#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

const int MAXN = 2000003;

vector<int> arr[MAXN];

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	
	for(int i=0;i<MAXN;i++)
	{	
		vector<int> cur;
		int t = i;
		do
		{
			cur.push_back(t%10);
			t /= 10;
		}while(t);
		reverse(cur.begin(), cur.end());
		for(int k=0;k<cur.size();k++)
		{
			int val = 0;
			
			for(int j=cur.size()-1-k;j<cur.size();j++)
				val = val*10+cur[j];
			for(int j=0;j<cur.size()-1-k;j++)
				val = val*10+cur[j];
			arr[i].push_back(val);
		}
	}
	for(int i=0;i<MAXN;i++)
	{
		sort(arr[i].begin(), arr[i].end());
		arr[i].erase(unique(arr[i].begin(),arr[i].end()), arr[i].end());
	}

	int n;
	cin>>n;

	for(int i=0;i<n;i++)
	{
		int a,b;
		cin>>a>>b;
		int ans = 0;
		for(int j=a;j<=b;j++)
		{
			for(int k=0;k<arr[j].size();k++)
				if(arr[j][k] > j && arr[j][k] <= b)
					ans++;
		}
		cout<<"Case #"<<i+1<<": "<<ans<<endl;
	}

	return 0;
}