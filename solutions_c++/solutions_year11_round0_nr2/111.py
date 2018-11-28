/*
	ID: lkq19921
	PROG: b
	LANG: C++
*/
#include <iostream>
#include <string.h>
#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#define INF 2111222333
#define MAX(a, b)    ((a) > (b) ? (a) : (b))
#define MIN(a, b)    ((a) < (b) ? (a) : (b))
#define eps 1e-8
#define MAXN 105
#define DEBUG

using namespace std;

map<pair<char, char>, char> combine;
map<pair<char, char>, int> opposite;
pair<char, char> p;
string ori, res;
int c, d, n;

void Solve()
{
	int i, j, state;
	string s;
	combine.clear();
	opposite.clear();
	res.clear();
	scanf("%d", &c);
	for (i = 0; i < c; i++)
	{
		cin >> s;
		p = make_pair(s[0], s[1]);
		combine[p] = s[2];
	}
	scanf("%d", &d);
	for (i = 0; i < d; i++)
	{
		cin >> s;
		p = make_pair(s[0], s[1]);
		opposite[p]++;
	}
	scanf("%d", &n);
	cin >> ori;
	for (i = 0; i < ori.size(); i++)
	{
		state = 0;
		res.push_back(ori[i]);
		if (res.size() > 1)
		{
			p = make_pair(res[res.size() - 1], res[res.size() - 2]);
			//printf("-pair is %c %c\n", p.first, p.second);
			if (combine.find(p) != combine.end())
				state = 1;
			else
			{
				p = make_pair(res[res.size() - 2], res[res.size() - 1]);
				if (combine.find(p) != combine.end())
					state = 1;
			}
			if (state == 1)
			{
				//printf("Here\n");
				res.erase(res.size() - 1);
				res.erase(res.size() - 1);
				res.push_back(combine[p]);
				state = 1;
				//cout<<"\t"<<res<<endl;
			}
		}
		if (res.size() > 1 && state == 0)
		{
			for (j = 0; j < res.size() - 1; j++)
			{
				p = make_pair(res[j], *(--res.end()));
				//printf("--pair is %c %c\n", p.first, p.second);
				if (opposite.find(p) != opposite.end())
					break;
				p = make_pair(*(--res.end()), res[j]);
				//printf("--pair is %c %c\n", p.first, p.second);
				if (opposite.find(p) != opposite.end())
					break;
			}
			if (j != res.size() - 1)
			{
				res.clear();
				//printf("Clear it! %d\n", res.size());
			}
		}
	}
	//cout << res << endl;
	printf("[");
	for (i = 0; i < res.size(); i++)
	{
		if (i > 0)
			printf(", ");
		printf("%c", res[i]);
	}
	printf("]\n");
}

int main()
{
	#ifdef DEBUG
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	#endif
	int t, f;
	scanf("%d", &t);
	for (f = 1; f <= t; f++)
	{
		printf("Case #%d: ", f);
		Solve();
	}
	return 0;
}


