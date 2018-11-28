#include <fstream>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <functional>
#include <numeric>

using namespace std;

long main (long argc, char *argv[])
{
	if (argc < 2) return 1;
	ifstream file(argv[1]);
	if (!file) return 2;
	unsigned long num;
	file >> num;
	//	cout << num;
	unsigned long caseNum = 1;

	while ( caseNum <= num )
	{
		long p, k ,l;
		file >>p >>k >>l;
//		cout <<p <<' ' << k <<' ' <<l <<endl;
		vector<long> letters(l);
		for (long i=0; i<l; i++)
		{
			long lt;
			file >>lt;
//			cout <<lt <<endl;
			letters.push_back(lt);
		}
		sort(letters.begin(), letters.end(), greater<long>());
		long long total = 0ll;
		int j = 1;
		for (unsigned int i=0; i<letters.size(); i++)
		{
//			cout <<j <<' '<<letters[i] <<endl;
			total += j * letters[i];
			if ((i+1) % k == 0)
				j++;
		}

		cout <<"Case #" <<caseNum <<": ";
		cout <<total <<endl;
		caseNum++;
	}
	return 0;
}
