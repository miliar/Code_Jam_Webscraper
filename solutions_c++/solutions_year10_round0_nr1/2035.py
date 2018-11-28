//#include <iostream>
#include <sstream>
#include <fstream>
#include <math.h>


using namespace std;

ifstream cin ("A-large.in");
ofstream cout ("outfile3.out");



bool f(int N, long K) {
	long test = pow(2,N);
	if ((K+1)%test == 0) return true;
	else return false;
}

int main () {
	int T;
	string s;
	cin>>T;
	cin.get();
	for (int i=0;i<T;i++) {
		int N;
		long K;
		getline(cin,s);
		istringstream str(s);
		str>>N;
		str>>K;
		bool res = f(N,K);
		if (res == true) cout<<"Case #"<<i+1<<": ON"<<endl;
		else cout<<"Case #"<<i+1<<": OFF"<<endl;
	}
	return 0;

}
