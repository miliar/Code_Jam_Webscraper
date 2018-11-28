//Maked by diver_ru, maked with love^^
#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <string>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>

#ifdef ONLINE_JUDGE
//#include <iostream>
FILE *fi = stdin, *fo = stdout;
#else
#include <fstream>

//std::ifstream cin("input.txt");
//std::ofstream cout("output.txt");
FILE *fi = fopen("input.txt", "r"), *fo = fopen("output.txt", "w");
#endif
using namespace std;

const int	PLACE_A = 0,
			PLACE_B = 1;

int t;

struct TimeItem{
	int start, finish;
	int place;
	bool operator < (const TimeItem &b) const{
		return (start < b.start);
	}
};

priority_queue<int, vector<int>, greater<int> > trains[2];

vector<TimeItem> items;

int answer[2];

int getTime()
{
	int h, m;
	fscanf(fi, "%d:%d", &h, &m);
	return (h * 60 + m);
}

void readData()
{
	items.clear();
	int na, nb;
	fscanf(fi, "%d", &t);
	fscanf(fi, "%d%d\n", &na, &nb);
	TimeItem item;
	for (int i = 0; i < na; ++i){
		item.start = getTime();
		item.finish = getTime();
		item.place = PLACE_A;
		items.push_back(item);
	}
	for (int i = 0; i < nb; ++i){
		item.start = getTime();
		item.finish = getTime();
		item.place = PLACE_B;
		items.push_back(item);
	}
}

void solve()
{
	sort(items.begin(), items.end());
	memset(answer, 0, sizeof answer);
	for (int i = 0; i <= 1; ++i)
		trains[i] = priority_queue<int, vector<int>, greater<int> >();
	for (int i = 0; i < (int)items.size(); ++i){
		int place = items[i].place;
		if (trains[place].empty() || trains[place].top() > items[i].start){
			trains[place].push(-1);
			++answer[place];
		}
		trains[place].pop();
		trains[1 - place].push(items[i].finish + t);
	}
}

void writeResult()
{
	fprintf(fo, "%d %d\n", answer[0], answer[1]);
}

int main()
{
	int n;
	fscanf(fi, "%d\n", &n);
	for (int i = 1; i <= n; ++i){
		readData();
		solve();
		fprintf(fo, "Case #%d: ", i);
		writeResult();
	}
	return 0;
}