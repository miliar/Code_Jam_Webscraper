#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <queue>

using namespace std;

#define REP(i,n) for(int i = 0; i < (n); ++i)
#define FORE(it,x) for(typeof(x.begin()) it=x.begin();it!=x.end();++it)
#define CLEAR(x,with) memset(x,with,sizeof(x))  

#define pb push_back
#define all(x) (x).begin(),(x).end()
#define sz(a) int((a).size())

typedef pair<int,int> pii;
typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;

int main()
{
	int numCases;
	cin >> numCases;

	for(int c=1; c<=numCases; c++)
	{
		int count;
		cin >> count;

		vector<int> a, b;
		for(int i=0; i<count; i++)
		{
			int temp;
			cin >> temp;
			a.push_back(temp);
		}
		for(int i=0; i<count; i++)
		{
			int temp;
			cin >> temp;
			b.push_back(temp);
		}

		sort( all(a) );
		sort( all(b) );

		int ans = 0;
		for(int i=0; i<count; i++)
		{
			ans += a[i] * b[count-1-i];
		}
		cout << "Case #" << c << ": " << ans << endl;
	}

	return 0;
}
