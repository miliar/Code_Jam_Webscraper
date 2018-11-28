#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int T, N;
bool order[100];
bool useButton;
int orderIdx;
class Robot
{
public:
	int path[100];
	int idx;
	int now;
	int nowIdx;
	int id;
	Robot()
	{
		idx = 0;
		now = 1;
		nowIdx = 0;
	}
	void SetOrder(int in){id = in;}
	void SetPath(int in){path[idx++] = in;}
	void doStep(int step)
	{
		if(IsFinish() == true) return;
		if(now == path[nowIdx])
		{
			if(order[orderIdx] == id && useButton == false)
			{
				nowIdx++; orderIdx++;
				useButton = true;
			}
		}
		else
		{
			if(path[nowIdx] > now) now++;
			else				   now--;
		}
	}
	bool IsFinish(){return nowIdx == idx;}
};

int main()
{
	scanf("%d", &T);
	for(int i = 1; i <= T; i++)
	{
		Robot robot[2];

		robot[0].SetOrder(0);
		robot[1].SetOrder(1);
		orderIdx = 0;
		scanf("%d", &N);
		char tr;
		int tp;
		for(int j = 0; j < N; j++)
		{
			scanf(" %c %d", &tr, &tp);
			if(tr == 'O')
			{
				robot[0].SetPath(tp);
				order[j] = false;
			}
			else if(tr == 'B')
			{
				robot[1].SetPath(tp);
				order[j] = true;
			}
		}

		int result = 0;
		for(;;result++)
		{
			useButton = false;
			if(robot[0].IsFinish() == true && robot[1].IsFinish() == true) break;
			robot[0].doStep(result);
			robot[1].doStep(result);
		}

		printf("Case #%d: %d\n", i, result);
	}

	return 0;
}
