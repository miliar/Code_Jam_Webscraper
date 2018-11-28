#include <iostream>
#include <vector>
#include <set>
#include <string.h>

using namespace std;

const int N = 2000000;

void makeRecVec(int x, vector<int> &res)
{
	res.clear();

	char s1[8];
	char s2[8];

	itoa(x, s1, 10);

	set<int> tmp;

	int NS = strlen(s1);
	s2[NS] = 0;

	for(int j=0; j<NS; ++j)
	{
		for(int i=0; i<NS; ++i)
		{
			s2[(i+j)%NS] = s1[i];
		}
		if(s2[0]!='0')
		{
			tmp.insert(atoi(s2));
		}
	}

	for(set<int>::const_iterator ii = tmp.begin(); ii != tmp.end(); ++ii)
	{
		if((*ii)<=N)
			res.push_back(*ii);
	}
}

int main()
{
	vector<char> used;
	vector<int> a;

	a.resize(N+1);
	used.resize(N+1);

	for(int i=1; i<=N; ++i)
	{
		if(!used[i])
		{
			vector<int> tmp;
			makeRecVec(i, tmp);

			int NN = tmp.size();

			for(int j=0; j<NN; ++j)
				used[tmp[j]] = true;

			if(NN>1)
			{
				for(int j=1; j<NN; ++j)
					a[tmp[j]] = tmp[j-1];
			}
		}
	}

	int T, A, B;

	cin>>T;

	for(int t = 1; t<=T; ++t)
	{
		cin>>A>>B;

		int cnt = 0;

		for(int i = A+1; i<=B; ++i)
		{
			int jj = i;

			while(a[jj]>=A)
			{
				++cnt;
				jj = a[jj];
			}
		}

		cout<<"Case #"<<t<<": "<<cnt<<endl;
	}

	return 0;
}
