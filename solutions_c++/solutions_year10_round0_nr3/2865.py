#include <iostream>
#include <fstream>
#include <queue>

using namespace std;


int main() {
	ifstream inF;
	inF.open("C-small-attempt0.in");
	ofstream outF;
	outF.open("C-small-attempt0.out");


	int T;
	inF >> T;
	for (int tests = 0; tests < T; ++tests)
	{
		int R, k, N, toQ;
		deque<int> q;

		inF >> R >> k >> N;
		for(int g=0; g<N; ++g)
		{
			inF >> toQ;
			q.push_back(toQ);
		}

		int sumEuros = 0;
		for(int iter = 0; iter < R; ++iter)
		{
			deque<int> atRoller;
			int toGo = 0;
			
			while(!q.empty())
			{
				if (toGo + q.front() <= k)
				{
					toGo += q.front();
					atRoller.push_back(q.front());
					q.pop_front();
				} else break;
			}
			sumEuros += toGo;

			q.insert(q.end(), atRoller.begin(), atRoller.end());			
		}

		outF << "Case #" << tests+1 << ": " << sumEuros << endl;
	}

	inF.close();
	outF.close();
	return 0;
}