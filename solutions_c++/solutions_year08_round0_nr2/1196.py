#include <set>
#include <iostream>
#include <string>
#include <vector>
#include <cstdio>

using namespace std;

typedef pair<int,int> Event;
typedef pair<int,int> Trip;

Trip readTrip()
{
	int m1, s1, m2, s2;
	scanf("%d:%d %d:%d", &m1, &s1, &m2, &s2);
	return Trip(m1*60+s1, m2*60+s2);
}

enum{
	AR_A, AR_B, DP_A, DP_B
};

/*
bool contain(Trip& t1, Trip& t2)
{
	return t1.first <= t2.first && t2.second <= t1.second;
}

int solve(vector<Trip>& trips)
{
	vector<bool> removed(trips.size(), false);
	for(int i=0;i<trips.size();i++){
		if( removed[i] )continue;
		for(int j=0;j<trips.size();j++){
			if( removed[j] || i == j )continue;
			if( contain(trips[i], trips[j]) ){
				removed[j] = true;
			}
		}
	}
	int cnt = 0;
	for(int i=0;i<trips.size();i++){
		if( !removed[i] )cnt++;
	}
	return cnt;
}
*/

	
int main()
{
	int c;
	scanf("%d", &c);
	for(int i=0;i<c;i++){
		int t;
		scanf("%d", &t);

		int n[2];
		scanf("%d %d", &n[0], &n[1]);
		cout << "Case #" << (i+1) << ":";
		vector<Event> events;
		for(int k=0;k<n[0];k++){
			Trip trip = readTrip();
			events.push_back( Event(trip.first, DP_A) );
			events.push_back( Event(trip.second+t, AR_B) );
		}
		for(int k=0;k<n[1];k++){
			Trip trip = readTrip();
			events.push_back( Event(trip.first, DP_B) );
			events.push_back( Event(trip.second+t, AR_A) );
		}
		sort( events.begin(), events.end() );

		int na = 0, nb = 0;
		int ans1 = 0, ans2 = 0;
		for(int i=0;i<events.size();i++){
			Event& e = events[i];
			if( e.second == AR_A ){
				na++;
			}
			if( e.second == AR_B ){
				nb++;
			}
			if( e.second == DP_A ){
				if( na == 0 ){
					ans1++;
				} else {
					na--;
				}
			}
			if( e.second == DP_B ){
				if( nb == 0 ){
					ans2++;
				} else {
					nb--;
				}
			}
		}
		
		cout << " " << ans1 << " " << ans2 << endl;
	}
}



		
