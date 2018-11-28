#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <set>
#include <queue>
#include <map>

using namespace std;

#define pii pair <int, int>
#define mp make_pair
#define ll long long

string str;

char g[50] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n;
	scanf("%d\n", &n);
	for(int i = 0; i < n; i ++) {
		getline(cin, str);
		printf("Case #%d: ", i + 1);
		for(int j = 0; j < str.size(); j ++) {
			if (str[j] == ' ')
				cout << ' ';
			else cout << g[ str[j] - 'a' ];
		}
		cout << endl;
	}
	return 0;
}