#include <iostream>
#include <vector>
#include <algorithm>
#include <stdlib.h>
#include <math.h>
#include <stdio.h>

using namespace std;

struct task 
{
	int type;
	int button;
};

vector<task> vec;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);
	int T;
	cin>>T;
	for(int test = 1; test <= T; ++test)
	{
		int n;
		cin >> n;
		
		for (int i = 0; i < n; ++i)
		{
			char c;
			task t;
			cin>>c;
			t.type = (c == 'O') ? 0 : 1;
			cin>>t.button;
			vec.push_back(t);
		}

		int cur_type, future_type;
		int pos[2] = {1, 1};
		int turns = 0;
		while (vec.size() > 0)
		{
			cur_type = vec[0].type;
			future_type = 1 - cur_type;
			int fut_task;
			for( int j=1; j < vec.size(); ++j)
			{
				if (vec[j].type == future_type )
				{
					fut_task = vec[j].button;
					break;
				}
			}

			int add_turns = abs(pos[cur_type] - vec[0].button ) + 1;

			turns += add_turns;
			pos[cur_type] = vec[0].button;

			if (add_turns >= abs(fut_task - pos[future_type]) )
				pos[future_type] = fut_task;
			else 
			{
				if (fut_task > pos[future_type])
					pos[future_type] += add_turns;
				else pos[future_type] -= add_turns;
			}


			vec.erase(vec.begin());
		}

		cout << "Case #"<<test<<": ";
		cout<<turns;

		cout<<endl;
	}
	fclose(stdout);
	return 0;
}