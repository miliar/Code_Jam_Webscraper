#include <iostream>
#include <fstream>
#include <iomanip>
#include <sstream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>

#define MAX 1024
#define PRIMES 1000100

using namespace std;
ifstream in; ofstream out;

vector <int> v[MAX];
set <int> cont[MAX];

int cnt[PRIMES];
int vis[PRIMES]; int col;

char a[PRIMES];
vector <int> primes;

void getPrimes(void)
{
	int i, c;

	memset(a, 0, sizeof(a));
	for (i=2; i<PRIMES; i++)
	{
		if (a[i] != 0) continue;
		
		primes.push_back(i);
		for (c=i+i; c<PRIMES; c+=i) a[c] = 1;
	}
}

void color(int cur)
{
	vis[cur] = col;
	for (int i=0; i<(int)v[cur].size(); i++)
		if (vis[v[cur][i]] == 0) color(v[cur][i]);
}

void doWork(int testNum)
{
	long long ans = 0;
	long long i, c, j, sq;
	long long A, B, P, cur;
	
	memset(cnt, 0, sizeof(cnt));
	for (i=0; i<MAX; i++) v[i].clear();
	for (i=0; i<MAX; i++) cont[i].clear();
	
	in >> A >> B >> P;
	
	if (A == 1) {ans = 1; A++;}
	for (i=A; i<=B; i++)
	{
		vector <int> facts;
		cur = i; sq = (long long)sqrt(i) + 1;
		
		for (c=0; c<(int)primes.size(); c++)
		{
			if (sq < primes[c]) break;
			if (cur % primes[c] == 0)
			{
				if (primes[c] >= P) facts.push_back(primes[c]);
				while (cur % primes[c] == 0) cur /= primes[c];
			}
			if (cur == 1) break;
		}
		if (cur != 1) facts.push_back(cur);
		if ((cur >= PRIMES) || (facts.size() == 0)) ans++;
		else
		{
			cnt[facts[0]]++;			
			for (c=0; c<(int)facts.size(); c++)
			{
				for (j=c+1; j<(int)facts.size(); j++)
				{
					if (cont[facts[c]].find(facts[j]) == cont[facts[c]].end())
					{
						cont[facts[c]].insert(facts[j]);
						v[facts[c]].push_back(facts[j]);
						v[facts[j]].push_back(facts[c]);
					}
				}
			}
		}
	}
	
	col = 1;
	memset(vis, 0, sizeof(vis));
	
	for (i=0; i<PRIMES; i++)
		if (cnt[i] != 0 && vis[i] == 0) {color(i); col++;}
	
	out << ans + col - 1 << endl;
	return;
}

int main(void)
{
	int tests, i;
	
	in.open("numberSets.in");
	out.open("numberSets.out");

	getPrimes();
	
	in >> tests;
	for (i=0; i<tests; i++)
	{
		out << "Case #" << i+1 << ": ";
		doWork(i+1);
	}
	
	return 0;
}
