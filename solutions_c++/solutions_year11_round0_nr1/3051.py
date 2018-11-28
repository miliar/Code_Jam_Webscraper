#include <iostream>
#include <vector>

using namespace std;

int T, N;

vector<pair<int, int>> actions;

inline long Abs(long x)
{
	return (x<0?-x:x);
}

inline long Max(long a, long b)
{
	return (a>b?a:b);
}

long Compute()
{
	vector<long> time(actions.size());
	for (int i=0; i<(int)actions.size(); i++)
	{
		if (i==0)
			time[0]=Abs(actions[0].second-1)+1;
		else
		{
			if (actions[i].first==actions[i-1].first)
				time[i]=time[i-1]+Abs(actions[i].second-actions[i-1].second)+1;
			else
			{
				int last=-1;
				for (int j=i-1; j>=0; j--)
					if (actions[i].first==actions[j].first)
					{
						last=j;
						break;
					}
				if (last<0)
					time[i]=Max(time[i-1]+1, Abs(actions[i].second-1)+1);
				else
					time[i]=Max(time[i-1]+1, time[last]+Abs(actions[i].second-actions[last].second)+1);
			}
		}
	}
	return time[time.size()-1];
}

int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);

	cin>>T;
	for (int i=0; i<T; i++)
	{
		cin>>N;
		char ch;
		int pos;
		actions.clear();
		for (int i=0; i<N; i++)
		{
			cin>>ch>>pos;
			if (ch=='O')
				actions.push_back(pair<int, int>(0, pos));
			else if (ch=='B')
				actions.push_back(pair<int, int>(1, pos));
		}

		long ret=Compute();
		cout<<"Case #"<<(i+1)<<": "<<ret<<endl;
	}

	return 0;
}