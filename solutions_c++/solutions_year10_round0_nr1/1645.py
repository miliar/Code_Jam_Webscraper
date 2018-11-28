#include <iostream>
#include <vector>

using namespace std;

int main() {
	int T;
	int N;
	int K;
	bool result=false;
	cin>>T;
	for(int t=0;t<T;t++) {
		cin>>N>>K;
		int mask = (1<<N)-1;
		result = ((K&mask) == mask);
		cout<<"Case #"<<(t+1)<<": "<<((result)?"ON":"OFF")<<endl;
	}
	
	return 0;
}

