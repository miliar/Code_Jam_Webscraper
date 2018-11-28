#include <stdio.h>
#include <algorithm>

class Event
{
public:
	static const int arrive = 0;
	static const int leave = 1;
	int type;
	int place;
	int time;
	bool operator < (Event e)
	{
		if (time != e.time)
			return time < e.time;
		return type < e.type;
	}
};

Event ar[1000];
int size;

void push(Event e)
{
	ar[size++] = e;
}


void solve(int test_case)
{
	int T;
	size = 0;
	scanf("%d", &T);
	int na, nb;
	scanf("%d%d", &na, &nb);
	Event dummy;
	for(int i = 0; i < na; i++)
	{
		int t1,t2,d1,d2;
		scanf("%d:%d", &d1, &d2);
		t1 = d1*60+d2;
		scanf("%d:%d", &d1, &d2);
		t2 = d1*60+d2;

		dummy.place = 0;
		dummy.type = dummy.leave;
		dummy.time = t1;
		push(dummy);
		dummy.place = 1;
		dummy.type = dummy.arrive;
		dummy.time = t2 + T;
		push(dummy);
	}
	for(int i = 0; i < nb; i++)
	{
		int t1,t2,d1,d2;
		scanf("%d:%d", &d1, &d2);
		t1 = d1*60+d2;
		scanf("%d:%d", &d1, &d2);
		t2 = d1*60+d2;
		dummy.place = 1;
		dummy.type = dummy.leave;
		dummy.time = t1;
		push(dummy);
		dummy.place = 0;
		dummy.type = dummy.arrive;
		dummy.time = t2 + T;
		push(dummy);
	}
	std::sort(ar, ar+size);
	int cur[2] = {0,0}, max[2] = {0,0};
	for(int i = 0; i < size; i++)
	{
		if (ar[i].type == ar[i].arrive)
			cur[ar[i].place] ++;
		else
		{
			cur[ar[i].place] --;
			if (cur[ar[i].place] == -1)
			{
				cur[ar[i].place] = 0;
				max[ar[i].place] ++;
			}
		}
	}
	printf("Case #%d: %d %d\n", test_case, max[0], max[1]);
}



int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n;
	scanf("%d", &n);
	for(int i = 1; i <= n; i++)
		solve(i);
	return 0;
}
