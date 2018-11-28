#include <stdio.h>
#include <stdlib.h>
#include <memory.h>

#include <string>
#include <vector>
#include <algorithm>
using namespace std;

typedef struct time
{
	int hour;
	int minute;
	time& operator=(const time& t)
	{
		hour = t.hour;
		minute = t.minute;
		return *this;
	}
}TIME;
typedef struct timePair
{
	TIME depart;
	TIME arrive;
	timePair& operator=(const timePair& tp)
	{
		depart = tp.depart;
		arrive = tp.arrive;
		return *this;
	}

}TIMEPAIR;

typedef pair<char *, char *> TIMESTRING;

void readTime(vector<TIMESTRING>& timestring, vector<TIMEPAIR >& time)
{
	int i = 0;
	int size = timestring.size();
	for(; i < size; i++)
	{
		time[i].depart.hour = atoi(timestring[i].first);
		time[i].depart.minute = atoi(timestring[i].first + 3);
		time[i].arrive.hour = atoi(timestring[i].second);
		time[i].arrive.minute = atoi(timestring[i].second + 3);
	}
}
bool operator< (const TIME& time1, const TIME& time2)
{
	if(time1.hour == time2.hour)
		return time1.minute < time2.minute;
	return time1.hour < time2.hour;
}

bool operator<= (const TIME& time1, const TIME& time2)
{
	if(time1.hour == time2.hour)
		return time1.minute <= time2.minute;
	return time1.hour <= time2.hour;
}

bool operator< (const TIMEPAIR& tp1, const TIMEPAIR& tp2)
{
	if(tp1.depart.hour == tp2.depart.hour && tp1.depart.minute == tp2.depart.minute )	// 若离开时间相等
		return tp1.arrive < tp2.arrive;
	return tp1.depart < tp2.depart;
}

bool operator<= (const TIMEPAIR& tp1, const TIMEPAIR& tp2)
{
	if(tp1.depart.hour == tp2.depart.hour && tp1.depart.minute == tp2.depart.minute )	// 若离开时间相等
		return tp1.arrive <= tp2.arrive;
	return tp1.depart <= tp2.depart;
}

void addTime(TIME& time, int penalty)
{
	if(!(time.minute + penalty < 60))
	{
		time.minute += penalty - 60;
		time.hour++;
	}
	else
		time.minute += penalty;
}

void nextCursor(int& cursor,int * arrange, int size)
{
	while(*(arrange + cursor) && cursor < size) // 若该时间已经被安排
		cursor++;
}

void findMatch(vector<TIMEPAIR>& atob, vector<TIMEPAIR>& btoa,
			   TIME& t, int * arrangeA, int * arrangeB, int atB, int ta)  // 1表示在B站
{
	int i;
	if(atB)
	{
		for(i = 0; i < btoa.size(); i++)
		{
			if( !(*(arrangeB + i)) && t <= btoa[i].depart ) // 没有安排且时间允许
			{
				*(arrangeB + i) = 1; // 安排
				t = btoa[i].arrive;  // 更新时间
				break;
			}
		}
		if(i == btoa.size() )
			return;
		else
		{
			addTime(t, ta);
			return findMatch(atob, btoa, t, arrangeA, arrangeB, 0, ta);
		}
	}
	else	// at A
	{
		for(i = 0; i < atob.size(); i++)
		{
			if( !(*(arrangeA + i)) && t <= atob[i].depart )
			{
				*(arrangeA + i) = 1;
				t = atob[i].arrive;
				break;
			}
		}
		if( i == atob.size() )
			return ;
		else
		{
			addTime(t, ta);
			return findMatch(atob, btoa, t, arrangeA, arrangeB, 1, ta);
		}
	}
}
int main()
{
	FILE * fin, * fout;
	fin = fopen("C:\\B-small.in", "r");
	fout = fopen("C:\\B-small.out", "w");
	int caseNum;
	fscanf(fin, "%d\n", &caseNum);
	int num = 0;
	int turnaround, NA, NB, i, j;
	vector<pair<char *, char *> > atob, btoa;
	vector<TIMEPAIR> tatob, tbtoa;
	int * arrangeA, * arrangeB;
	int numA, numB, cursorA, cursorB;
	TIME t;
	for(; num < caseNum; num++)
	{
		fscanf(fin, "%d\n", &turnaround);
		fscanf(fin, "%d %d\n", &NA, &NB);
		atob = vector<pair<char *, char *> >(NA);
		btoa = vector<pair<char *, char *> >(NB);
		for(i = 0; i < NA; i++)
		{
			atob[i].first = (char *)malloc(sizeof(char) * 5);
			atob[i].second = (char *)malloc(sizeof(char) * 5);
			fscanf(fin, "%s %s\n", atob[i].first, atob[i].second);
		}
		for(i = 0; i < NB; i++)
		{
			btoa[i].first = (char *)malloc(sizeof(char) * 5);
			btoa[i].second = (char *)malloc(sizeof(char) * 5);
			fscanf(fin, "%s %s\n", btoa[i].first, btoa[i].second);
		}
		tatob = vector<TIMEPAIR >(NA);
		tbtoa = vector<TIMEPAIR >(NB);
		readTime(atob, tatob);
		readTime(btoa, tbtoa);
		// 排序
		sort(tatob.begin(), tatob.end());
		sort(tbtoa.begin(), tbtoa.end());
		numA = numB = 0;
		arrangeA = (int *)malloc(sizeof(int) * NA);
		arrangeB = (int *)malloc(sizeof(int) * NB);
		memset(arrangeA, 0, sizeof(int) * NA);
		memset(arrangeB, 0, sizeof(int) * NB);
		cursorA = cursorB = 0;
		while( cursorA < NA && cursorB < NB)
		{
			if(tatob[cursorA] <= tbtoa[cursorB])
			{
				arrangeA[cursorA] = 1;
				numA++;
				t = tatob[cursorA].arrive;
				addTime(t, turnaround);
				findMatch(tatob, tbtoa, t, arrangeA, arrangeB, 1, turnaround); // 1表示在B站
			}
			else
			{
				arrangeB[cursorB] = 1;
				numB++;
				t = tbtoa[cursorB].arrive;
				addTime(t, turnaround);
				findMatch(tatob, tbtoa, t, arrangeA, arrangeB, 0, turnaround); // 0表示在A站
			}
			nextCursor(cursorA, arrangeA, NA);
			nextCursor(cursorB, arrangeB, NB);
		}
		while(cursorA < NA)
		{
			if( !(*(arrangeA + cursorA)) )
				numA++;
			cursorA++;
		}
		while(cursorB < NB)
		{
			if( !(*(arrangeB + cursorB)) )
				numB++;
			cursorB++;
		}
		// 输出
		fprintf(fout, "Case #%d: %d %d\n", num + 1, numA, numB);
	}
	fclose(fin);
	fclose(fout);
	return 0;
}