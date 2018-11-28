#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int N_SIZE = 103;

char ty[N_SIZE];
int pos[N_SIZE];
int next[N_SIZE];

int move(int from, int pNext, int step)
{
	if (pNext == -1)
		return from;
	if (abs(from - pos[pNext]) <= step)
		return pos[pNext];
	return from + (from < pos[pNext] ? step : -step);
}

int main()
{
	int testCount, nCount;
	int oPos, bPos;
	int step;
	int ans;
	
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	scanf("%d", &testCount);
	for (int ct = 1; ct <= testCount; ct++) {
		scanf("%d ", &nCount);
		for (int i = 0; i != nCount; i++)
			scanf("%c%d ", &ty[i], &pos[i]);
		memset(next, -1, sizeof(next));
		for (int i = 0; i != nCount; i++)
			for (int j = i + 1; j != nCount; j++)
				if (ty[i] != ty[j]) {
					next[i] = j;
					break;
				}
		oPos = bPos = 1;
		ans = 0;
		for (int i = 0; i != nCount; i++) {
			if (ty[i] == 'O') {
				step = abs(pos[i] - oPos) + 1;
				oPos = pos[i];
				bPos = move(bPos, next[i], step);
			}
			else {
				step = abs(pos[i] - bPos) + 1;
				bPos = pos[i];
				oPos = move(oPos, next[i], step);
			}
			ans += step;
		}
		printf("Case #%d: %d\n", ct, ans);
	}
	return 0;
}
