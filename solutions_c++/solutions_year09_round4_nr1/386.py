#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;


int main()
{
	freopen("A2in.txt","r",stdin);
	freopen("A2out.txt","w",stdout);

	int T;
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		int N;
		cin>>N;
		vector<int> v(N,0);
		for(int i=0;i<N;i++)
		{
			string str;
			cin>>str;
			for(int j=0;j<str.length();j++)
			{
				if(str[j]=='1')
					v[i]=j;
			}
		}

		int ans = 0;
		for(int limit=0;limit<N;limit++)
		{
			int row=0;
			for(row=limit;row<N;row++)
			{
				if(v[row]<=limit)
					break;
			}
			ans+=row-limit;

			for(int i=row;i>limit;i--)
			{
				swap(v[i],v[i-1]);
			}
		}

		cout << "Case #" << t <<": " << ans << endl;
	}
}