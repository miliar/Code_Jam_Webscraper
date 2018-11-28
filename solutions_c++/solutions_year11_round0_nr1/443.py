#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <algorithm>
#include <memory.h>

using namespace std;
#define MAXN 110

int N;
int casenum;
struct MIS{
	int pos;
	int color;
}mission[MAXN];

int main()
{
	char color[2];
	int pos;
	int cases;
	casenum = 1;
	freopen("test", "r", stdin);
	freopen("output", "w", stdout);
	scanf("%d", &cases);
	while(cases--)
	{
		scanf("%d", &N);
		for(int i = 0;i < N; i++){
			scanf("%s%d", color, &pos);
			if(color[0] == 'O') {mission[i].color = 0;mission[i].pos = pos;};
			if(color[0] == 'B') {mission[i].color = 1;mission[i].pos = pos;};
		}

		int oRobot = 1;
		int bRobot = 1;
		int oSave = 0;
		int bSave = 0;
		int ans = 0;
		int tmp;
		for(int i = 0;i < N; i++){
			if(mission[i].color == 0) {
				tmp = abs(mission[i].pos - oRobot) - oSave;
				tmp = max(0, tmp) + 1;

				//cout<<"O:"<<tmp<<" "<<mission[i].pos<<" "<<oRobot<<" "<<oSave<<endl;
				ans += tmp;
				oSave = 0;
				bSave += tmp;
				oRobot = mission[i].pos;
			}
			if(mission[i].color == 1)	{
				tmp = abs(mission[i].pos - bRobot) - bSave;
				tmp = max(0, tmp) + 1;

				//cout<<"B:"<<tmp<<" "<<mission[i].pos<<" "<<bRobot<<" "<<bSave<<endl;
				ans += tmp;
				bSave = 0;
				oSave += tmp;
				bRobot = mission[i].pos;
			}
		}


		printf("Case #%d: %d\n", casenum++, ans);
	}
	return 0;
}

