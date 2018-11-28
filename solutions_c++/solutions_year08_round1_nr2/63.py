#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

struct request
{
	vector<int> zeros;
	int rem_id, rem_type;
};

int C, N, M;

int main()
{
	ifstream input;
	ofstream output;
	input.open("B-large.in");
	output.open("B-large.out");

	input >> C;
	for (int t = 0; t < C; t++)
	{
		input >> N;
		input >> M;
		vector<request> reqs(M);

		for (int i = 0; i < M; i++)
		{
			int num;
			input >> num;
			
			reqs[i].rem_type = 0;
			for (int j = 0; j < num; j++)
			{
				int id, type;
				input >> id >> type;
				id--;

				if (type == 1)
				{
					reqs[i].rem_id = id;
					reqs[i].rem_type = type;
				}
				else
					reqs[i].zeros.push_back(id);
			}
		}

		vector<int> ans(N);

		while (true)
		{
			bool done = true;

			for (int i = 0; i < M; i++)
				if (reqs[i].rem_type == 1)
				{
					int j = 0;
					while (j < (int)reqs[i].zeros.size() && ans[reqs[i].zeros[j]] == 1) j++;

					if (j == (int)reqs[i].zeros.size() && ans[reqs[i].rem_id] == 0)
					{
						ans[reqs[i].rem_id] = 1;
						done = false;
					}
				}

			if (done) break;
		}

		bool ok = true;

		for (int i = 0; i < M; i++)
			if (reqs[i].rem_type == 0)
			{
				int j = 0;
				while (j < (int)reqs[i].zeros.size() && ans[reqs[i].zeros[j]] == 1) j++;
				if (j == (int)reqs[i].zeros.size()) 
					ok = false;
			}

		output << "Case #" << t + 1 << ":"; 
		if (ok)
		{
			for (int i = 0; i < N; i++) 
				output << " " << ans[i];
			output << endl;
		}
		else
			output << " IMPOSSIBLE" << endl;
	}
}