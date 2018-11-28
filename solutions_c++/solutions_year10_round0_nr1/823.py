#include<cstdio>
#include<iostream>
#include<cstring>
#include<string>
#include<cctype>
#include<sstream>
#include<map>
#include<queue>
#include<vector>

using namespace std;

#define vi vector<int>
#define re return
#define co continue
#define sf scanf
#define pf printf

const int inf = 1000000000;

int main() {
	int t, cases = 1;
	for( scanf("%d", &t); t--; ) {
		int N, K;
		cin >> N >> K;
		int mask = (1<<N) - 1;
		bool yes = false;
		if( (K & mask) == mask ) yes = true;
		printf("Case #%d: %s\n", cases++, yes ? "ON" : "OFF");
	}

	return 0;
}
