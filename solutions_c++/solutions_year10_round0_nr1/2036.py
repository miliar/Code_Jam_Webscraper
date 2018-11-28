#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <queue>
#include <stack>
#include <string>
#include <cstdio>
#include <cctype>
#include <vector>
#include <cassert>
#include <iomanip>
#include <sstream>
#include <numeric>
#include <string.h>
#include <iostream>
#include <algorithm>
using namespace std;
typedef long long LL;
typedef pair<int,int> PI;
#define dbg(x) cerr << #x << " -> " << (x) << "\t";
#define dbge(x) cerr << #x << " -> " << (x) << "\n";


int main()
{
	int kase_;
	cin >> kase_;
	for ( int kase=1;kase<=kase_;kase++ )
	{
		int N,K;
		cin >> N >> K;
		string result;
		K %= (1<<N);
		if ( K + 1 == (1<<N) ) 
			result = "ON";
		else
			result = "OFF";
		cout <<"Case #" << kase <<": " << result << endl;
	}
	return 0;
}
