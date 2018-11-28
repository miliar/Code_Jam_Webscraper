#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>

using namespace std;

struct Time
{
	int start, end;
};
bool operator <(Time a, Time b)
{
	if(a.start<b.start || (a.start==b.start&&a.end<b.end))
		return true;
	return false;
}

int n, na, nb, tour;
int main()
{
	Time a[100], b[100];
	scanf("%d", &n);
	char t1[6], t2[6];

	for(int r=1; r<=n; r++)
	{
		int i=0, j=0, numa=0, numb=0;
		scanf("%d", &tour);
		scanf("%d %d", &na, &nb);
		for(i=0; i<na; i++)
		{
			scanf("%s %s", &t1, &t2);
			a[i].start=int(int(t1[0]-'0')*600+int(t1[1]-'0')*60+int(t1[3]-'0')*10+int(t1[4]-'0'));
			a[i].end=int(int(t2[0]-'0')*600+int(t2[1]-'0')*60+int(t2[3]-'0')*10+int(t2[4]-'0'))+tour;
		}
		for(i=0; i<nb; i++)
		{
			scanf("%s %s", &t1, &t2);
			b[i].start=int(int(t1[0]-'0')*600+int(t1[1]-'0')*60+int(t1[3]-'0')*10+int(t1[4]-'0'));
			b[i].end=int(int(t2[0]-'0')*600+int(t2[1]-'0')*60+int(t2[3]-'0')*10+int(t2[4]-'0'))+tour;
		}
		priority_queue<int, vector<int>, greater<int> > qa;
		priority_queue<int, vector<int>, greater<int> > qb;
		if(na>1)
			sort(a, a+na);
		if(nb>1)
			sort(b, b+nb);
		i=0, j=0;
next:		
		for(; i<na&&j<nb; )
		{
			if(a[i].start<b[j].start)
			{
				if(qa.empty() || (!qa.empty()&&qa.top()>a[i].start))
				{
					numa++;
					qb.push(a[i].end);
					i++;
					goto next;
				}
				if(!qa.empty() && qa.top()<=a[i].start)
				{
					qa.pop();
					qb.push(a[i].end);
				}
				i++;
				goto next;
			}
			if(a[i].start>b[j].start)
			{
				if(qb.empty() || (!qb.empty()&&qb.top()>b[j].start))
				{
					numb++;
					qa.push(b[j].end);
					j++;
					goto next;
				}
				if(!qb.empty() && qb.top()<=b[j].start)
				{
					qb.pop();
					qa.push(b[j].end);
				}
				j++;
				goto next;
			}
			if(a[i].start==b[j].start)
			{
				if(qa.empty() || (!qa.empty()&&qa.top()>a[i].start))
				{
					numa++;
					qb.push(a[i].end);
				}
				if(!qa.empty() && qa.top()<=a[i].start)
				{
					qa.pop();
					qb.push(a[i].end);
				}
				if(qb.empty() || (!qb.empty()&&qb.top()>b[j].start))
				{
					numb++;
					qa.push(b[j].end);
				}
				if(!qb.empty() && qb.top()<=b[j].start)
				{
					qb.pop();
					qa.push(b[j].end);
				}
				i++, j++;
				goto next;
			}
		}
		if(i<na)
		{
			while(!qa.empty() && i<na)
			{
				if(a[i].start>=qa.top())
				{
					qa.pop();
					i++;
					continue;
				}
				if(a[i].start<qa.top())
				{
					numa++;
					i++;
				}
			}
			if(i<na)
				numa+=na-i;
		}
			
		if(j<nb)
		{
			while(!qb.empty() && j<nb)
			{
				if(b[j].start>=qb.top())
				{
					qb.pop();
					j++;
					continue;
				}
				if(b[j].start<qb.top())
					numb++;
				j++;
			}
			if(j<nb)
				numb+=nb-j;
		}
		printf("Case #%d: %d %d\n", r, numa, numb);

	}
	return 0;
}