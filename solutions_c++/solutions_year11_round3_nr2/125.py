#include <stdio.h>
#include <map>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

long long distFrom[1000009];
long long a[1009];
long long L, t, N, C;


long long gotry(long long startTid, long long start, long long startHarBoost){
	long long tid = startTid;
	long long myL;
	if(startHarBoost){
		myL = L-1;
		long long dist = distFrom[start];
		if(tid>=t){
			tid += dist;
		} else {				
			long long fardigAt = (t-tid)/2;
			if(fardigAt>=dist){
				tid += 2*dist;
			} else {
				tid += 2*fardigAt + (dist-fardigAt);
			}
		}
	}else{
		myL = L;
		tid += 2*distFrom[start];
	}
	vector<long long> v;
	for(long long fr=start+1;fr<N;fr++){
		v.push_back(distFrom[fr]);
	}
	sort(v.begin(), v.end());
	for(long long i=v.size()-1;i>=0;i--){
		if(myL>0){
			tid += v[i];
		} else {
			tid += 2*v[i];
		}
		myL--;
	}
	
	return tid;
}

void run(long long fall){
	printf("Case #%lld: ", fall+1);
	scanf("%lld %lld %lld %lld", &L, &t, &N, &C);	
	for(long long i=0;i<C;i++){
		scanf("%lld", &a[i]);
	}
	long long i=0;
	for(long long j=0;j<N;j++){
		distFrom[j] = a[i];
		i = (i+1)%C;
	}

	long long tid = 0;
	long long provaFrom = N;
	for(long long fr=0;fr<N;fr++){
		long long dist = distFrom[fr];
		long long frammeAt = tid + 2*dist;
		if(frammeAt > t){
			provaFrom = fr;
			break;
		}
		tid = frammeAt;
	}
	if(provaFrom == N){
		printf("%lld\n", tid);
		return;
	}
	if(L>=1){
		long long best = gotry(tid, provaFrom, 1);
		long long nu = gotry(tid, provaFrom, 0);
		if(nu<best) best = nu;

		printf("%lld\n", best);
	} else {
		long long tid = 0;
		for(long long fr=0;fr<N;fr++){
			long long dist = distFrom[fr];
			long long frammeAt = tid + 2*dist;
			tid = frammeAt;
		}
		printf("%lld\n", tid);
	}

}


int main(){
	long long N;
	scanf("%lld", &N);
	for(long long i=0;i<N;i++){
		run(i);
	}	
}