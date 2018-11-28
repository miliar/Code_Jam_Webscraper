#include <iostream>

using namespace std;

char data[110];
char combine[110][5];
char opp[110][5];
int T, cases, C, D, N;
int curr;

bool check_combine()
{
	if (curr<2)
		return false;

	for (int i=0 ;i<C ;i++)
	{
		if (data[curr-1]==combine[i][0] && data[curr-2]==combine[i][1])
		{
			data[curr-2] = combine[i][2];
			curr--;
			return true;
		}
		if (data[curr-2]==combine[i][0] && data[curr-1]==combine[i][1])
		{
			data[curr-2] = combine[i][2];
			curr--;
			return true;
		}
	}

	return false;
}

bool check_opp()
{
	if (curr<2)
		return false;

	for (int i=0 ;i<D ;i++)
	{
		if (data[curr-1]==opp[i][0])
		{
			for (int j=0 ;j<curr-1 ;j++)
			{
				if (data[j]==opp[i][1])
				{
					curr = 0;
					return true;
				}
			}
		}
		if (data[curr-1]==opp[i][1])
		{
			for (int j=0 ;j<curr-1 ;j++)
			{
				if (data[j]==opp[i][0])
				{
					curr = 0;
					return true;
				}
			}
		}
	}

	return false;
}

void check ()
{
	bool combined = false;

	while (true)
	{
		if (check_combine())
			combined = true;
		else
			break;
	}

	if (!combined)
		check_opp();
}

int main ()
{

	cin >> T;

	for (cases = 1 ;cases<=T ;cases++)
	{
		cout << "Case #" << cases << ": ";

		cin >> C;

		for (int i=0 ;i<C ;i++)
		{
			cin >> combine[i];
		}

		cin >> D;

		for (int i=0 ;i<D ;i++)
		{
			cin >> opp[i];
		}

		cin >> N;

		curr = 0;
		while (N>0)
		{
			cin >> data[curr++];

			check ();

			N--;
		}

		cout << "[";
		for (int i=0 ;i<curr ;i++)
		{
			if (i>0)
				cout << ", ";

			cout << data[i];
		}

		cout << "]" << endl;
	}

	return 0;
}
