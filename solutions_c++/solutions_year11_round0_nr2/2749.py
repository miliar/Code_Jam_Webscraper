#include <cstdio>
#include <cstring>

int ttt, T;
int n;
bool oppose[26][26];
int combine[26][26];
int cnt[26];
int list[105];
char s[105];
void push(int x)
{
	list[++list[0]] = x;
	++cnt[x];
}
void del()
{
	int x = list[list[0]];
	--list[0];
	--cnt[x];
}

void work()
{
	char tmp[5];
	scanf("%d", &n);
	memset(combine, -1, sizeof(combine));
	memset(oppose, 0, sizeof(oppose));
	for (int i = 1; i <= n; ++i) {
		scanf("%s", tmp);
		combine[tmp[0] - 'A'][tmp[1] - 'A'] = tmp[2] - 'A';
		combine[tmp[1] - 'A'][tmp[0] - 'A'] = tmp[2] - 'A';
	}
	scanf("%d", &n);
	for (int i = 1; i <= n; ++i) {
		scanf("%s", tmp);
		oppose[tmp[0] - 'A'][tmp[1] - 'A'] = true;
		oppose[tmp[1] - 'A'][tmp[0] - 'A'] = true;
	}
	list[0] = 0;
	memset(cnt, 0, sizeof(cnt));
	scanf("%d", &n);
	scanf("%s", s);
	for (int i = 0; i < n; ++i) {
		if (list[0] > 0 && combine[list[list[0]]][s[i] - 'A'] > -1) {
			int tmp = combine[list[list[0]]][s[i] - 'A'];
			del();
			push(tmp);
		} else {
			bool del = false;
			for (int j = 0; j < 26; ++j) if (oppose[s[i] - 'A'][j] && cnt[j] > 0) {
				list[0] = 0;
				memset(cnt, 0, sizeof(cnt));
				del = true;
				break;
			}
			if (!del) 
				push(s[i] - 'A');
		}
	}
	printf("Case #%d: ", ++ttt);
	printf("[");
	for (int i = 1; i <= list[0]; ++i) {
		printf("%c", list[i] + 'A');
		if (i < list[0]) printf(", ");
	}
	printf("]\n");
}
int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf("%d", &T);
	while (T--) work();
}