#include <cstdlib>
#include <cstdio>
#include <string>
#include <memory.h>
using namespace std;

string wcj = "welcome to code jam";
int mem[501][20];

int main()
{
	int T;
	char buffer[512];
	gets(buffer); T = atoi(buffer);
	for (int t = 1; t <= T; t++) {
		gets(buffer);
		memset(mem, 0x00, sizeof(mem));
		
		for (int i = 0; i <= 500; i++) mem[i][0] = 1;
		for (int i = 0; buffer[i]; i++) {
			for (int j = 0; j < wcj.size(); j++) {
				mem[i+1][j+1] = mem[i][j+1];
				if (buffer[i] == wcj[j]) mem[i+1][j+1] += mem[i][j];
				mem[i+1][j+1] %= 10000;
			}
		}
		printf("Case #%d: %04d\n", t, mem[strlen(buffer)][wcj.size()]);
	}
	return 0;
}
