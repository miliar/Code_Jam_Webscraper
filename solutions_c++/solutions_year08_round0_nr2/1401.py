#include <iostream>
#include <algorithm>
using namespace std;



struct node
{
	int beginTime, endTime;
};
node A[200], B[200];
int turnTime = 0, ta, tb, resA, resB;
void InputData()
{
	int hh, mm;
	scanf("%d", &turnTime);
	scanf("%d%d", &ta, &tb);
	for(int i = 0; i < ta; i++)
	{
		scanf("%d:%d", &hh, &mm);
		A[i].beginTime = hh * 60 + mm;
		scanf("%d:%d", &hh, &mm);
		A[i].endTime = hh * 60 + mm;
	}
	for(int i = 0; i < tb; i++)
	{
		scanf("%d:%d", &hh, &mm);
		B[i].beginTime = hh * 60 + mm;
		scanf("%d:%d", &hh, &mm);
		B[i].endTime = hh * 60 + mm;
	}
}
bool MyCMP(const node &a, const node &b)
{
	if(a.beginTime != b.beginTime)
	{
		return a.beginTime < b.beginTime;
	}
	return a.endTime < b.endTime;
}
void TrainGo(int id, int beginP, int current, int beginQ)
{
	if(id == 0)
	{
		while(beginP < ta && A[beginP].beginTime < current)	beginP++;
		if(beginP < ta)
		{
			A[beginP].beginTime = -1;
			TrainGo(1, beginQ, A[beginP].endTime + turnTime, beginP+1);
		}
	}else
	{
		while(beginP < tb && B[beginP].beginTime < current)	beginP++;
		if(beginP < tb)
		{
			B[beginP].beginTime = -1;
			TrainGo(0, beginQ, B[beginP].endTime + turnTime, beginP+1);
		}
	}
}
void Process()
{
	int beginA = 0, beginB = 0;
	while(beginA < ta && beginB < tb)
	{
		while(A[beginA].beginTime < 0 && beginA < ta)	beginA++;
		while(B[beginB].beginTime < 0 && beginB < tb)	beginB++;
		if(beginA >= ta || beginB >= tb)	break;
		if(A[beginA].beginTime <= B[beginB].beginTime)
		{
			resA++;
			A[beginA].beginTime = -1;
			TrainGo(1, beginB, A[beginA].endTime + turnTime, beginA);
		}else
		{
			resB++;
			B[beginB].beginTime = -1;
			TrainGo(0, beginA, B[beginB].endTime + turnTime, beginB);
		}
	}
	while(beginA < ta)
	{
		if(A[beginA].beginTime >= 0)	resA++;
		beginA++;
	}
	while(beginB < tb)
	{
		if(B[beginB].beginTime >= 0)	resB++;
		beginB++;
	}
}
void Initialize()
{
	sort(A, A+ta, MyCMP);
	sort(B, B+tb, MyCMP);
	resA = 0;
	resB = 0;
}
int main()
{
	int t = 0;

	scanf("%d", &t);
	for(int i = 1; i <= t; i++)
	{
		InputData();
		Initialize();
		Process();
		printf("Case #%d: %d %d\n", i, resA, resB);
	}
	return 0;
}