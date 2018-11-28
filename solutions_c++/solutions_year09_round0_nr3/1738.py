#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

int main(int argc, char *argv[])
{
	unsigned long long paths[512];
	unsigned long long total;
	
	int N;
	cin >> N;
	
	string phrase = "welcome to code jam";
	//string phrase = "bcb";
	int np = phrase.length();
	
	for (int n = 1; n <= N; n++)
	{
		string s;
		if (n == 1) getline(cin, s); // Clear out getline firs ttime
		getline(cin, s);
		int ns = s.length();
		int error = 0;
		
		for (int i = 0; i < 512; i++)
		{
			paths[i] = 0ULL;
		}
		
		// Find paths from from end to beginning of phrase
		for (int pidx = np - 1; pidx > 0; pidx--)
		{
			// Find lower bound in s
			int pidx2 = 0;
			int lower_iter = -1;
			//cout << "Iteration for pidx = " << pidx << endl;
			for (int lower = 0; lower < ns; lower++)
			{
				if (pidx2 == pidx - 1)
				{
					lower_iter = lower;
					break;
				}
				if (s[lower] == phrase[pidx2])
					pidx2++;
			}
			//cout << "2";
			if (lower_iter == -1)
			{
				error = 1;
				break;
			}
			//cout << "3";
			int upper_iter = -1;
			pidx2 = np - 1;
			for (int upper = ns - 1; upper >= 0; upper--)
			{
				if (pidx2 == pidx)
				{
					upper_iter = upper;
					break;
				}
				if (s[upper] == phrase[pidx2])
					pidx2--;
			}
			//cout << "4";
			if (upper_iter == -1)
			{
				error = 1;
				break;
			}
			//cout << "5";
			//cout << "Lower bound " << lower_iter << " Upper bound " << upper_iter << endl;
			// We now have our bounds

			unsigned long long counter = 0;
			for (int i = upper_iter; i >= lower_iter; i--)
			{
				//cout << "Comparing " << s[i] << " with " << phrase[pidx] << endl;
				if (s[i] == phrase[pidx])
				{
					if (pidx == np - 1)
					{
						counter += 1ULL;
					}
					else
					{
						counter += paths[i];
					}
				}
				//cout << "Comparing " << s[i] << " with " << phrase[pidx-1] << endl;
				if (s[i] == phrase[pidx - 1])
				{
					paths[i] += counter;
				}
				//cout << "Counter is " << counter << endl;
			}
			
			/*cout << "Array is now: ";
			for (int i = 0; i < ns; i++)
				cout << paths[i] << " ";
			cout << endl;*/
		}
		
		total = 0;
		if (error != 1)
		{
			for (int i = 0; i < ns; i++)
			{
				if (s[i] == phrase[0])
					total += paths[i];
			}
		}
		
		printf("Case #%d: %04d\n", n, total % 10000);
		//cout << "Case #" << n << ": " << total%10000 << endl;
		
		total = 0ULL;
		
	}
	
	return 0;
}
