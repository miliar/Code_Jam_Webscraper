#include <cstdio>
#include <map>

using namespace std;

typedef pair<int,int> Pii;
typedef pair<Pii,Pii> Line;
typedef multimap<Pii,bool> Schedule;

Pii solve_case() {
    int T,NA,NB;
    scanf("%d\n", &T);
    scanf("%d %d\n", &NA, &NB);

    Schedule A,B;
    
    for(int i=0; i<NA; i++) {
	int ah,am, dh, dm;
	scanf("%d:%d %d:%d\n", &ah, &am, &dh, &dm);
	dm+=T;
	if(dh<23 && dm>60) { dh+=1; dm-=60; }
	A.insert(make_pair(make_pair(ah,am), true));
	B.insert(make_pair(make_pair(dh,dm), false));
    }

    for(int i=0; i<NB; i++) {
	int ah,am, dh, dm;
	scanf("%d:%d %d:%d\n", &ah, &am, &dh, &dm);
	dm+=T;
	if(dh<23 && dm>60) { dh+=1; dm-=60; }
	B.insert(make_pair(make_pair(ah,am), true));
	A.insert(make_pair(make_pair(dh,dm), false));
    }
    
    int trains_at_A = 0;
    int trains_at_B = 0;
    Pii diff_time = make_pair(-1,-1);
    Pii trains = make_pair(0,0);

    for(Schedule::iterator it = A.begin(); it != A.end(); it++) {
	if (it->first != diff_time) {
	    diff_time = it->first;
	    if(trains_at_A<0) {
		trains.first -= trains_at_A;
		trains_at_A = 0;
	    }
	}
	if (it->second) {
	    trains_at_A--;
	} else
	    trains_at_A++;
    }
    if(trains_at_A<0) {
	trains.first -= trains_at_A;
	trains_at_A = 0;
    }

    diff_time = make_pair(-1,-1);
    for(Schedule::iterator it = B.begin(); it != B.end(); it++) {
	if (it->first != diff_time) {
	    diff_time = it->first;
	    if(trains_at_B<0) {
		trains.second -= trains_at_B;
		trains_at_B = 0;
	    }
	}
	if (it->second) {
	    trains_at_B--;
	} else
	    trains_at_B++;
    }
    if(trains_at_B<0) {
	trains.second -= trains_at_B;
	trains_at_B = 0;
    }

    return trains;
};

int main()
{
    int N;
    scanf("%d\n", &N);
     for(int i_case=0; i_case<N; i_case++) {
	Pii result = solve_case();
	printf("Case #%d: %d %d\n", i_case+1, result.first, result.second);
    }
    return 0;
};
