#include <iostream>
#include <vector>
#include <string>
#include <set>
using namespace std;

typedef long long hashtype;
const long long prime = 999983;
hashtype getHash (const string& s)
{
	hashtype res = 0;
	for (int i = 0; i < s.length (); ++i)
		res = res*prime + s[i];
	return res;
}

int getLastEncounter (const vector<hashtype>& names, const vector<hashtype>& queries, int from)
{
	int mx = -1;
	int left = names.size ();
	set<hashtype> encountered;

	for (int j = from; j < queries.size (); ++j)
	{
		if (encountered.find (queries[j]) == encountered.end ())
		{
			mx = j;
			--left;
			encountered.insert (queries[j]);
		}
	}

	return (left > 0 ? queries.size () : mx);
}

int main (int argc, char* argv[])
{
	if (argc >= 2)
		freopen (argv[1], "r", stdin);
	if (argc >= 3)
		freopen (argv[2], "w", stdout);

	int N;
	cin >> N;
	for (int j = 0; j < N; ++j)
	{
		int S;
		cin >> S;

		string dummy;
		getline (cin, dummy);
		vector<hashtype> names (S);
		for (int i = 0; i < S; ++i)
		{
			getline (cin, dummy);
			names[i] = getHash (dummy);
		}

		int Q;
		cin >> Q;

		getline (cin, dummy);
		vector<hashtype> queries (Q);
		for (int i = 0; i < Q; ++i)
		{
			getline (cin, dummy);
			queries[i] = getHash (dummy);
		}

		int from = 0, swaps = 0;
		while ( (from = getLastEncounter (names, queries, from)) != queries.size ())
			++swaps;

		cout << "Case #" << j + 1 << ": " << swaps << '\n';
	}
	return 0;
}