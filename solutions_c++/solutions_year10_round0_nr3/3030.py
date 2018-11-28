#include <iostream>
using namespace std;

int main(){
	int T;
	cin >> T;
	for (int c=1; c<=T; c++){
		int R, k, N;
		cin >> R >> k >> N;
		int* group = new int [N];
		for (int i=0; i<N; i++)	cin >> group[i];

		int cost = 0;
		int round = 0;
		int first=0;
		while (round<R){
			int knum=0; int count=0;
			while (count<N && knum+group[first]<=k){
				knum+=group[first];
				count++;
				first = (first+1)%N;
			}
			cost+=knum;	
			round++;
		}

		delete [] group;
		cout<<"Case #"<<c<<": "<<cost<<endl;

	}
	return 0;
}
