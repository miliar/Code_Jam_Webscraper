#include <map>
#include <set>
#include <cmath>
#include <list>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <limits>
#include <algorithm>
#include <iostream>
#include <ctime>
using namespace std;

#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define rFor(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define Rep(i,n) for (int i(0),_n(n); i < _n; ++i)
#define rRep(i,n) for (int i((n)-1); i >= 0; --i)
#define Fill(a,c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))
#define All(v) (v).begin(), (v).end()
#define Min(t) numeric_limits<t>::min()
#define Max(t) numeric_limits<t>::max()
#define VI vector<int>
#define VS vector<string>

int main()
{
	int c;
	unsigned long long ans;
	int p,k,l;
	int curr=0;
	VI freq;
	cin>>c;
	For(i,1,c)
	{
		freq.clear();
		ans=0;
		curr=0;
		printf("Case #%d: ",i);
		cin>>p>>k>>l;
		Rep(j,l)
		{
			int tmp;
			cin>>tmp;
			freq.push_back(tmp);
		}
		sort(All(freq),greater<int>());
		For(j,1,l)
		{
			if((j-1)%k==0)
				curr++;
			ans+=(curr*freq[j-1]);
		}
		cout<<ans<<endl;
	}
	return 0;
}
