#include<iostream>
using namespace std;

unsigned long long money(unsigned int R, unsigned int k, unsigned int N, unsigned int G[]){
    if( G[0] > k ){
	return 2;
    }
    unsigned long all = 0;
    for(int i = 0 ; i < N ; i++){
	all += G[i];
    }
    if(all <= k){
	return  all * R;
    }
    unsigned int step[N], pile[N], sum = G[0], ptr = 0, tail = 1;
    for(ptr = 0 ; ptr < N ; ptr++){
	while( sum + G[ tail%N ] <= k ){
	    sum += G[ (tail++)%N ];
	}
	pile[ptr] = sum;
	step[ptr] = tail%N;
	sum -= G[ptr];
    }

    unsigned long long earned = 0;
    for(int i = 0, idx = 0 ; i < R ; i++){
	earned += pile[idx];
	idx = step[idx];
    }

    return earned;
}

int main(int argc, char* argv[]){
    unsigned int T, R, N, k;
    unsigned G[1005];
    cin >> T;
    for(int i = 0 ; i < T ; i++){
	cin >> R >> k >> N;
	for(int j = 0 ; j < N ; j++){
	    cin >> G[j];
	}
	cout << "Case #" << i+1 << ": " << money(R, k, N, G) << endl;
    }
    return 0;
}
