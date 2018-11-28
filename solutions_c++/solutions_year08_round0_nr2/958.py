// test.cpp : Defines the entry point for the console application.
//
//
#include "stdafx.h"

#include "iostream"
#include "math.h"
#include "string"

#include <algorithm> 
#include <vector>
#include <deque>
#include <map>
#include <set>
#include <climits>

using namespace std;

short casenum;
short caseindex;

int t;
int na;
int nb;

int ansa;
int ansb;

vector<short> stationa;
vector<short> stationb;
vector<short>::iterator it;

typedef struct  
{
	short from;
	short to;
	bool  startfroma;
}stimetable;

stimetable timelist[201];

int cmp( const void *a , const void *b ) 
{ 
	stimetable *c = (stimetable *)a; 

	stimetable *d = (stimetable *)b; 

	if(c->from != d->from)
		return c->from - d->from; 
	else
		return c->to - d->to; 
} 

void doing()
{
	int i;

	qsort(timelist, na+nb+1, sizeof(stimetable), cmp);

	ansa = 0;
	ansb = 0;
	stationa.clear();
	stationb.clear();

	for (i=1; i<=na+nb; ++i) {
		if (timelist[i].startfroma) {
			if (0 == stationa.size()) {
				++ansa;
				it = stationb.begin();
				while ((it != stationb.end()) && (*it<timelist[i].to+t)) {
					++it;
				}
				stationb.insert(it, timelist[i].to+t);
			}
			else if (*(stationa.begin()) > timelist[i].from){
				++ansa;
				it = stationb.begin();
				while ((it != stationb.end()) && (*it<timelist[i].to+t)) {
					++it;
				}
				stationb.insert(it, timelist[i].to+t);
			}
			else {
				//stationa.pop_front();
				stationa.erase(stationa.begin());
				it = stationb.begin();
				while ((it != stationb.end()) && (*it<timelist[i].to+t)) {
					++it;
				}
				stationb.insert(it, timelist[i].to+t);
			}
		}
		else {
			if (0 == stationb.size()) {
				++ansb;
				it = stationa.begin();
				while ((it != stationa.end()) && (*it<timelist[i].to+t)) {
					++it;
				}
				stationa.insert(it, timelist[i].to+t);
			}
			else if (*(stationb.begin()) > timelist[i].from){
				++ansb;
				it = stationa.begin();
				while ((it != stationa.end()) && (*it<timelist[i].to+t)) {
					++it;
				}
				stationa.insert(it, timelist[i].to+t);
			}
			else {
				//stationb.pop_front();
				stationb.erase(stationb.begin());
				it = stationa.begin();
				while ((it != stationa.end()) && (*it<timelist[i].to+t)) {
					++it;
				}
				stationa.insert(it, timelist[i].to+t);
			}
		}
	}

	cout << "Case #" << caseindex << ": " << ansa << " " << ansb << endl;
}


int main()
{
	int i;

	int time;
	int hour, minute;

	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);

	while (cin>>casenum) {
		for (caseindex = 1; caseindex <= casenum; ++caseindex) {
			cin >> t >> na >> nb;
			for (i=1; i<=na; ++i) {
				scanf("%d:%d", &hour, &minute);
				time = hour*60 + minute;
				timelist[i].from = time;
				scanf("%d:%d", &hour, &minute);
				time = hour*60 + minute;
				timelist[i].to = time;
				timelist[i].startfroma = true;
			}
			for (i=na+1; i<=na+nb; ++i) {
				scanf("%d:%d", &hour, &minute);
				time = hour*60 + minute;
				timelist[i].from = time;
				scanf("%d:%d", &hour, &minute);
				time = hour*60 + minute;
				timelist[i].to = time;			
				timelist[i].startfroma = false;
			}
			doing();
		}
	}

	return 0;
}
