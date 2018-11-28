#include<vector>
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
		long int L;
		long int H;
		cin>>N;
		cin>>L;
		cin>>H;

		vector<long int> data(N, 0);
		for (int n = 0; n < N; ++n) {
			long int tmp;
			cin>> tmp;
			data[n] = tmp;
		}

		bool found = false;
		long int frequency = 0;
		for(int f = L; f<=H;++f) {
			bool fo = true;
			for (int n = 0; n < N; ++n) {
				if (f/data[n]*data[n] != f && data[n]/f*f != data[n]) {
					fo = false;
						break;
				}
			}
			if (fo) {
				found = true;
				frequency = f;
				break;
			}
		}
		if (found) {
			cout<<"Case #"<<t+1<<": "<<frequency<<endl;
		}
		else
		{
			cout<<"Case #"<<t+1<<": "<<"NO"<<endl;
		}
	}
}
