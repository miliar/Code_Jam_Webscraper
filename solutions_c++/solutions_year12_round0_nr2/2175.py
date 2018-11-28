#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char **argv)
{
	if(argc != 2)
	{
		cout << "Wrong args" << endl;
		return 1;
	}

	ifstream f(argv[1]);
	ofstream o("boutput.txt", ofstream::out);

	int T;
	f >> T;

	for(int i = 0 ; i < T; i++)
	{
		int N, S, p, t;
		f >> N;
		f >> S;
		f >> p;
		int minNoSurprise = p-1 + p-1 + p;
		int minSurprise = p-2 + p-2 + p;

		if(p == 0)
		{
			minNoSurprise = 0;
			minSurprise = 0;
		}
		if(p == 1)
		{
			minSurprise = 2;
			minNoSurprise = 1;
		}

		int result = 0;
		for(int j = 0; j < N; j++)
		{
			f >> t;
			if(t == 0 && minNoSurprise == 0)
			{
				result++;
			}
			else if( t > 0 && t >= minNoSurprise) result++;
			else if( t > 0 && t >= minSurprise && S > 0)
			{
				result++;
				S--;
			}
		}

		o << "Case #" << i+1 << ": " << result << endl;
	}

	return 0;
}
