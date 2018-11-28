#include <algorithm>
#include <fstream>
#include <string>
#include <queue>
#include <set>
#include <stack>
#include <map>
#include <sstream>
#include <iostream>
#include <cmath>
using namespace std;

typedef unsigned int uint;
typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pI;
typedef pair<string,int> pSI;
typedef pair<int,string> pIS;

#define FOR(i,n) for(int i=0, upTo##i=n; i<upTo##i; ++i)
#define REVFOR(i,n) for(int i=(n)-1; i>=0; --i)
#define FOR2(i,b,n) for(int i=b; i<(n); ++i)
#define REVFOR2(i,b,n) for(int i=(n)-1; i>=b; --i)
#define SC(i) scanf("%d", i)
#define ALL(C) (C).begin(), (C).end()
#define MIN(C) *min_element(ALL(C))
#define MAX(C) *max_element(ALL(C))
#define A first
#define B second

struct train {
	int start, end;
	//int startAt;

	train(int s, int e) : start(s), end(e) {} 

	bool operator<(const train &t) const {
		if (start!=t.start) return start < t.start;
		return end < t.end;
	}
};


const int CURR_A = 0;
const int CURR_B = 1;

void find(int currTime, vector<train> &BtoA, vector<train> &AtoB, int curr, int turnaround) {
	if (curr == CURR_A) {
		vector<train>::iterator it = lower_bound(ALL(AtoB), train(currTime,0));
		if (it != AtoB.end()) {
			currTime = it->end + turnaround;
			AtoB.erase(it);
			find(currTime, BtoA, AtoB, CURR_B, turnaround);
		}
	} else {
		vector<train>::iterator it = lower_bound(ALL(BtoA), train(currTime,0));
		if (it != BtoA.end()) {
			currTime = it->end + turnaround;
			BtoA.erase(it);
			find(currTime, BtoA, AtoB, CURR_A, turnaround);
		}
	}
}

int main(void)
{
	int n; SC(&n);
	FOR(i,n) {
		int t,na,nb; scanf("%d %d %d", &t, &na, &nb);
		vector<train> AtoB, BtoA;
		FOR(j,na) {
			int hStart,mStart,hEnd,mEnd;
			scanf("%d:%d %d:%d", &hStart, &mStart, &hEnd, &mEnd);
			AtoB.push_back(train(hStart*60+mStart, hEnd*60+mEnd));
		}
		FOR(j,nb) {
			int hStart,mStart,hEnd,mEnd;
			scanf("%d:%d %d:%d", &hStart, &mStart, &hEnd, &mEnd);
			BtoA.push_back(train(hStart*60+mStart, hEnd*60+mEnd));
		}
		sort(ALL(BtoA));
		sort(ALL(AtoB));

		int trainA=0, trainB=0;

		while(!BtoA.empty() && !AtoB.empty()) {
			if (BtoA.begin()->start < AtoB.begin()->start) {
				find(0, BtoA, AtoB, CURR_B, t);
				++trainB;
			} else {
				find(0, BtoA, AtoB, CURR_A, t);
				++trainA;
			}
		}

		trainA += AtoB.size();
		trainB += BtoA.size();

		printf("Case #%d: %d %d\n", i+1, trainA, trainB);
	}

    return 0;
}
