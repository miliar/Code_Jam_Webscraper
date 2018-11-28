#include <iostream>
#include <vector>
using namespace std;

long long val = -1;
vector<int> candy;

void solve(bool chose[], int pos)
{
	if(pos == candy.size())
	{
		int left = 1;
		long long vl = 0;
		int right = 1;
		long long vr = 0;

		for(int i = 0; i < pos; ++i)
			if(chose[i])
			{
				left ^= candy[i];
				vl += candy[i];
			}
			else
			{
				right ^= candy[i];
				vr += candy[i];
			}

		left ^= 1;
		right ^= 1;
		long long larger = max(vl, vr);

		if(left == right && larger > val && vl != 0 && vr != 0)
			val = larger;

		return ;
	}

	chose[pos] = true;
	solve(chose, pos+1);

	chose[pos] = false;
	solve(chose, pos+1);
}

int main()
{
	int T;
	cin>>T;

	for(int i = 0; i < T; ++i)
	{
		int N;
		cin>>N;
	
		for(int j = 0; j < N; ++j)
		{
			int tmp;
			cin>>tmp;
			candy.push_back(tmp);
		}

		bool chose[100] = {0};
		solve(chose, 0);

		if(val != -1)
		{
			cout<<"Case #"<<i+1<<": "<<val<<endl;
		}
		else
		{
			cout<<"Case #"<<i+1<<": NO"<<endl;
		}

		val = -1;
		candy.clear();
	}

	return 0;
}