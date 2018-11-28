#include <iostream>

using namespace std;

int main(){
	int T;
	cin >> T;
	long long gsize[1000];
	int target[1000];
	long long rides[1000];
	int DIGG = 1;
	while(T--){
		int R,k,N;
		cin >> R >> k >> N;
		for(int i = 0; i < N; i++){
			cin >> gsize[i];
		}
		for(int i = 0; i < N; i++){
			int next = i;
			long long tot = 0;
			for(int j = 0; j < N; j++){
				if(tot+gsize[next] <= k){
					tot += gsize[next];
				}
				else{
					break;
				}
				next = (next+1)%N;
			}
			rides[i] = tot;
			target[i] = next;
		}
		bool visited[1000];
		for(int i = 0; i < N; i++) visited[i] = false;
		long long tot_rides = 0;
		int next = 0;
		visited[0] = true;
		tot_rides += rides[0];
		next = target[0];
		int cycle_start = 0;
		long long count = 1;
		for(int i = 0; i < R; i++){
			if(count == R){
				break;
			}
			if(visited[next] == false){
				visited[next] = true;
				tot_rides+=rides[next];
				next = target[next];
			}
			else{
				cycle_start = next;
				break;
			}
			count++;
		}
		for(int i = 0; i < N; i++) visited[i]=false;
		if(count < R){
			long long rides_per_cycle = 0;
			int nx = cycle_start;
			int num_per_cycle = 1;
			visited[nx] = true;
			rides_per_cycle += rides[nx];
			nx = target[nx];
			for(int i = 0; i < N; i++){
				if(visited[nx] == false){
					visited[nx] = true;
					rides_per_cycle += rides[nx];
					nx = target[nx];
				}
				else{
					break;
				}
				num_per_cycle++;
			}
			if((R-count)>=num_per_cycle){
				tot_rides += ((R-count)/num_per_cycle)*rides_per_cycle;
				count += ((R-count)/num_per_cycle)*num_per_cycle;
			}
		}
		if(count < R){
			int nx = cycle_start;
			count++;
			tot_rides+=rides[nx];
			for(int i = 0; i < N; i++){
				if(count < R){
					nx = target[nx];
					tot_rides+=rides[nx];
					count++;
				}
				else{
					break;
				}
			}
		}
		cout << "Case #" << DIGG << ": " << tot_rides << endl;
		DIGG++;
	}

}
