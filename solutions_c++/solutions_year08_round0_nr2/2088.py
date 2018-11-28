#include <iostream>
#include <queue>
using namespace std;

struct TimeTable {
	int Begin, End, Dir;
	TimeTable::TimeTable(int a,int b,int c){Begin=a;End=b;Dir=c;};
	bool operator< (const TimeTable& x) const {return Begin > x.Begin; }
};

struct NextTrain {
	int time;
	bool operator< (const NextTrain& x) const {return time > x.time;}
	};
	
	
int main (int argc, char * const argv[]) {
    int cases;
    std::cin >> cases;
	for (int testcase=1;testcase<=cases;testcase++)
	{
		priority_queue<TimeTable> tt;
		int turntime;
		std::cin >> turntime;
		int NA, NB;
		std::cin >> NA >> NB;
		for (int i=1; i<=(NA+NB);i++){
			int BH,BM,EH,EM;
			char t;
			std::cin >> BH>>t>>BM>>EH>>t>>EM;
			
			int start=BH*60+BM;
			int end=EH*60+EM+turntime;
			//printf ("%i %i %i:%i %i:%i",start,end,BH,BM,EH,EM);
			//if (i<=NA) {printf (" A->B\n");}
			//else {printf (" b->a\n");};
			
			tt.push(TimeTable(start,end,i<=NA?0:1));
		}
		int Dir[2];Dir[0]=0;Dir[1]=0;
		priority_queue<NextTrain> NextAvail[2];
		while (!tt.empty()){
			TimeTable t=tt.top(); tt.pop();
			NextTrain nextTrain;
			nextTrain.time=t.End;
			//printf("%i %i %i",t.Begin,t.End,t.Dir);
			//printf(" NxtAvail: ");
			//for (int t=0;t<2;t++){if (NextAvail[t].empty()) {printf("99999 ");}else{printf ("-%i-",NextAvail[t].top());};};
			if (NextAvail[t.Dir].empty() ){
				Dir[t.Dir]++;
			//	printf(" +E ");
			} else if (NextAvail[t.Dir].top().time<=t.Begin){
				NextAvail[t.Dir].pop();
			//	printf(" -- ");
			} else {
				Dir[t.Dir]++;
			//	printf(" +N ");
			}
			NextAvail[t.Dir==1?0:1].push(nextTrain);
			//for (int t=0;t<2;t++){if (NextAvail[t].empty()) {printf("99999 ");}else{printf ("-%i-",NextAvail[t].top());};};
			
			//printf("Trains: %i %i\n",Dir[0],Dir[1]);
			
		}
		printf("Case #%i: %i %i\n",testcase,Dir[0],Dir[1]);
		//for (int i=0;i<2;i++) while (!NextAvail[i].empty()) NextAvail[i].pop();
		
	}
}