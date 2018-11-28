#include "stdafx.h"
#include <iostream>

using std::printf;
using std::scanf;
using System::Collections::Generic::List;

using namespace System;

FILE *stream;

int main(array<System::String ^> ^args)
{
	freopen_s(&stream, "D:\\Documents\\Misc\\CodeJam\\2011\\Data\\In\\A-large.in", "r", stdin);
	freopen_s(&stream, "D:\\Documents\\Misc\\CodeJam\\2011\\Data\\Out\\A-large.out", "w", stdout);
	int N = 0;
	scanf_s("%d", &N);
	for (int i = 1; i <= N; i++)
	{
		int answer = 0;
		int P = 0;
		int oPos = 1;
		int oTimeSinceAction = 0;
		int bPos = 1;
		int bTimeSinceAction = 0;
		scanf_s("%d ", &P);
		for (int k = 1; k <= P; k++)
		{
			char actor = ' ';
			int target = 0;
			scanf("%c %d ", &actor, &target);
			if (actor == 'O')
			{
				int time = (System::Math::Abs(target - oPos) - oTimeSinceAction); 
				if (time <= 0) time = 0;
				time++;
				answer += time;
				bTimeSinceAction += time;
				oTimeSinceAction = 0;
				oPos = target;
			}
			else
			{
				int time = (System::Math::Abs(target - bPos) - bTimeSinceAction);
				if (time <= 0) time = 0;
				time++;
				answer += time;
				oTimeSinceAction += time;
				bTimeSinceAction = 0;
				bPos = target;
			}
		}		
		printf("Case #%d: %d\n", i, answer);
	}
    return 0;
}
