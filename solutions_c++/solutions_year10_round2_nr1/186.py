#include <algorithm>
#include <iostream>
#include <vector>
#include <string>
#include <deque>
#include <cmath>
#include <map>

using namespace std;
int M,N;
map<string,bool>Map;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);

	int T;
	cin>>T;
	string str,tmp;
	for(int t=1;t<=T;t++)
	{
		Map.clear();
		int ans=0;
		cin>>N>>M;
		for(int i=0;i<N;i++)
		{
			cin>>str;
			int k=1;
			while(k<str.size())
			{
				while(str[k]!='/'&&k<str.size())
					k++;
				tmp=str.substr(0,k);
				k++;
				Map[tmp]=true;
			}
		}
		for(int i=0;i<M;i++)
		{
			cin>>str;
			int k=1;
			while(k<str.size())
			{
				while(str[k]!='/'&&k<str.size())
					k++;
				tmp=str.substr(0,k);
				k++;
				if(Map[tmp]==false)
					ans++,Map[tmp]=true;
			}
		}
		cout<<"Case #"<<t<<": "<<ans<<endl;
	}

	return 0;
}