#include <iostream>
#include <ios>
#include <fstream>
#include <tr1/unordered_map>
#include <vector>
using namespace std;
using namespace std::tr1;

istream& in = cin;
ostream& out = cout;

int M;
int C[16384];
int G[16384];
int I[16384];
int mem[16384][2];

int f(int n, int v);

#define INF 16384

int do_f(int n, int v)
{
	int l = 2 * n + 1;
	int r = 2* n + 2;
	
	int cand = !G[n] * (C[n] ? 1 : INF);
	int cor = G[n] * (C[n] ? 1 : INF);

	int res;
	if(v)
		res = min(cand + f(l, 1) + f(r, 1), min(cor + f(l, 0) + f(r, 1), min(cor + f(l, 1) + f(r, 0), cor + f(l, 1) + f(r, 1))));
	else
		res = min(cor + f(l, 0) + f(r, 0), min(cand + f(l, 0) + f(r, 1), min(cand + f(l, 1) + f(r, 0), cand + f(l, 0) + f(r, 0))));

	if(res >= INF)
		res = INF;

	return res;
}

int f(int n, int v)
{
	if(n >= (M - 1) / 2)
		return (I[n] == v) ? 0 : INF;
	else if(mem[n][v] >= 0)
		return mem[n][v];
	else
		return mem[n][v] = do_f(n, v);
}

int main(int argc, char** argv)
{
	int N;
	in >> N;
	for(int cas = 0; cas < N; ++cas)
	{
		int V;
		in >> M >> V;
		for(int i = 0; i < (M - 1)/2; ++i)
			in >> G[i] >> C[i];
		for(int i = (M - 1)/2; i < M; ++i)
			in >> I[i];
		memset(mem, 0xff, sizeof(mem));
		int res = f(0, V);
		out << "Case #" << (cas + 1) << ": ";
		if(res < INF)
			out << res;
		else
			out << "IMPOSSIBLE";
		out << endl;
	}
}

