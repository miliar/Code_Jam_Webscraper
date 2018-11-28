#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <cassert>
#include <algorithm>
typedef long long LL;

using namespace std;

int main()
{
	int t;
	cin >> t;
	cout.precision(6);
	for(int i=1;i<=t;++i)
	{
		int T,ctr=0;
		cin >> T;
		for(int j=1;j<=T;++j)
		{
			int tmp;
			cin>> tmp;
			if(tmp!=j)
				++ctr;
		}
		cout << "Case #" << i << ": "<< ctr << endl;
	}
	return 0;
}
