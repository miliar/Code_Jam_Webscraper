#include <iostream>
#include <map>
#include <string>
using namespace std;

int main()
{
	int t;

	cin>>t;
	for(int count = 1; count <= t; count++)
	{
		int s;
		int q;
		map <string, int> freq;
		string str;

		map <string, int>::iterator it = freq.begin();
		(cin>>s).get();
		for(int i = 0; i < s; i++)
		{
			getline(cin,str);
			freq[str] = 0;
		}
		(cin>>q).get();
		string inp[q];
		bool zero = false;
		int switches = 0;
		for(int i = 0; i < q; i++)
		{
			getline(cin, str);
			freq[str]++;
			inp[i] = str;
			for(it = freq.begin();it != freq.end(); ++it)
			{
				if(it->second == 0)
				{
					zero = true;
					break;
				}
			}
			if(zero == true)
			{
				zero = false;
			}
			else
			{
				switches++;
				for(it = freq.begin(); it != freq.end(); ++it)
					it->second = 0;
				freq[str]++;
			}
		}
		cout<<"Case #"<<count<<": "<<switches<<'\n';
		switches = 0;
	}
}
