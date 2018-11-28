#include<iostream>
#include<vector>

using namespace std;

class state_t
{
	public:
		state_t()
//		: next_state(-1), value(0)
		{}
		size_t next_state;
		long long value;
};

ostream & operator<<(ostream & out, const state_t & rhs)
{
	out << "Val(" << rhs.value << ") Next: " << rhs.next_state;
	return out;
}

void fill(vector<state_t> & states, vector<long long> & groups, long long capacity)
{
	for(size_t i=0;i<states.size();i++)
	{
		states[i].value = groups[i];
		//Working backwards can introduce bounds that might speed this up
		for(size_t j=(i+1);j<(i+states.size());j++)
		{
			size_t index = j % states.size();
			states[i].value += groups[index];
			if(states[i].value > capacity)
			{
				states[i].value -= groups[index];
//				states[i].next_state = (index + states.size() - 1) % states.size();
				states[i].next_state = index;
				break;
			}
		}
	}
}

long long cycle(vector<state_t> & states, long long rides)
{
	long long retval = 0;
	vector<char> visited(states.size(),0);

	vector<size_t> path;

	bool shorted = false;

	size_t at = 0;
	for(long long i=0;i<rides;i++)
	{
		if(visited[at] && !shorted)
		{
			//Try to discover cycle
			while(path[0] != at)
			{
				path.erase(path.begin());
			}
			long long pathval = 0;
			for(size_t j=0;j<path.size();j++)
			{
				pathval += states[path[j]].value;
			}
			long long leftover = (rides - i)/path.size();
			retval += leftover * pathval;
			i += leftover * path.size();

			i--;
			shorted = true;
			continue;
		}
		else
		{
			visited[at] = 1;
			path.push_back(at);
			retval += states[at].value;
			at = states[at].next_state;
		}
	}
	return retval;
}

int main()
{
	int num;
	cin >> num;

	for(int i=1;i<=num;i++)
	{
		long long rides, capacity, gnum;
		cin >> rides >> capacity >> gnum;

		vector<long long> groups(gnum,0);
		long long sum = 0;
		for(size_t j=0;j<groups.size();j++)
		{
			cin >> groups[j];
			sum += groups[j];
		}
//		cout << endl;

		if(capacity >= sum)
		{
			cout << "Case #" << i << ": " << rides*sum << endl;
			continue;
		}

		vector<state_t> states(gnum);
		fill(states, groups, capacity);

//		for(size_t j=0;j<states.size();j++)
//		{
//			cout << j << ": " << states[j] << endl;
//		}

		long long cash_money = cycle(states,rides);

		cout << "Case #" << i << ": " << cash_money << endl;
	}
	return 0;
}
