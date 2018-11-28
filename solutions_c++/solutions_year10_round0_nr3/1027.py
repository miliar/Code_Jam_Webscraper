#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

class note
{
private:
	unsigned int _next;
	long long _amount;
public:
	unsigned int next (void) { return _next; }
	long long amount (void) { return _amount; }
	note (unsigned int next, long long amount) : _next(next), _amount(amount) { }
};

int
main (
	int argc,
	char **argv
) {
	if (argc < 2)
	{
		cerr << "no input data specified." << endl;
		return -1;
	}

	fstream fin(argv[1], ios::in);

	int T;
	fin >> T;

	for (int t = 0; t < T; t++)
	{
		cout << "Case #" << (t + 1) << ": ";

		long long R, k, N;
		fin >> R >> k >> N;

		//cerr << "R: " << R << ", k: " << k << ", N: " << N << endl;

		vector< long long > groups;
		for (unsigned int n = 0; n < N; n++)
		{
			long long buffer;
			fin >> buffer;
			groups.push_back(buffer);
		}

		vector< note > notes;
		for (unsigned int n = 0; n < N; n++)
		{
			unsigned int next = n;
			long long amount = 0;
			for (unsigned int m = 0; m < N; m++)
			{
				unsigned int _next = ((n + m) % N);
				long long tmp = groups[_next];
				if (amount + tmp > k)
				{
					next = _next;
					break;
				}

				amount += tmp;
			}
			notes.push_back(note(next, amount));
		}

		long long result = 0;
		unsigned int current = 0;
		for (int r = 0; r < R; r++)
		{
			result += notes[current].amount();
			current = notes[current].next();
		}
		cout << result;

		cout << endl;
	}

	fin.close();

	return 0;
}
