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
	for(int i=1;i<=t;++i)
	{
		int N;
		cin >> N;
		int sxor=0,smin=1000001,ssum=0;
		for(int j=0;j<N;++j)
		{
			int tmp;
			cin >> tmp;
			sxor^=tmp;
			ssum+=tmp;
			if(tmp<smin)
				smin=tmp;
		}
		if(sxor)
			cout << "Case #" << i << ": NO"<< endl;
		else	
			cout << "Case #" << i << ": "<< ssum-smin << endl;
	}
	return 0;
}
