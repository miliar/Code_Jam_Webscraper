#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>

#define FOR(i, n) for(int i = 0; i < n; i++)

using namespace std;

int people[1000];
int profit[10000001];
map<pair<int,int>,int> m;

int main() {
	int T, R, sz, N, cycle_start, cycle_length;
	unsigned long long leg_sum, cycle_sum, answer;
	
	scanf("%d\n", &T);
	
	FOR(nCase, T) {
		scanf("%d %d %d\n", &R, &sz, &N);
		
		FOR(i, N) scanf("%d ", &people[i]);
		
		int i = 0, j = 0, sum;
		m.clear();
		
		while(true) {
			sum = people[i];
			j = (i+1)%N;
			while(i != j && sum + people[j] <= sz) {
				sum += people[j];
				j = (j+1)%N;
			}
			
			//printf("\t%d: (%d %d) %d\n", m.size(), i, (j+N-1)%N, sum);
			
			pair<int,int> p = make_pair(i, (j+N-1)%N);
			
			if(m.find(p) != m.end()) {
				cycle_start = m[p]-1;
				cycle_length = m.size() - cycle_start;
				break;
			} else {
				profit[m.size()] = sum;
				m[p] = m.size();
			}
			
			i = j;
		}
		
		leg_sum = 0;
		FOR(x, cycle_start) leg_sum += profit[x];
		cycle_sum = 0;
		for(int x = cycle_start; x < m.size(); x++) cycle_sum += profit[x];
		
		answer = 0;
		if(R <= cycle_start) {
			for(int x = 0; x < R; x++) answer += profit[x];
		} else {	
			//printf("%lld %d %d %d %d\n", answer, R, cycle_start, cycle_length, cycle_sum);
			answer = leg_sum + cycle_sum * ((R-cycle_start)/cycle_length);
			R = (R-cycle_start) % cycle_length - 1;
			//printf("%lld %d\n", answer, R);
			for(int x = 0; x <= R; x++) answer += profit[x+cycle_start];
			//printf("%lld %d\n", answer, R);
		}
		
		printf("Case #%d: %lld\n", nCase+1, answer);
	}
}
