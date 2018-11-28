#include <iostream>
#include <ios>
#include <tr1/unordered_map>
using namespace std;
using namespace std::tr1;

istream& in = cin;
ostream& out = cout;

int q[1024];
int Q;
int S;

short mem[1024][128];

int f(int i, int s);

int do_f(int i, int s)
{
	if(i == Q)
		return 0;
	if(q[i] != s)
		return f(i + 1, s);
	else
	{
		int ret = INT_MAX;
		for(int j = 0; j < S; ++j)
		{
			if(j != s)
				ret = min(ret, 1 + f(i + 1, j));
		}
		return ret;
	}
}

int f(int i, int s)
{
	if(mem[i][s] >= 0)
		return mem[i][s];
	else
		return mem[i][s] = do_f(i, s);
}

int main(int argc, char** argv)
{
	int N;
	in >> N;
	for(int cas = 0; cas < N; ++cas)
	{
		unordered_map<string, int> se_map;
		int nse = 0;

		in >> S;
		for(int si = 0; si < S; ++si)
		{
			string se;
			in >> ws;
			getline(in, se);
			se_map[se] = nse++;
		}
		in >> Q;

		for(int qi = 0; qi < Q; ++qi)
		{
			string qs;
			in >> ws;
			getline(in, qs);
			q[qi] = se_map[qs];
		}
		
		memset(mem, 0xff, sizeof(mem));
		
		int res = INT_MAX;
		for(int start = 0; start < S; ++start)
		{
			res = min(res, f(0, start));
		}
		
		out << "Case #" << (cas + 1) << ": " << res << endl;
	}
}

