#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
	int t;
	cin >> t;
	for(int ti=0;ti<t;ti++)
	{
		string a,ret;
		cin >> a;

		ret = a;
		next_permutation(ret.begin(), ret.end());
		if(ret<=a)
		{
			for(int i=0;i<(int)ret.length();i++)
				if(ret[i]!='0')
				{
					swap(ret[0],ret[i]);
					ret = ret[0]+("0"+ret.substr(1,ret.length()));
					break;
				}
		}

		cout << "Case #"<<ti+1 << ": "<<ret << endl;
	}
}
