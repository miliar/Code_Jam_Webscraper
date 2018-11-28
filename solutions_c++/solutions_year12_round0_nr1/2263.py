#include <cstdio>

char map[128];
char a[120];
char b[120];

int main(int argc, char const *argv[])
{
	freopen("in.txt", "r", stdin);
	int n = 3;
	int i;
	while (n--) {
		gets(a);
		gets(b);
		i = 0;
		while (a[i]) {
			map[a[i]] = b[i];
			++i;
		}
	}
	i = 0;
	while (i<128) {
		if(map[i]) {
			printf("map['%c']='%c';\n", i, map[i]);
		}
		++i;
	}
	return 0;
}