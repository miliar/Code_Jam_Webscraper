#include <iostream>
#include <vector>
#include <string>
#include <queue>

using namespace std;

struct Objective
{
	Objective(int button, int order) : button(button), order(order) { }

	int button;
	int order;
};

int main()
{
	int T;

	cin >> T;

	for(int i = 0; i < T; ++i)
	{
		int N;
		cin >> N;
		queue<Objective> O;
		queue<Objective> B;
		for(int j = 0; j < N; ++j)
		{
			char c;
			cin >> c;
			int button;
			cin >> button;
			if(c == 'O')
				O.push(Objective(button, j));
			else
				B.push(Objective(button, j));
		}


		int lastObjective = -1;
		int Bpos = 1;
		int Opos = 1;

		unsigned int seconds = 0;
		for(;!B.empty() || !O.empty(); ++seconds)
		{
			bool clicked = false;
			if(!B.empty())
			{
				if(B.front().button != Bpos)
				{
					if(B.front().button > Bpos)
						++Bpos;
					else
						--Bpos;
				}
				else if(B.front().order - 1 == lastObjective)
				{
					lastObjective = B.front().order;
					B.pop();
					clicked = true;
				}
			}

			if(!O.empty())
			{
				if(O.front().button !=Opos)
				{
					if(O.front().button > Opos)
						++Opos;
					else
						--Opos;
				}
				else if(O.front().order - 1 == lastObjective && !clicked)
				{
					lastObjective = O.front().order;
					O.pop();
				}
			}
		}
		cout << "Case #" << i + 1 << ": " << seconds << endl;


	}

	return 0;
}
