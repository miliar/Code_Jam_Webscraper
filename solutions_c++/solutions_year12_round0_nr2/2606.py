#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>

#define MAXN 110

using namespace std;

int pont[40][2];

int inp[MAXN];

void pre() {
	memset(pont, -1, sizeof(pont));
	for(int i = 0; i < 11; ++i)
	for(int j = i; j < 11; ++j)
	for(int k = j; k < 11; ++k) {
		if(k - i > 2) break;
		int p = i + j + k;
		bool magic = false;
		if(i + 2 == j || j + 2 == k || i + 2 == k) magic = true;
		if(pont[p][magic] < k) pont[p][magic] = k;
	}

	/*
	for(int i = 0; i < 32; ++i)
		printf("<< pont[%d] %d %d\n", i, pont[i][0], pont[i][1]);
	printf("\n");
	//*/
}

bool cmp(const int i, const int j) {
	if(pont[i][0] != pont[j][0]) return pont[i][0] > pont[j][0];
	return pont[i][1] < pont[j][1];
}
bool cmp2(const int i, const int j) {
	if(pont[i][1] != pont[j][1]) return pont[i][1] > pont[j][1];
	return pont[i][0] < pont[j][0];
}

int main() {
	pre();
	int casos, n, s, mini;
	scanf("%d", &casos);
//	printf(">>> %d\n", casos);
	for(int caso = 1; caso <= casos; ++caso) {
		scanf("%d%d%d", &n, &s, &mini);
		for(int i = 0; i < n; ++i) scanf("%d", &inp[i]);

		int ans = 0;
		/*
		for(int i = 0; i < n && s; ++i) {
			if(inp[i] == 2 || inp[i] == 3) {
				inp[i] = 0; --s;
				if(mini <= 2) ++ans;
			}
		}
		//*/
			
		sort(inp, inp + n, cmp);
		/*
		for(int i = 0; i < n; ++i)
			printf("%d %d\n", i, inp[i]);
		printf("\n");
		//*/
		for(int i = 0; i < n; ++i)
			if(mini <= pont[ inp[i] ][0]) ++ans, inp[i] = 0;

		/*
		for(int i = 0; i < n; ++i)
			printf("%d %d\n", i, inp[i]);
		printf("\n");
		//*/

		sort(inp, inp + n, cmp2);
		/*
		for(int i = 0; i < n; ++i)
			printf("%d %d\n", i, inp[i]);
		printf("\n");
		//*/
		for(int i = 0; i < n && s; ++i)
			if(mini <= pont[ inp[i] ][1]) ++ans, --s, inp[i] = 0;
		
		printf("Case #%d: %d\n", caso, ans);
	}
	
	return 0;
}


