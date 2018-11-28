#include <iostream>
#include <vector>
using namespace std;

int main()
{
	int T;
	cin>>T;

	for(int i = 1; i <= T; ++i)
	{
		int N,S,p;
		cin>>N>>S>>p;

		vector<int> vi;
		for(int j = 0; j < N; ++j)
		{
			int tmp;
			cin>>tmp;
			vi.push_back(tmp);
		}

		int min = p + 2*(p-1);
		int ret = 0;
		for(int j = 0; j < N; ++j)
			if(vi[j] >= min || (min-vi[j])<=2 && --S>=0 && vi[j]>=2)
				++ret;

		cout<<"Case #"<<i<<": "<<ret<<endl;
	}
}