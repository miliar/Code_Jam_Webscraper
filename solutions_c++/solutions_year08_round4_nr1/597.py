#include <iostream>
#include <math.h>
#include <stdlib.h>
#include <iomanip>
#include <vector>
#include <string>
#pragma comment (linker, "/STACK:16000000")
using namespace std;
#define inf 2123456789
#define INPUT "a.in"
#define OUTPUT "a.out"

struct node
{
	int g;
	bool ch;
};

node s[30001];

int n,v;
int DFS(int pos, int val)
{
	if (pos > n/2) {//leaf
		if (val == s[pos].g) return 0;
		else return inf;
	}
	int l0 = DFS(pos*2, 0);
	int l1 = DFS(pos*2, 1);
	int r0 = DFS(pos*2+1, 0);
	int r1 = DFS(pos*2+1, 1);

	int min = inf;
	if (val == 0) {
		if (r0 < inf && l0 < inf)
			min = r0+l0;
		if (s[pos].g == 0) {
			if (s[pos].ch == true) {//or
				if (l0 < inf && r1 < inf && l0+r1+1 < min)
					min = l0+r1+1;
				if (l1 < inf && r0 < inf && l1+r0+1 < min)
					min = l1+r0+1;
			}
			else return min;
		}
		else {
			if (l0 < inf && r1 < inf && l0+r1 < min)
				min = l0+r1;
			if (l1 < inf && r0 < inf && l1+r0 < min)
				min = l1+r0;
		}
	}
	else {
		if (r1 < inf && l1 < inf)
			min = r1+l1;
		if (s[pos].g == 1) {
			if (s[pos].ch == true) {//and
				if (l0 < inf && r1 < inf && l0+r1+1 < min)
					min = l0+r1+1;
				if (l1 < inf && r0 < inf && l1+r0+1 < min)
					min = l1+r0+1;
			}
			else return min;
		}
		else {
			if (l0 < inf && r1 < inf && l0+r1 < min)
				min = l0+r1;
			if (l1 < inf && r0 < inf && l1+r0 < min)
				min = l1+r0;
		}
	}

	return min;
}				

int main()
{
	freopen(INPUT, "r", stdin);
	freopen(OUTPUT, "w", stdout);
	int t; cin >> t;
	for (int r=0; r<t; r++) {
		cin >> n >> v;
		for (int i=1; i<=(n-1)/2; i++)
			cin >> s[i].g >> s[i].ch;
		for (int i=(n-1)/2+1; i<=n; i++)
			cin >> s[i].g;
		int ans = DFS(1,v);

		cout << "Case #" << r+1 << ": ";
		if (ans < inf)
			cout << ans << endl;
		else
			cout << "IMPOSSIBLE\n";
	}
	return 0;
}