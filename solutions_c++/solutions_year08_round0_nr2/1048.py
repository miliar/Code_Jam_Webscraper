#include <stdio.h>
#include <string.h>
#include <cstdio>
#include <algorithm>
#include <cctype>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <list>
#include <iostream>
#include <queue>
#include <utility>
using namespace std;
#define rep(x,from,to,step) for(int x=(from);x<(to);x+=(step))
#define all(x) (x).begin(),(x).end()

#define convert(a,b) ((b)+((a)*60))

typedef pair < int, int > bla;
list < int >trainsAvailable[2];
vector < bla > estacao[2];
int c[2];
int tmp[2];
unsigned int pos[2];
int t;

void clear()
{
	estacao[0].clear();
	estacao[1].clear();
	trainsAvailable[0].clear();
	trainsAvailable[1].clear();
	pos[0] = tmp[0] = c[0] = 0;
	pos[1] = tmp[1] = c[1] = 0;

}

void read()
{
	int dep;
	int na, nb;
	int t1, t2;
	scanf("%d", &t);
	scanf("%d%d", &na, &nb);
	while(na--) {
		scanf("%d:%d", &t1, &t2);
		dep = convert(t1, t2);
		scanf("%d:%d", &t1, &t2);
		estacao[0].push_back(bla(dep, convert(t1, t2) +t));
	}
	while(nb--) {
		scanf("%d:%d", &t1, &t2);
		dep = convert(t1, t2);
		scanf("%d:%d", &t1, &t2);
		estacao[1].push_back(bla(dep, convert(t1, t2) +t));
	}
	sort(all(estacao[0]));
	sort(all(estacao[1]));
}
bool getTrain(int sta,int time){
	list<int>::iterator begin=trainsAvailable[sta].begin(),end=trainsAvailable[sta].end();
	while(begin!=end){
		if(*begin<=time){
			trainsAvailable[sta].erase(begin);
			return true;
		}
		begin++;	
	}
	return false;
}


void doStuff()
{
	int from,to;
	bla times;
	for(pos[0] = pos[1] = 0; estacao[0].size()>pos[0] && estacao[1].size()>pos[1];) {
		if(estacao[0][pos[0]].first < estacao[1][pos[1]].first) {
			times=estacao[0][pos[0]];
			from=0;
			to=1;
			pos[0]++;
		}
		else {
			times=estacao[1][pos[1]];
			from=1;
			to=0;
			pos[1]++;
		}
		if(!getTrain(from,times.first))
			c[from]++;
		trainsAvailable[to].push_back(times.second);
	}
	for(; estacao[0].size()>pos[0] ;pos[0]++) 
		if(!getTrain(0,estacao[0][pos[0]].first))
			c[0]++;
	for(; estacao[1].size()>pos[1] ;pos[1]++) 
		if(!getTrain(1,estacao[1][pos[1]].first))
			c[1]++;

}

int main()
{
	int cases;
	int a=0;
	scanf("%d", &cases);
	while(a++<cases) {
		clear();
		read();
		doStuff();
		printf("Case #%d: %d %d\n",a,c[0],c[1]);
	}
	

}
