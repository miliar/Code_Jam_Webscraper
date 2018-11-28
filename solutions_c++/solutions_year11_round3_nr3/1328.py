// C2

#include <iostream>
#include <set>

using namespace std;

int main(int nargs, char** args)
{
	long T, N, L, H;
	long* notes;
	bool done;
	set<long> factors;
	long res;

	cin >> T;

	for(int t = 1; t <= T; ++t)
	{
		factors.clear();
		done = false;
		cin >> N >> L >> H;
		notes = (long*)calloc(N,sizeof(long));
		for(int n = 0; n < N; ++n)
		{
			cin >> notes[n];
		}

		for(long i = L; i <= H; ++i)
		{
			done = true;

			for( int n = 0; n < N; ++n)
			{
				if(!(i % notes[n] == 0 || notes[n] % i == 0))
				{
					done = false;
					break;
				}
			}

			if(done) {
				res = i;
				break;
			}
		}


		
		/*for(int n = 0; n < N; ++n)
		{
			for(int i=2; i <= notes[n]; i++) 
			{ 
				if(notes[n] % i == 0) 
				{ 
					factors.insert(i);
					notes[n] = notes[n]/i; 
					i--; 
					if(notes[n] == 1) 
						break; 
				} 
			} 
		}

		res = 1;
		for(set<int>::iterator it = factors.begin(); it != factors.end(); ++it)
		{
			res *= *it;
		}*/

		if(done && (res >= L && res <= H) )
		{
			cout << "Case #" << t << ": " << res << endl;
		}
		else
		{
			cout << "Case #" << t << ": NO" << endl;
		}

	//	free(notes);
	}

	return 0;
}