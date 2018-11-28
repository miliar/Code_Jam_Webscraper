#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;

int looplen;
char str[50005];
int len;

bool used[20];
int permu[20];
int mingroup;
char tostr[50005];

void calgroup()
{
	int i, j, k;
	int count;

	i = 0;
	while (i < len) {
		for (j = 0; j < looplen; j ++) {
			tostr[i+j] = str[i+permu[j]];
		}
		i += looplen;
	}

	count = 0;
	i = 0;
	j = 0;
	while (i < len) {
		while (i < len && tostr[i] == tostr[j]) {
			i ++;
			continue;
		}
		count ++;
		j = i;
	}

	if (count < mingroup) mingroup = count;
}

void dfsmeiju(int now)
{
	int i;

	if (now == looplen) {
		calgroup();
		return;
	}

	for (i = 0; i < looplen; i ++) {
		if (used[i]) continue;
		used[i] = true;
		permu[now] = i;
		dfsmeiju(now+1);
		used[i] = false;
	}
}

int main()
{
	int i, j, k;
	int t;
	int nowt;
	int temp;

	freopen("D-small-attempt0.in.txt", "r", stdin);
//	freopen("D-small-attempt0.out.txt", "w", stdout);

	scanf("%d", &t);
	nowt = 0;
	while (t --) {
		nowt ++;

		scanf("%d", &looplen);
		scanf("%s", str);
		len = strlen(str);

		mingroup = 10000000;
		for (i = 0; i < looplen; i ++) {
			used[i] = false;
		}
		dfsmeiju(0);

		printf("Case #%d: %d\n", nowt, mingroup);
	}

	return 0;
}




