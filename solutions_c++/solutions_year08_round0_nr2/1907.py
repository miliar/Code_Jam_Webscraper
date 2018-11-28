#include <stdio.h>
#include <vector>
#include <queue>
#include <algorithm>

#define A_TO_B -1
#define B_TO_A 1
#define HOUR_MINUTES 60


using namespace std;

typedef struct ttime {
	int hh;
	int mm;

	ttime(int hh, int mm){
		this->hh = hh;
		this->mm = mm;
	}
	
	ttime(){
	}

	ttime operator+(ttime rhs){
		int add_hours = ( mm + rhs.mm ) / HOUR_MINUTES ;
		int minutes =  ( mm + rhs.mm ) % HOUR_MINUTES ;
		int hours = hh + rhs.hh + add_hours;

		return ttime(hours, minutes);
	}
};

typedef struct tt_entry {
	ttime departure;
	ttime arrival;
	int dir;

	tt_entry(ttime departure, ttime arrival, int dir){
		this->departure = departure;
		this->arrival = arrival;
		this->dir = dir;
	}


};

typedef vector<tt_entry>::iterator ttIt;

bool cmp( ttime lhs, ttime rhs ){
	if (lhs.hh < rhs.hh) return true;
	if (lhs.hh > rhs.hh) return false;
	if (lhs.mm < rhs.mm) return true;
	if (lhs.mm > rhs.mm) return false;

	return true;
}

struct cmpTime {

	bool operator()( ttime lhs, ttime rhs ){
		if (lhs.hh < rhs.hh) return false;
		if (lhs.hh > rhs.hh) return true;
		if (lhs.mm < rhs.mm) return false;
		if (lhs.mm > rhs.mm) return true;

		return false;
	}
};

bool cmpEntries(tt_entry lhs, tt_entry rhs){
	return cmp(lhs.departure, rhs.departure);
}

vector<tt_entry> schedule;

pair<int, int> count_trains(int T, int nA, int nB){	
	int 			lResult = 0;
	int				rResult = 0;

	ttime 			turnaround_time(0, T);
	
	priority_queue<ttime, vector<ttime>, cmpTime> aPQ;
	priority_queue<ttime, vector<ttime>, cmpTime> bPQ;

	sort(schedule.begin(), schedule.end(), cmpEntries);

	for (ttIt scheduleIt = schedule.begin(); scheduleIt != schedule.end();
			++scheduleIt){
		tt_entry nextEntry = *scheduleIt;


		bool properTrain = false;

		if ( nextEntry.dir == A_TO_B ){
			if (!aPQ.empty()){
				ttime t = aPQ.top();

				if (cmp(t, nextEntry.departure)){
					properTrain = true;
					aPQ.pop();
				}
			}
			
			if (!properTrain)
				lResult++;

			bPQ.push(nextEntry.arrival + turnaround_time);			
		}

		if ( nextEntry.dir == B_TO_A ){
			if (!bPQ.empty()){
				ttime t = bPQ.top();

				if (cmp(t, nextEntry.departure)){
					properTrain = true;
					bPQ.pop();
				}
			}
			
			if (!properTrain)
				rResult++;

			aPQ.push(nextEntry.arrival + turnaround_time);			
		}

	}

	return make_pair(lResult, rResult);
}

int main(){
	int				T, nA, nB;
	int 			nCases;
	int				i, j;
	pair<int,int>	result;
	int				caseCounter = 1;

	scanf("%d", &nCases);

	while (nCases--){
		int a_hh, a_mm, b_hh, b_mm;
		
		schedule.clear();

		scanf("%d %d %d", &T, &nA, &nB);

		for ( i = 0; i < nA; i++ ){
			scanf("%d:%d %d:%d\n", &a_hh, &a_mm, &b_hh, &b_mm);	
			schedule.push_back(tt_entry(ttime(a_hh, a_mm), ttime(b_hh, b_mm), A_TO_B));
		}

		for ( i = 0; i < nB; i++ ){
			scanf("%d:%d %d:%d\n", &b_hh, &b_mm, &a_hh, &a_mm);	
			schedule.push_back(tt_entry(ttime(b_hh, b_mm), ttime(a_hh, a_mm), B_TO_A));
		}

		result = count_trains(T, nA, nB);	
		
		printf("Case #%d: %d %d\n", caseCounter, result.first, result.second);

		caseCounter++;
	}

	return 0;
}
