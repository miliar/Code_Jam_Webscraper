#include <iostream>
#include <cmath>

using namespace std;

typedef struct
{
	char color;
	int label;
} Cmd;

int main ()
{
	int T, N;
	int cases;

	cin >> T;

	for (cases=1 ;cases<=T ;cases++)
	{
		cin >> N;
		Cmd data[110];
		for (int i=0 ;i<N ;i++)
			cin >> data[i].color >> data[i].label;

		int O_pos = 1;
		int B_pos = 1;
		int O_quota = 0;
		int B_quota = 0;
		int total_step = 0;

		for (int i=0 ;i<N ;i++)
		{
			int sum = 0;
			if (data[i].color=='O')
			{
				sum = abs(data[i].label - O_pos);
				if (sum >= O_quota)
				{
					sum -= O_quota;
					total_step += sum;
					B_quota += sum;
				}

				O_pos = data[i].label;
				total_step++;
				B_quota++;
				O_quota = 0;
			}
			else
			{
				sum = abs(data[i].label - B_pos);
				if (sum >= B_quota)
				{
					sum -= B_quota;
					total_step += sum;
					O_quota += sum;
				}

				B_pos = data[i].label;
				total_step++;
				O_quota++;
				B_quota = 0;
			}


	//		cout << O_quota << " " << B_quota << " " << total_step << endl;
		}

		cout << "Case #" << cases << ": " << total_step << endl;
	}
	return 0;
}
