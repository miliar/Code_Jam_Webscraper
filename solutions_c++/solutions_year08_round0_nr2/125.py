#include<string>
#include<vector>
#include<set>
#include<stdio.h>
using namespace std;

struct TrainTime {
	int departure;
	int arrival;
};

struct TimeLess { 
	bool operator()(const TrainTime &A, const TrainTime &B) const 
	{ 
		if(A.departure != B.departure)
			return A.departure < B.departure; 
		else return A.arrival < B.arrival;
	} 
}; 

int main()
{
	FILE *in = freopen("B-large.in","r",stdin);
	FILE *out = freopen("B-large.out","w",stdout);
	typedef multiset<TrainTime,TimeLess> Myset;
	int n,na,nb;
	int N,NA,NB,T;
	int HH,MM;
	TrainTime t;
	scanf("%d",&N);
	for(n=0;n<N;n++) {
		Myset timeTableA;
		Myset timeTableB;
		scanf("%d",&T);
		scanf("%d",&NA);
		scanf("%d",&NB);
		for(na=0;na<NA;na++) {
			scanf("%d:%d",&HH,&MM);
			t.departure = 60 * HH + MM;
			scanf("%d:%d",&HH,&MM);
			t.arrival = 60 * HH + MM;
			timeTableA.insert(t);
		}	
		for(nb=0;nb<NB;nb++) {
			scanf("%d:%d",&HH,&MM);
			t.departure = 60 * HH + MM;
			scanf("%d:%d",&HH,&MM);
			t.arrival = 60 * HH + MM;
			timeTableB.insert(t);
		}	
		int resultA=0;
		int resultB=0;
		while(!timeTableA.empty()&&!timeTableB.empty()) {
			int AB,cur;
			if((*timeTableA.begin()).departure <= (*timeTableB.begin()).departure) {
				resultA++;
				cur = (*timeTableA.begin()).arrival + T;
				AB = 2;
				timeTableA.erase(timeTableA.begin());
			} else {
				resultB++;
				cur = (*timeTableB.begin()).arrival + T;
				AB = 1;
				timeTableB.erase(timeTableB.begin());

			}
			while(1) {
				if(AB == 1) {
					t.departure = cur;
					t.arrival = 0;
					Myset::iterator it = timeTableA.upper_bound(t);
					if(it != timeTableA.end()) {
						cur = (*it).arrival + T;
						AB = 2;
						timeTableA.erase(it);
					} else break;
				} else {
					t.departure = cur;
					t.arrival = 0;
					Myset::iterator it = timeTableB.upper_bound(t);
					if(it != timeTableB.end()) {
						cur = (*it).arrival + T;
						AB = 1;
						timeTableB.erase(it);
					} else break;
				}
			}
		}
		if(!timeTableA.empty()) resultA += timeTableA.size(); 
		if(!timeTableB.empty()) resultB += timeTableB.size();
		printf("Case #%d: %d %d\n",n+1,resultA,resultB);
	}

	return 0;
}
