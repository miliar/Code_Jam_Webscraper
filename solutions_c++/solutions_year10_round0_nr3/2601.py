#include <iostream>
using namespace std;
int main(int argc, char **argv)
{
	int numcases, curcase;
	long R, k, N;
	long g[1001];
	long total = 0, cursum, curpos, curincpos;
	cin >> numcases;
	for (curcase = 0; curcase < numcases; curcase++)
	{
		cin >> R >> k >> N;
		for(int i = 0; i< N; i++ )
			cin >> g[i];
		total = 0;
		curpos = 0;
		for (int i = 0; i< R; i++)
		{
			cursum = 0;
			curincpos = 0;
			while (true)
			{
				if (cursum + g[curpos] > k) break;
				cursum += g[curpos++];
				curincpos++;
				curpos %= N;
				if (curincpos >= N) break;
			}
			total += cursum;
		}
		cout << "Case #"<< curcase+1 <<": " << total << endl;
	}
	return 0;
}
