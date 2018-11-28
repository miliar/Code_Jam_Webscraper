#include<iostream>

using namespace std;

int main()
{
	int T;
	cin >> T;

	for(int t = 1; t <= T; t++)
	{

		char combine[100][100];
		char opposed[100][100];
		for(int i = 0; i < 100; i++)
			for(int j = 0; j < 100; j++)
				combine[i][j] = opposed[i][j] = 0;


		int C;
		cin >> C;

		for(int c = 0; c < C; c++)
		{
			char c1, c2, c3;
			cin >> c1;
			cin >> c2;
			cin >> c3;
			combine[c1][c2] = c3;
			combine[c2][c1] = c3;
		}

		int D;
		cin >> D;
		for(int d = 0; d < D; d++)
		{
			char c1, c2, c3;
			cin >> c1;
			cin >> c2;
			opposed[c1][c2] = 1;
			opposed[c2][c1] = 1;
		}

		int N;
		cin >> N;
		char result[N];
		for(int n = 0; n < N; n++)
			result[n] = 0;

		cin >> result[0];
		int current_list_position = 0;
		for(int n = 1; n < N; n++)
		{
			char next;
			cin >> next;
			if(current_list_position >= 0)
			{
				char combination = combine[result[current_list_position]][next];
				if(combination > 0)
					result[current_list_position] = combination;
				else
					result[++current_list_position] = next;
			}
			else
				result[++current_list_position] = next;
		
			for(int m = 0; m <= current_list_position; m++)
				if(opposed[result[m]][result[current_list_position]] > 0)
					current_list_position = -1;
		}

		cout << "Case #" << t << ": ";
		cout << "[";
		for(int n = 0; n <= current_list_position; n++)
		{
			cout << result[n];
			if(n < current_list_position)
				cout << ", ";
		}
		cout << "]";
		cout << endl;
	}
}
