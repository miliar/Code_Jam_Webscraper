#include <assert.h>
#include <iostream>
#include <ios>
#include <tr1/unordered_map>
#include <vector>
#include <fstream>
using namespace std;
using namespace std::tr1;

//ifstream in("B.ex");
istream& in = cin;
ostream& out = cout;

int sums[2 * 1024 * 1024];
int vec[1024 * 1024];

int until(int v)
{
	int r = 0;
	for(int i = 0; i < 32; ++i)
	{
		if(v & (1 << i))
		{
			r += sums[v];
			v -= 1 << i;
		}
	}
	return r;
}

void inc(int v)
{
	for(int i = 0; i <= 20; ++i)
	{
		if(v & (1 << i))
			v -= 1 << i;
		else
			++sums[v + (1 << i)];
	}
}

int advance(int p, int K, int n)
{
	int end;
start:
	end = (K - p) - (until(K) - until(p));
	if(n >= end)
	{
		p = 0;
		n -= end;
		goto start;
	}
	
	int l = p;
	int u = K;
	
	//(m - p) + until(m) - until(p) == n
	
	int target = p - until(p) + n;
	
	int m = l;
	for(;;)
	{
		m = (l + u) / 2;
		int v = m - until(m);
		if(v == target)
		{
			if(until(m + 1) == until(m))
				break;
			else
				l = m + 1;
		}
		else if(v < target)
			l = m + 1;
		else if(v > target)
			u = m;
	}
	
	assert(until(m + 1) == until(m));
		
	
	return m;
}

int main(int argc, char** argv)
{
	int N;
	in >> N;
	for(int cas = 0; cas < N; ++cas)
	{
		int K, n;
		
		in >> K >> n;
		int d[128];
		long long res;

		for(int i = 0; i < n; ++i)
		{
			in >> d[i];
		}
		
		memset(sums, 0, sizeof(sums));
		
		int p = 0;
		
		for(int i = 0; i < K; ++i)
		{
			p = advance(p, K, i);
			inc(p);
//			cerr << p << ' ' << until(p + 1) << ' ' << until(p) << endl;
			assert(until(p + 1) != until(p));
			vec[p] = i + 1;
			++p;
		}
		
		out << "Case #" << (cas + 1) << ":";
		
		for(int i = 0; i < n; ++i)
			out << ' ' << vec[d[i] - 1];
		
		out << endl;
	}
}

