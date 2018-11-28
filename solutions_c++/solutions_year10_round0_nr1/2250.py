#include <fstream>
#include <iostream>
using namespace std;

int main(int argc, char *argv[]){
	int n[31];
	int i;
	n[0] = 1;	
	for (i = 1;i<31;i++){
		n[i] = n[i-1]*2;
	}
	ifstream in("A-large.in");
	ofstream out("A-large.out");
	int T,N,K,count;
	in>>T;
	for (i=0;i<T;i++){
		in>>N>>K;
		count = n[N]-1;
		if (((K+1) % n[N]) == 0){
			out<<"Case #"<<i+1<<": ON\n";
		}
		else
		{
			out<<"Case #"<<i+1<<": OFF\n";
		}
	}

}