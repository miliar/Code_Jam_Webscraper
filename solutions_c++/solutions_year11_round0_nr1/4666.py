// JamA.cpp : コンソール アプリケーションのエントリ ポイントを定義します。
//
#include <stdio.h>
#include <tchar.h>
#include <vector>
#include <map>
#include <set>
using namespace std;

#pragma warning ( disable : 4996 )

void CodeMain(int caseindex)
{
	int N;
	scanf("%d", &N);
	int time = 0;
	int obpos[2] = {1, 1};
	int obtime[2] = {0, 0};

	for (int n = 0; n < N; n++) {
		char c[100];
		int pos;
		scanf("%s %d", &c, &pos);
		int index = 0;
		if (c[0] == 'B') {
			index = 1;
		}
		int plustime = abs(pos - obpos[index]);
		time = max(plustime + obtime[index], obtime[(index+1)%2]) + 1;
		obtime[index] = time;
		obpos[index] = pos;
	}
	printf("Case #%d: %d\n", caseindex, time);
}

int _tmain(int argc, _TCHAR* argv[])
{
	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; i++) {
		CodeMain(i+1);
	}
	return 0;
}

