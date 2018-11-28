#include <iostream>
#include <algorithm>
#include "stdio.h"
using namespace std;

//#define DBGOUT printf
void DBGOUT(...) { } 

int N,M;
char npath[10000][101];

int chkdir(char* path)
{
	int i;
	for (i = 0; i < N; i++)
		if (strcmp(npath[i], path) == 0)
			return 1;

	return 0;
}

int mkdir(char* path)
{
	char buf[101] = "";
	int ret = 0;
	int len = strlen(path);
	int i;

	if (chkdir(buf))
		return 0;

	for (i = 1; i <= len; i++)
	{
		if (path[i] == '/' || path[i] == 0x0)
		{
			memset(buf, 0, 101);
			strncpy(buf, path, i);
			if (!chkdir(buf))
			{
				strcpy(npath[N++], buf);
			}
		}
	}

	return 1;
}

int main()
{
	int case_cnt;
	int ret = 0;
	char path[101];
	int n;

	cin >> case_cnt;

	for (int i = 0; i < case_cnt; i++)
	{
		cin >> N;
		cin >> M;

		ret = 0;
		n = N;

		for (int l = 0; l < 10000; l++)
			npath[l][0] = 0x0;

		for (int j = 0; j < N; j++)
			cin >> npath[j];

		for (int k = 0; k < M; k++) 
		{
			cin >> path;
			mkdir(path);
		}

		ret = N - n;

		cout << "Case #" << i + 1 << ": " << ret << endl;
	}
}

