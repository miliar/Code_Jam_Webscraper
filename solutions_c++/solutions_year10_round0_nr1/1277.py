#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cmath>
#include <ctime>
#include <cassert>

using namespace std;

#define mp make_pair
#define pb push_back
#define all(a) a.begin(),a.end()
#define _(a,b) memset((a),b,sizeof(a))

typedef unsigned long long ull;
typedef long long lint;

const int INF = 1000 * 1000 * 1000;
const double EPS = 1e-9;

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	int i,T;
	ull x,k;
	int n;

	cin >> T;
	for (i=0; i<T; i++)
	{
		cin >> n >> k;
		x = (1 << n) - 1;
		k = k % (1<<n);
		
		cout << "Case #" << i + 1 << ": ";
		if (k==x)
			cout << "ON";
		else
			cout << "OFF";
		if (i!=T-1)
			cout << endl;
	}

	return 0;
}