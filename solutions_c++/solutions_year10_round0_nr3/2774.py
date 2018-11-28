#include<cstdio>
#include<vector>
#include<set>
using namespace std;

int main(){
	int t, R, k, N;
	scanf("%d", &t);
	for(int i=1; i<=t; i++){
		scanf("%d %d %d", &R, &k, &N);
		vector<int> g(N);
		for(int j=0; j<N; j++)
			scanf("%d", &g[j]);
		/*for(int j=0; j<N; j++){
			if(g[j] > k) {g.erase(g.begin()+j); j--; N--;}
		}*/
		vector<pair<int, int> >cycle;
		set<int> indices;
		int index = 0;
		int rest = k;
		int fare = 0;
		int people = 0;
		int prev_index = 0;
		while(true){
			if(rest >= g[index] && people < N){
				rest -= g[index];
				fare += g[index];
				index = (index + 1)%N;
				people++;
			} else {
				//printf("Ride : starting %d person will go next. Total fare collected in this round is %d. Prev index is %d\n", index, fare, prev_index);
				if(indices.find(prev_index) != indices.end()) break;
				cycle.push_back(make_pair(fare, prev_index));
				indices.insert(prev_index);
				rest = k;
				fare = 0;
				people = 0;
				prev_index = index;
			}
		}
		//printf("Prev index is %d\n", prev_index);
		//for(int j=0; j<cycle.size(); j++)
		//	printf("fare : %d | index : %d\n", cycle[j].first, cycle[j].second);
		int cycle_detected_at_index = prev_index;
		int total_profit_in_one_cycle = 0;
		int total_profit_till_cycle_starts = 0;
		int total_profit_after_cycle_ends = 0;
		int cycle_detected_at = cycle.size();
		for(int j = 0; j<cycle.size() && R>0; j++){
			if(cycle[j].second != cycle_detected_at_index){
				total_profit_till_cycle_starts += cycle[j].first;
				R--;
			}
			else{
				cycle_detected_at = j; break;
			}
		}
		for(int j = cycle_detected_at; j<cycle.size(); j++){
                        total_profit_in_one_cycle += cycle[j].first;
                }
		//printf("Profit in one cycle : %d\n", total_profit_in_one_cycle);
		int profit = total_profit_till_cycle_starts;
		//printf("Profit before cycles : %d | R is %d | cycle.size() is %d\n", profit, R, cycle.size());
		if(R > 0){
			int total_cycles = R / (cycle.size() - cycle_detected_at);
			//printf("Total cycles : %d\n", total_cycles);	
			profit += total_cycles * total_profit_in_one_cycle;
			R -= total_cycles * (cycle.size() - cycle_detected_at);
		}
		//printf("Profit after cycles : %d\n", profit);
		if(R > 0){
			for(int j = cycle_detected_at; R > 0; j = (j + 1)%cycle.size(), R--)
				profit += cycle[j].first;
		}
			
		printf("Case #%d: %d\n", i, profit);
	}
}
