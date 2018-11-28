#include <stdio.h>
#include <functional>
#include <bitset>
#include <math.h>
#include <time.h>
#include <stdlib.h>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <sstream>
#include <queue>
#include <bitset>
#include <string.h>
using namespace std;

int C, D, N;
map<pair<char, char>, char> combine;
map<char, char> opposed;
string s;

void readCase()
{
	combine.clear();
	opposed.clear();
	scanf("%d", &C);
	for(int i = 1; i <= C; i++) 
	{
		char A, B, C;
		scanf(" %c%c%c", &A, &B, &C);
		combine[make_pair(A, B)] = C;
		combine[make_pair(B, A)] = C;
	}
	scanf("%d", &D);
	for(int i = 1; i <= D; i++) 
	{
		char A, B;
		scanf(" %c%c", &A, &B);
		opposed[A] = B;
		opposed[B] = A;
	}
	scanf("%d", &N);
	s.clear();
	s.reserve(N);
	for(int i = 1; i <= N; i++) 
	{
		char A;
		scanf(" ");
		scanf("%c", &A);
		s += A;
	}	
}

void solve()
{
	vector<char> res;
	map<char, int> oppose;
	res.reserve(1000);
	char pred = 0;
	for(int i = 0; i < N; i++)
	{
		char cur = s[i];
		if(combine.count(make_pair(pred, cur)))
		{
			res.pop_back(), res.push_back(combine[make_pair(pred, cur)]);
			oppose[opposed[pred]]--;
			pred = 0;
			continue;
		}
		if(oppose[cur] > 0)
		{
			res.clear();
			oppose.clear();
			pred = 0;
			continue;
		}
		res.push_back(cur);
		oppose[opposed[cur]]++;
		pred = cur;
	}
	

	printf("[");
	for(int i = 0; i < res.size(); i++)
	{
		if(i) printf(", ");
		printf("%c", res[i]);
	}
	printf("]");
}

int main()
{
	//string fname = "./test/B-example.in";
	string fname = "./test/B-small-attempt2.in";
	//string fname = "./test/B-large.in";
	
	freopen(fname.c_str(),"r",stdin);freopen((fname+".out").c_str(),"w",stdout);

	int analizeCase = -1;
	
	int T;
	scanf("%d", &T);
	for(int tCase = 1; tCase <= T; tCase++) {
		printf("Case #%d: ", tCase);
		readCase();
		if(analizeCase < 0 || analizeCase == tCase) solve();
		printf("\n");
		fflush(stdout);
	}
	return 0;
}

