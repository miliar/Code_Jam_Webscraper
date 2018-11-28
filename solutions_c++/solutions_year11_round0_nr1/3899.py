#include <iostream>
#include <list>

using namespace std;

typedef list<int> stack;
typedef pair<bool,int> f;
typedef list<f > fstack;


int solve(fstack& full, stack& orange, stack& blue, int o, int b)
{
	int time;
	bool odone = false;
	bool bdone = false;

	if(full.empty())
		return 0;

	if(orange.empty())
		odone = true;
	if(blue.empty())
		bdone = true;
	if(!odone && o < orange.front())
	{
		++o;
		odone = true;
	}
	else if(!odone && o > orange.front())
	{
		--o;
		odone = true;
	}

	if(!bdone && b < blue.front())
	{
		++b;
		bdone = true;
	}
	else if(!bdone && b > blue.front())
	{
		--b;
		bdone = true;
	}

	if(!odone && full.front().first)
	{
		orange.pop_front();
		full.pop_front();
	}
	else if(!bdone && !full.front().first)
	{
		blue.pop_front();
		full.pop_front();
	}

	time = solve(full,orange,blue,o,b);

	return time+1;
}

int main(int nargs, char** args)
{
	stack  orange;
	stack  blue;
	fstack full;

	int T;
	int N;

	char color;
	int  button;

	int  time;

	cin >> T;

	for(int t = 1; t <= T; ++t)
	{
		orange.clear();
		blue.clear();
		full.clear();

		cin >> N;

		for(int n = 0; n < N; ++n)
		{
			cin >> color >> button;

			if(color == 'O')
				orange.push_back(button);
			else 
				blue.push_back(button);

			full.push_back(f(color=='O',button));
			
		}

		time = solve(full, orange, blue, 1, 1);

		cout << "Case #" << t << ": " << time << endl;

	}


	return 0;
}