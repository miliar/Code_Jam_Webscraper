#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

int P;
bool gone[100];

int getTime(const vector<int>& v)
{
	int ret = 0;
	for (int i=0; i<(int)v.size(); ++i)
	{
		gone[v[i]] = true;
		int loc = v[i]+1;
		while (loc < P && !gone[loc]) { ++ret; ++loc; }
		loc = v[i] - 1;
		while (loc>=0 && !gone[loc]) { ++ret; --loc; }
	}
	return ret;
}

int main()
{
	ifstream fin("C-small-attempt0.in");
	ofstream fout("C-small-attempt0.out");

	int N, Q;
	fin >> N;
	for (int i=1; i<=N; ++i)
	{
		fin >> P >> Q;
		vector<int> perm;
		for (int j=0; j<Q; ++j)
		{
			int temp; fin>>temp; perm.push_back(temp-1);
		}

		int ret = 9999999;
		while(true)
		{
			memset(gone, false, sizeof(gone));
			ret = min(ret, getTime(perm));
			if (!next_permutation(perm.begin(), perm.end()))
				break;
		}

		fout << "Case #" << i << ": " << ret << endl;
	}

	return 0;
}

