#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <algorithm>
#include <cmath>

using namespace std;

struct le {
	__int64 f;
	int i;
	le(__int64 _f) : f(_f) {}

	bool operator<(const le& rhs) {
		return f < rhs.f;
	}
};

int main()
{
	int N;
	cin>>N;
	for (int i = 0;i<N;i++)
	{
		int P,K,L;
		cin>>P>>K>>L;

		vector<le> l;
		for(int j=0;j<L;j++)
		{
			int f;
			cin>>f;
			l.push_back(le(f));
		}

		sort(l.begin(), l.end());
		reverse(l.begin(), l.end());


		int ii = 1;
		vector<le>::iterator it = l.begin();
		while (it != l.end()) {
			for(int j=0;j<K&&it != l.end();j++)
			{
				it->i = ii;
				++it;
			}
			ii++;
		}

		__int64 c = 0;
		it = l.begin();
		for (;it != l.end();it++)
		{
			c += it->f * it->i;
		}

		cout<<"Case #"<<(i+1)<<": "<<c<<endl;
	}

	return 0;
}
