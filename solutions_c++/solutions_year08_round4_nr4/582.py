#include <iostream>
#include <math.h>
#include <stdlib.h>
#include <iomanip>
#include <vector>
#include <string>
#pragma comment (linker, "/STACK:16000000")
using namespace std;
#define inf 2123456789
#define INPUT "d.in"
#define OUTPUT "d.out"

char s[1001];
int perm[17];
bool U[17];
int k;
int minn = inf;
int len;
char str[1001] ;

void DFS(int pos)
{
	if (pos == k) {
	//	for (int i=0; i<k; i++) cout << perm[i] << ' ';
	//	cout << endl;
		for (int i=0; i<len; i+=k) {
			for (int u=i; u<i+k; u++)
				str[u] = s[i+perm[u-i]];
		}
		int sum = 1;
		for (int i=1; i<len; i++)
			if (str[i] != str[i-1]) sum++;
		if (sum < minn) minn = sum;
	}

	for (int i=0; i<k; i++) {
		if (!U[i]) {
			U[i] = true;
			perm[pos] = i;
			DFS(pos+1);
			U[i] = false;
		}
	}
}
int main()
{
	freopen(INPUT, "r", stdin);
	freopen(OUTPUT, "w", stdout);
	int t; cin >> t;
	for (int i=0; i<t; i++) {
		cin >> k >> s;
		len = strlen(s);
		memset(U, 0, sizeof U);
		minn = inf;
		DFS(0);
		cout << "Case #" << i+1 << ": " << minn << endl;
	}

	return 0;
}