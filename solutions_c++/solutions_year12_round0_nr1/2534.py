#define _USE_MATH_DEFINES 
#define _CRT_SECURE_NO_DEPRECATE
#include <cmath> 
#include <iostream> 
#include <algorithm> 
#include <cstdio> 
#include <ctime> 
#include <map> 
#include <string> 
#include <vector> 
#include <set> 
#include <stack> 
#include <queue> 
#include <deque> 
#include <iomanip>
#include <sstream>

using namespace std; 

#pragma comment(linker, "/STACK:64000000") 
typedef long long int64; 
typedef unsigned long long uint64; 
template<class T> inline T sqr(T a) {return a * a;} 
#define prime 1103 
#define INF 123456789
#define TASK "A-small-attempt0"
#define MOD 1000000007


int a[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
	0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
	0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 32, 0,
	0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
	0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
	0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
	0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
	0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
	0, 0, 0, 121, 104, 101, 115, 111,
	99, 118, 120, 100, 117, 105, 103, 
	108, 98, 107, 114, 122, 116, 110, 
	119, 106, 112, 102, 109, 97, 113};

int main()
{
	freopen(TASK ".in", "r", stdin); 
	freopen(TASK ".out", "w", stdout); 
	int n;
	cin >> n;
	string s;
	getline(cin, s);
	for(int i = 0; i < n; ++i)
	{
		getline(cin, s);
		string res = "";
		for(int j = 0; j < s.length(); ++j)
			res += (char)a[s[j]];
		printf("Case #%d: ", i + 1);
		cout << res << endl;
	}
	return 0; 
}