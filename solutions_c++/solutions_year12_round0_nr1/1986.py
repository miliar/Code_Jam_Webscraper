#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
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
#include <ctime>
#include <cstring>
#include <climits>
//#define NDEBUG
#include <cassert>
using namespace std;
#define memsetz(NAME) memset(NAME, 0, sizeof(NAME))
typedef long long i64;

//char mx[128];
char mx[128] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
int main()
{
	int n; cin >> n;
	getchar();
	for (int T = 1; T <= n; T++) {
		char c;
		cout << "Case #" << T << ": ";
		while ((c = getchar()) != '\n')
			if (c < 0) {
				putchar(c);
				getchar();
				putchar(c);
			} else if (islower(c)) {
				cout << mx[c - 'a'];
			} else cout << c ;
		cout << endl;
	}
//	char c;
//	string string_a, string_b;
//	int times = 0;
//	while (times++ < 3) {
//		while ((c = getchar()) != '\n')
//			if (c < 0) getchar();
//			else if (islower(c))
//				string_a += c;
//		while ((c = getchar()) != '\n')
//			if (c < 0) getchar();
//			else if (islower(c))
//				string_b += c;
//		for (int i = 0; i < string_a.size(); i++) {
//			if (mx[string_a[i]])
//				if (mx[string_a[i]] != string_b[i])
//					cout << "yikes" << endl;
//			mx[string_a[i]] = string_b[i];
//		}
//		string_a = string_b = "";
//	}
//	for (int i = 'a'; i <= 'z'; i++) {
//		if (mx[i])
//			cout << '\'' << mx[i] << '\'' << ", ";
//		else
//			cout << '\'' << 'q' << '\'' << ", ";
//	}
//	for (int i = 'a'; i <= 'z'; i++) {
//		cout << (char) i << ":";
//		if (mx[i])
//			cout << mx[i] << ' ' ;
//		cout << endl;
//	}
	return 0;
}
