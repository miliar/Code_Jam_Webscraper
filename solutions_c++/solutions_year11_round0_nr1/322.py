#include <stdio.h>

int T, N;
struct Event_tag
{
	char szRobot[10];
	int nButton;
}Events[200];

void Read()
{
	scanf("%d", &N);
	for(int i = 0; i < N; i++){
		scanf("%s", Events[i].szRobot);
		scanf("%d", &Events[i].nButton);
	}
}

int Abs(int x)
{
	return x<0?-x:x;
}

int Max(int a, int b)
{
	return a>b?a:b;
}

struct 
{
	int nPos;
	int nMove;
	int nAction;
}Robot[2];

long long Solve()
{
	long long nResult = 0;
	Robot[0].nPos = 1;
	Robot[0].nMove = 0;
	Robot[0].nAction = 0;
	Robot[1].nPos = 1;
	Robot[1].nMove = 0;
	Robot[1].nAction = 0;
	for(int i = 0; i < N; i++){
		int j = 0;
		if(Events[i].szRobot[0] == 'O')
			j = 0;
		else
			j = 1;
		int nMove = Abs(Events[i].nButton-Robot[j].nPos);
		nMove -= Robot[!j].nMove+Robot[!j].nAction;
		nMove = Max(0,nMove);
		Robot[j].nPos = Events[i].nButton;
		Robot[j].nMove += nMove;
		Robot[j].nAction++;
		nResult += nMove+1;
		//
		Robot[!j].nMove = 0;
		Robot[!j].nAction = 0;
	}
	return nResult;
}

int main()
{
	scanf("%d", &T);
	// push button many times?
	for(int i = 0; i < T; i++){
		Read();
		printf("Case #%d: %lld\n", i+1, Solve());
	}
	return 0;
}