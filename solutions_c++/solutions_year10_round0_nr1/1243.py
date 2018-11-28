
#include <iostream>
#include <vector>
#include <algorithm>
#include <stdlib.h>

using namespace std;

typedef struct stat{
	bool on;
	bool power;
}state;

int power(int n){
	int result=1;
	for(int i =0; i<n; i++){
		result= result*2;
	}
	return result;
}

main(){
	int T = 0; cin >> T;

	for(int i=0; i<T; i++){
		int answer = 0;
		int N=0;unsigned int K=0;cin >> N >> K;

		K = K%(power(N));
		if((power(N)-1) == K)answer=1;
		cout << "Case #" << i+1 << ": " << (answer?"ON":"OFF") << endl;

		/*
		state chain[N];
		for(int n=0; n<N; n++){
			chain[n].on = false;
			chain[n].power = false;
		}

		chain[0].power=true;

		for(unsigned int k=0; k<K; k++){
			
			for(int n=0; n<N; n++){
				if(chain[n].power)chain[n].on = !chain[n].on;
				if(!chain[n-1].power){
					chain[n].power=false;
				}else{
					chain[n].power= !chain[n].power;
				}
			}
		}
			*/

	}
}
