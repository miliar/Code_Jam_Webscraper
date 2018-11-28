#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


// TODO's:  
// SeanAdd
// PatrickAdd

// Generate Permutations
// PatrickAdd each permutation:
//   for each OK:
//     SeanAdd, keep highest

typedef vector<int> bag;
typedef bag::iterator bagit;

int SeanAdd(bag& sean, bag& patrick)
{
	int sums = 0;
	int sump = 0;
	for(bagit it = sean.begin(); it != sean.end(); ++it)
	{
		sums += *it;
	}
	for(bagit it = patrick.begin(); it != patrick.end(); ++it)
	{
		sump += *it;
	}


	return (sums > sump)?sums:sump;
}
bool PatrickAdd(bag& sean, bag& patrick)
{
	int sums = 0;
	int sump = 0;
	for(bagit it = sean.begin(); it != sean.end(); ++it)
	{
		sums = sums ^ *it;
	}
	for(bagit it = patrick.begin(); it != patrick.end(); ++it)
	{
		sump = sump ^ *it;
	}

	return sums == sump;
}

int CheckLevel(int level, bag sean, bag patrick, int N)
{
	int maxAtLevel = 0;
	int val = 0;

	bagit it;

	if(level > 0 && PatrickAdd(sean, patrick))
	{
		maxAtLevel = SeanAdd(sean,patrick);
	}

	if(level < N-1)
	{
		for(int n = N-level-1; n >= level ; --n)
		{
			patrick.push_back(sean[n]);
			for(it = sean.begin(); it != sean.end(); ++it)
			{
				if (*it == patrick.back())
				{
					sean.erase(it);
					break;
				}
			}

			val = CheckLevel(level+1,sean,patrick,N);
			if(val > maxAtLevel)
				maxAtLevel = val;

			sean.push_back(patrick.back());
			patrick.pop_back();

		}
	} 

	return maxAtLevel;
}

int main(int nargs, char** args)
{
	int T;
	int N;
	bag b;
	int candy;
	char tmp[100];

	int result = 0;

	cin >> T;

	for(int t = 1; t <= T; ++t)
	{
		b.clear();
		result = 0;

		cin >> N;

		for(int n = 0; n < N; ++n)
		{
			cin >> candy;
			b.push_back(candy);
		}

		result = CheckLevel(0,b, bag(), N);

		cout << "Case #" << t << ": " << ((result > 0)?itoa(result,tmp,10):"NO") << endl;
	}

	return 0;
}