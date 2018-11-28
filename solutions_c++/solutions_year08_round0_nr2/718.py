#include <cstdio>
#include <list>
#include <vector>
#include <algorithm>

using namespace std;

typedef struct{
	int station, d_time, a_time;
}Trip;

bool cmp(Trip a, Trip b){
	if(a.d_time != b.d_time)
		return a.d_time < b.d_time;
	return a.a_time < b.a_time;
}

int main(){
	int nTests, test = 0;
	int na, nb, turn;
	vector<Trip> trips;
	for(scanf("%d", &nTests);nTests--;){
		scanf("%d", &turn);
		trips.clear();;
		scanf("%d %d", &na, &nb);
		while(na--){
			Trip t;
			t.station = 0;
			int h, m;
			scanf("%d:%d", &h, &m);
			t.d_time = h * 60 + m;		
			scanf("%d:%d", &h, &m);
			t.a_time = h * 60 + m;		
			trips.push_back(t);
		}
		while(nb--){
			Trip t;
			t.station = 1;
			int h, m;
			scanf("%d:%d", &h, &m);
			t.d_time = h * 60 + m;		
			scanf("%d:%d", &h, &m);
			t.a_time = h * 60 + m;		
			trips.push_back(t);
		}
		na = nb = 0;
		sort(trips.begin(), trips.end(), cmp);
		while(trips.size()){
			int t_chega = -turn - 1, station = trips[0].station;
			if(station == 0) ++na;
			else ++nb;
			for(int i = 0;i < trips.size();i++){
				//printf("%d %d %d - station %d \n", tr.station, tr.d_time, tr.a_time, station);
				if(t_chega + turn <= trips[i].d_time && station == trips[i].station){
					t_chega = trips[i].a_time;
					trips.erase(trips.begin() + i);
					station = (1 + station) % 2;
					i--;
				}
			}
		}
		printf("Case #%d: %d %d\n", ++test, na, nb);
	}
	return 0;
}
