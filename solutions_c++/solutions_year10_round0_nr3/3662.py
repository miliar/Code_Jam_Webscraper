#include <iostream>
using namespace std;

int groups[1000];
int cur_i;

int getCur()
{
	return groups[cur_i];
}

void incCur(int N)
{
	if (cur_i + 1 >= N)
		cur_i = 0;
	else
		cur_i++;
}

int money(int R, int k, int N)
{
	int money = 0;
	cur_i = 0;
	for (int i = 0; i < R; i++)
	{
		int pass = 0;
		int first = cur_i;
		while (pass + getCur() <= k)
		{
			pass += getCur();
			//cout << pass << endl;
			incCur(N);
			if (first == cur_i)
				break;
		}
		money += pass;
	}
	return money;
}



int main()
{
	int T;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		int R, k, N;
		cin >> R >> k >> N;
		for (int j = 0; j < N; j++)
			cin >> groups[j];
		cout << "Case #" << i + 1 << ": " << money(R, k, N) << endl;
	}
}
