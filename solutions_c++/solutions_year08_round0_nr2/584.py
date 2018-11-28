#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

const int MAXN = 110;

int t;
int na, nb;

struct Train
{
	int st, end;
	int type, cnt;
};
Train a[MAXN], b[MAXN];

int tim(char x[6])
{
	return (x[0]-'0')*600+(x[1]-'0')*60+(x[3]-'0')*10+(x[4]-'0');	
}

void input()
{
	scanf("%d%d%d", &t, &na, &nb);
	for (int i=0; i<na; i++)
	{
		char x[6], y[6];
		scanf("%s%s", x, y);
		a[i].st = tim(x);
		a[i].end = tim(y)+t;	
	}
	for (int i=0; i<nb; i++)
	{
		char x[6], y[6];
		scanf("%s%s", x, y);
		b[i].st = tim(x);
		b[i].end = tim(y)+t;	
	}
}

Train s[2*MAXN];

inline bool cmp(Train a, Train b)
{
	return a.st < b.st;	
}

void solve()
{
	for (int i=0; i<na; i++)
	{
		s[i].type = 0;
		s[i].cnt = 0;
		s[i].st = a[i].st;
		s[i].end = a[i].end;	
	}
	for (int i=0; i<nb; i++)
	{
		int j = i+na;
		s[j].type = 1;
		s[j].cnt = 0;
		s[j].st = b[i].st;
		s[j].end = b[i].end;	
	}
	sort(s, s+na+nb, cmp);
	int resA = 0, resB = 0;
	int curA = 0, curB = 0;
	for (int i=0; i<na+nb; i++)
	{
		if (s[i].type == 0)
		{
			curA += s[i].cnt;
			if (curA == 0)
				resA++;	
			else
				curA--;
			for (int j=0; j<na+nb; j++)
				if (s[j].type == 1 && s[j].st >= s[i].end)
				{
					s[j].cnt++;
					break;	
				}
		}
		else{
			curB += s[i].cnt;
			if (curB == 0)
				resB++;
			else
				curB--;
			for (int j=0; j<na+nb; j++)
				if (s[j].type == 0 && s[j].st >= s[i].end)
				{
					s[j].cnt++;
					break;	
				}
		}	
	}
	printf(" %d %d\n", resA, resB);
}

int main()
{
	//freopen("B-large.in", "r", stdin);
	//freopen("B-large.out", "w", stdout);
	int cas;
	scanf("%d", &cas);
	for (int kth=1; kth<=cas; kth++)
	{
		input();
		printf("Case #%d:", kth);
		solve();	
	}	
	return 0;
}
