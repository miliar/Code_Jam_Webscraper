#include<iostream>
using namespace std;

bool light(unsigned int N, unsigned int K){
    // 0 <= K <= 10^8, 1 <= N <= 30
    K += 1;
    unsigned int base = (1 << N)-1;
    //cout << "K&base == " << (K&base) << " ==0?" << ((K&base)==0)<< endl;
    return (K&base) == 0 ? true : false;
}

int main(int argc, char* argv[]){
    unsigned int T, N, K;
    cin >> T;
    for(int i = 0 ; i < T ; i++){
	cin >> N >> K;
	if( light(N, K) ){
	    cout << "Case #" << i+1 << ": ON" << endl;
	}else{
	    cout << "Case #" << i+1 << ": OFF" << endl;
	}
    }
    return 0;
}
