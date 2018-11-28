#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>

using namespace std;

template<class T> inline const T& Max(const T& a, const T& b){return a > b ? a : b;}
template<class T> inline const T& Min(const T& a, const T& b){return a < b ? a : b;}
template<class T> inline T sqr(const T a) {return a * a;}
const double PI = acos(-1);

FILE *fin = fopen("prob2.in", "r");
FILE *fout = fopen("prob2.out", "w");
string data;
int len;

int ans = 0;

inline bool test(__int64 value)
{
	if (value % 2 == 0) return true;
	else if (value % 3 == 0) return true;
	else if (value % 5 == 0) return true;
	else if (value % 7 == 0) return true;
	return false;
}
__int64 vvalue[20][20];

__int64 str2int(string str)
{
	int i;
	__int64 ret = 0;
	int size = str.size();
	for (i=0; i<size; ++i) {
		ret *= 10;
		ret += str[i] - '0';
	}
	return ret;
}

void dfs(int last, int pos, __int64 value)
{
	if (pos == len - 1) {
		if (test(vvalue[last][pos] + value)) {
			++ans;
	//		cout << vvalue[last][pos] + value << endl;
		}
		if (last != 0 && test(value - vvalue[last][pos])) {
			++ans;
	//		cout << value - vvalue[last][pos] << endl;
		}
		return;
	}
	dfs(last, pos+1, value);
	dfs(pos + 1, pos + 1, value + vvalue[last][pos]);
	if (last != 0) 
		dfs(pos + 1, pos + 1, value - vvalue[last][pos]);
}



void pretreat()
{
	for (int i=0; i<len; ++i) {
		for (int j=i; j<len; ++j) {
			string sub = data.substr(i, j-i+1);
			vvalue[i][j] = str2int(sub);
		}
	}
}

int main()
{
	int test;
//	fscanf(fin, "%d", &test);
	scanf("%d", &test);

	int tt;
	for (tt=1; tt<=test; ++tt) {
		fprintf(fout, "Case #%d: ", tt);
		printf("Case #%d: ", tt);
		ans = 0;
//		fscanf(fin, "%s", data);
		cin >> data;
		len = data.size();
		pretreat();
		dfs(0, 0, 0);
		fprintf(fout, "%d\n", ans);
		printf("%d\n", ans);
	}

	return 0;
}