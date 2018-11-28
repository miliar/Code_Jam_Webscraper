#include <cstdio>
#include <cstdlib>
#include <string>
#include <iostream>
#include <vector>
using namespace std;

int N;
char DataStr[505];
const char * ObStr = "welcome to code jam";
int cnt = 0;


void f(int x, int y )
{
	if(x >= 19)
	{
		cnt++;
		return;
	}
	int len = strlen(DataStr);
	for(int i = y; i < len; i++)
	{
		if(len - i < 19-x) return;
		if(DataStr[i] == ObStr[x]) f(x+1, i+1);
	}
}


int main()
{
	freopen("C-small-attempt2.in", "r", stdin);
	freopen("csout.txt", "w", stdout);
	scanf("%d", &N);
	getchar();
	
	for(int i = 0; i < N; i++)
	{
		cnt = 0;
		gets(DataStr);
		f(0, 0);
		printf("Case #%d: %04d\n", i+1, cnt);
	}	
	return 0;
}
