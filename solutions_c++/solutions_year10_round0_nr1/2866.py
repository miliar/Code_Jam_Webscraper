#include <iostream>
#include <fstream>
using namespace std;

ofstream fout("A-large.out.txt");



int main(){
	freopen("A-large.in.txt","r",stdin);
	int T;
	unsigned long N;
	unsigned long temp; 
	unsigned long K;


	cin>>T;

	for(int i = 1 ; i <= T ; i++){
		cin>>N>>K;

		temp = 2;
		for(int j = 1 ; j < N ; j++){
			temp *= 2;
		}

		temp--;

		if((temp & K) == temp)
			fout<<"Case #"<<i<<": ON"<<endl;
		else
			fout<<"Case #"<<i<<": OFF"<<endl;		
	}

	return 0;
}