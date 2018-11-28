#include <iostream>
#include <cstring>
using namespace std;

char str[31], patten[20];
int len, cnt;

void DFS(int strPos, int pos)
{
	if(str[strPos] == patten[pos]) {
		if(pos == 18)
			cnt++;
		for(int i = strPos+1; i < len; i++) {
			DFS(i, pos+1);
		}
	}
}

int main()
{
	FILE *fp;
	fp = fopen("output.txt", "w");
	int N, i, j;
	strcpy(patten, "welcome to code jam");
	scanf("%d\n", &N);
	for(int cases = 1; cases <= N; cases++) {
		cnt = 0;
		gets(str);
		len = strlen(str);
		for(i = 0; i < len-18; i++) {
			DFS(i, 0);
		}
		if(cnt < 10)
			fprintf(fp, "Case #%d: 000%d\n", cases, cnt);
		else if(cnt < 100)
			fprintf(fp, "Case #%d: 00%d\n", cases, cnt);
		else if(cnt < 1000)
			fprintf(fp, "Case #%d: 0%d\n", cases, cnt);
		else {
			cnt %= 10000;
			fprintf(fp, "Case #%d: %d\n", cases, cnt);
		}
	}
	fclose(fp);
	return 0;
}
