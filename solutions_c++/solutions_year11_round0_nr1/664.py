#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include <algorithm>
#include <queue>


using namespace std;

ifstream in("large.in");
ofstream out("large.out");

queue <int> O;
queue <int> B;
queue <char> S;

int solve()
{
	int pos_O = 1;
	int pos_B = 1;
	int time;
	
	for (time = 1; !S.empty(); ++time)
		if (S.front() == 'O')
		{
			if (pos_O == O.front())
			{
				O.pop();
				S.pop();
			}
			else
			{
				if (pos_O < O.front())
					pos_O++;
				else
					pos_O--;
			}
			if (!B.empty())
			{
				if (pos_B < B.front())
					pos_B++;
				else
				if (pos_B > B.front())
					pos_B--;

			}
		}
		else
		{
			if (pos_B == B.front())
			{
				B.pop();
				S.pop();
			}
			else
			{
				if (pos_B < B.front())
					pos_B++;
				else
					pos_B--;
			}
			if (!O.empty())
			{
				if (pos_O < O.front())
					pos_O++;
				else
				if (pos_O > O.front())
					pos_O--;
			}
		}
	return time - 1;	
}

template <class T>
void clear(queue <T>& q)
{
	while (!q.empty())
		q.pop();
}

int main()
{
	int test,t,nomer,N,i;
	char ch;

	in >> test;

	for (t = 1; t <= test; ++t)
	{
		in >> N;
		clear(O);
		clear(B);		
		clear(S);
		for (i = 0 ; i < N; ++i)
		{
			in >> ch >> nomer;
			S.push(ch);
			if (ch == 'O')
				O.push(nomer);
			else
				B.push(nomer);
		}
		out << "Case #" << t << ": " << solve() << endl;
	}

	return 0;
}