#include<iostream>

using namespace std;

int main() {
	unsigned long long T;
	cin>>T;
	for(unsigned long long t=0;t<T;t++) {
        unsigned long long N,K,X;
        cin>>N>>K;
        X = 1<<N;
        X--;
        if((X&K)==X) {
			cout<<"Case #"<<t+1<<": ON\n";
		}
		else {
            cout<<"Case #"<<t+1<<": OFF\n";
		}
	}
	return 0;
}
