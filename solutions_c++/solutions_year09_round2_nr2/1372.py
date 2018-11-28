#include <cstdio>
#include <cstring>

using namespace std;

int digit[10];
int temp[10];
int ans;

void bt(int pos) {
	for(int i = 0; i < 9; ++i) {
		
	}
}

int sol(int n)
{
	ans = 0xFFFFFFF;	
	memset(digit, 0, sizeof(digit));
	int t = n;
	for(; t != 0; t /= 10) {
		digit[t%10]++;
	}
//	for(int i = 1; i <= 9; ++i) {
//		printf("digit[%d]:%d\n", i, digit[i]);
//	}
	int i;
	for(i = n+1; ; ++i) {
		memset(temp, 0, sizeof(temp));
		int t = i;
		for(; t != 0; t /= 10) {
			temp[t%10]++;
		}
		int ok = 1;
		for(int j = 1; j <= 9; ++j) {
			if(digit[j] != temp[j]) ok = 0;
		}
		//printf("%d %d\n", i, ok);
		if(ok) break;
	}

	return i;
}

int main()
{
	int T, N;
	scanf(" %d", &T);
	for(int _42 = 1; _42 <= T; ++_42) {
		scanf("%d", &N);
		printf("Case #%d: %d\n", _42, sol(N));
	}
	return 0;
}
