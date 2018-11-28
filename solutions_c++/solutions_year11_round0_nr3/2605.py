#include <vector>
#include <iostream>
#include <string> 
#include <limits>

using namespace std;

int main()
{
	int T;
	cin>> T;
	for(int t = 0; t<T;++t) {
		int N;
		cin>>N;
		vector<unsigned int> cand(N, 0);
		for(int i = 0; i<N; ++i ){
			unsigned int tmp;
			cin>>tmp;
			cand[i] = tmp;
		}
		unsigned int res = 0;
		for(int i = 0; i<N; ++i ){
			res = res ^ cand[i];
		}
		if (res != 0u){
			cout<<"Case #"<<t+1<<": NO"<<endl;
		}
		else
		{
			int sum = 0;
			unsigned int minv = numeric_limits<unsigned int>::max();
			for(int i = 0; i<N; ++i ){
				sum += cand[i];
				minv = min(minv, cand[i]);
			}
			cout<<"Case #"<<t+1<<": "<<sum-minv<<endl;
		}

	}
}
