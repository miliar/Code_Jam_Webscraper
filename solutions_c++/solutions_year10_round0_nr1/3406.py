#include <iostream>

using namespace std;

int main() {

	long i,n,k;
	cin>>i;
	long cycle;
	long wasted;
	for(int c=0;c<i;++c) {
		cin>>n>>k;
		cycle = (long)pow((double)2, n);
		cout << "Case #" << (c+1) << ": " << ((k+1)%cycle==0 ? "ON":"OFF") << endl;
	}
	return 0;
}