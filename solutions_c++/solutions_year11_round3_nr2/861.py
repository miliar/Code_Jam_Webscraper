#include <cstdio>
#include <vector>

using namespace std;

int main(){
	unsigned int T;
	unsigned long long L,t,N,C;
	scanf("%d", &T);
	unsigned long long curr_time;
	short a;
	for(unsigned int i = 0; i < T; ++i){
		scanf("%llu%llu%llu%llu", &L, &t, &N, &C);
		short *dists = new short[C];
		curr_time = 0;
		for(unsigned int j = 0; j < C; ++j){
			scanf("%hd", &a);
			dists[j] = a;
		}
		vector<unsigned long long> boosts;
		unsigned long long curr_time = 0;
		unsigned int start_ind;
		for(unsigned int j = 0; j < N; ++j){
			if(curr_time >= t){ 
				boosts.push_back(dists[j%C]*2);
			}else if(curr_time + dists[j%C]*2 > t){
				start_ind = j;
				boosts.push_back(curr_time + dists[j%C]*2 - t);
			}else{
				boosts.push_back(0);
			}
			
			curr_time += dists[j%C]*2;
		}
		unsigned long long optimized=0;
		unsigned long long sum = curr_time;
		//printf("sum: %llu\n", sum);
		for(unsigned int k = 0; k < L; ++k){
			unsigned long long curr_heighest_i = N-1;
			unsigned long long curr_heighest = 0;
			for(unsigned int j = 0; j < N; ++j){
				/*if(j-C>=curr_heighest_i){
					break;
				}*/
				//printf("boosts at %d: %llu\n", j, boosts[j]);
				if(boosts[j] > curr_heighest){
					curr_heighest_i = j;
					curr_heighest = boosts[j];
				}
			}
			if(curr_heighest > 0){
				optimized += boosts[curr_heighest_i]/2;
				//printf("optimize at %llu: %llu\n", curr_heighest_i, boosts[curr_heighest_i]);
				boosts[curr_heighest_i] = 0;
			
				if(curr_heighest_i == start_ind){
					bool new_si = false;
					for(unsigned int l = curr_heighest_i+1; l < N; ++l){
						if(boosts[l]>0){
							start_ind = l;
							new_si = true;
							break;
							
						}
					}
					if(!new_si){
						break;
					}
				}
				//break;
			}else{
				break;
			}
		}
		printf("Case #%d: %llu\n", i+1,sum-optimized);
	}
	return 0;
}
