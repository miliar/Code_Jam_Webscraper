#include <iostream>
#include <ios>
#include <sstream>
#include <iomanip>
#include <queue>
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

string time_str(int t)
{
	ostringstream ss;
	ss << setw(2) << setfill('0') << (t / 60) << ":" << setw(2) << setfill('0') << (t % 60);
	return ss.str();
}

int main(int argc, char** argv)
{
	int N;
	in >> N;
	for(int cas = 0; cas < N; ++cas)
	{
		typedef pair<int, pair<int, int> > ev_t;
		priority_queue<ev_t, vector<ev_t>, greater<ev_t> > q;
		
		int T, N[2];
		in >> T >> N[0] >> N[1];
		for(int e = 0; e < 2; ++e)
		{
			for(int i = 0; i < N[e]; ++i)
			{
				int a, b, c, d;
				char k0, k1;
				in >> a >> k0 >> b >> c >> k1 >> d;
//				cerr << a << ' ' << b << ' ' << c << ' ' << d << endl;
				q.push(make_pair(a * 60 + b, make_pair(e, c * 60 + d + T)));
			}
		}
		
		int t[2] = {0, 0};
		int avail[2] = {0, 0};
		
		while(!q.empty())
		{
			ev_t ev = q.top();
			q.pop();
			int e = ev.second.first;
			int arr = ev.second.second;
//			cerr << time_str(ev.first) << " at " << e << ": " << t[0] << ' ' << t[1] << ' ' << avail[0] << ' ' << avail[1] << endl;
			if(arr < 0)
			{
				++avail[e];
				//cerr << "\ttrain arrived" << endl;
			}
			else
			{
				if(avail[e])
					--avail[e];
				else
				{
					++t[e];
					//cerr << "\tcreating new train" << endl;
				}

				q.push(make_pair(arr, make_pair(!e, -1)));
				//cerr << "\ttrain leaving, arriving at " << time_str(arr) << endl;
			}
		}
		
		out << "Case #" << (cas + 1) << ": " << t[0] << ' ' << t[1] << endl;
	}
}

