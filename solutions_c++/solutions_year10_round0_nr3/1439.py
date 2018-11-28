#include <iostream>
#include <fstream>
#include <cassert>
#include <vector>
using namespace std;

long long solve_themepark_case_naive(long long Rounds, long long kapacity, size_t N, const vector<long long> & groups)
{
	long long euros = 0;
	size_t next = 0;
	for (long long r = 0; r < Rounds; ++r)
	{
		long long thisround = 0;
		size_t start=next;
		while (thisround + groups[next] <= kapacity)
		{
			thisround += groups[next];
			next = (next+1) % N;
			if (next == start)
				break; //dimos toda la vuelta!
		}
		euros += thisround;
	}
	return euros;
}

long long solve_themepark_case(long long Rounds, long long kapacity, size_t N, const vector<long long> & groups)
{
	//precompute rides
	vector<long long> euros(N);
	vector<size_t> nextstart(N);
	for (size_t start = 0; start < N; ++start)
	{
		long long thisround = 0;
		size_t next = start;
		while (thisround + groups[next] <= kapacity)
		{
			thisround += groups[next];
			next = (next+1) % N;
			if (next == start)
				break; //dimos toda la vuelta!
		}
		euros[start] = thisround;
		nextstart[start] = next;
	}

	//simulate
	long long total_euros = 0;
	size_t next = 0;
	for (long long r = 0; r < Rounds; ++r)
	{
		total_euros += euros[next];
		next = nextstart[next];
	}
	return total_euros;
}

void solve_themepark(istream & in, ostream & out)
{
	int T;
	in >> T;
	for (int t = 1; t <= T; ++t)
	{
		long long Rounds, kapacity;
		size_t N;
		in >> Rounds >> kapacity >> N;
		vector<long long> groups(N);
		for (size_t i = 0; i < N; ++i)
			in >> groups[i];
		long long euros = solve_themepark_case(Rounds, kapacity, N, groups);
		out << "Case #" << t << ": " << euros << "\n";
	}
}

int main()
{
	assert(sizeof(long long) == 8);
	//ifstream in("C-sample.in");
	//ofstream out("C-sample.txt");

	//ifstream in("C-small-attempt0.in");
	//ofstream out("C-small-out.txt");

	ifstream in("C-large.in");
	ofstream out("C-large-out.txt");
	solve_themepark(in,out);

	return 0;
}