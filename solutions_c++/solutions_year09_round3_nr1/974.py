#include <cstdio>
#include <cstring>
#include <cmath>

using namespace std;

char buff[100];
char symbol[100];
int val[1000];

int sol()
{
	int nsym = 0;
	int len;
	int ans = 0;
	len = strlen(buff);
	//printf("buff:%s\n", buff);
	for(int i = 0; buff[i] != '\0'; ++i) {
		int found = 0;
		for(int j = 0; j < nsym; ++j) {
			if(buff[i] == symbol[j]) found = 1;
		}
		if(found) continue;
		symbol[nsym] = buff[i];
		nsym++;
	}
	if(nsym < 2) nsym = 2;
	//printf("nsym:%d\n", nsym);
	val[symbol[0]] = 1;
	val[symbol[1]] = 0;
	for(int i = 2; i < nsym; ++i) {
		val[symbol[i]] = i;
	}
	for(int i = len-1, j = 0; i >= 0; --i, ++j) {
		//printf("buff[%d]:%c val[%c]:%d", i, buff[i], buff[i], val[buff[i]]);
		//printf(" -> %d*pow(%d, %d) = %d\n", val[buff[i]], nsym, j, val[buff[i]]*pow(nsym, j));
		ans += val[buff[i]]*pow(nsym, j);
	}
	return ans;
}

int main()
{
	int T;
	scanf(" %d", &T);
	for(int _42 = 1; _42 <= T; ++_42) {
		memset(buff, 0, sizeof(buff));
		memset(symbol, 0, sizeof(symbol));
		memset(val, 0, sizeof(val));
		scanf(" %[^\n]\n", buff);
		printf("Case #%d: %d\n", _42, sol());
	}
	return 0;
}
