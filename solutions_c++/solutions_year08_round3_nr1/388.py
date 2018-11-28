// program written in C++
// compiled with g++ 3.4.2

#include <iostream>
#include <cstdlib>
#include <list>
#include <stack>
#include <queue>
#include <algorithm>
#include <set>
#include <vector>
#include <map>
#include <cmath>
#include <cstring>
#include <iterator>
#include <functional>
using namespace std;
typedef unsigned long long ull;

int main()
{
	int z,n,i,j,k;
	int p,l,g,h,L,ll;
	int m;
	ull count;
		
	cin >> n;
	
	for (z=1; z<=n; ++z)
	{
		cin >> p>>k>>l;
		vector<ull> L;
		count = 0;
		for (i=0;i<l;++i)
		{ cin >> ll; L.push_back(ll);}
		sort(L.begin(), L.end());
		reverse(L.begin(), L.end());
		
		for(i=0; i<L.size(); ++i)
		{
			m = i/k + 1;
			count += L[i] * m;
		}
		
		L.clear();		
		
		cout << "Case #" << z << ": " << count 
		<< endl;
	}

	return 0;
}
