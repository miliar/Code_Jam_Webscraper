#include <iostream>
#include <vector>
#include <deque>
using namespace std;

int main()
{
	int t;
	cin>>t;

	for(int i = 0;i < t; ++i)
	{
		int R, k, N;
		cin>>R>>k>>N;
		deque<int> di;
		for(int j = 0; j < N; ++j)
		{
			int tmp;
			cin>>tmp;
			di.push_back(tmp);
		}

		int ret = 0;
		int inc = 0;
		int j = 0;
		for(j = 0; j < R; ++j)
		{
			int m = 0;
			int c = 0;
			deque<int>::iterator it = di.begin();
			while(it != di.end() && (m+*it) <= k) {
				m += *it;
				++it;
				++c;
			}

			int pos = 0;
			while(pos < c) {
				di.push_back(di.front());
				di.pop_front();
				++pos;
			}
			
			ret += m;
			//if(R>N && j<(R%N))
			//	inc += m;
		}

		//if(j == R)
			cout<<"Case #"<<i+1<<": "<<ret<<endl;
		//else
		//	cout<<"Case #"<<i+1<<": "<<ret*(R/N)+inc<<endl;
	}
}