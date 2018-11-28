#include <iostream>
#include <ios>
#include <fstream>
#include <tr1/unordered_map>
#include <vector>
using namespace std;
using namespace std::tr1;

istream& in = cin;
ostream& out = cout;

int N, M, A;

char products[10000 * 10000 + 256];
short prodx[10000 * 10000 + 256];
short prody[10000 * 10000 + 256];

int main(int argc, char** argv)
{
	int cases;
	in >> cases;
	for(int cas = 0; cas < cases; ++cas)
	{
		int V;
		in >> N >> M >> A;

		memset(products, 0, sizeof(products));
		for(int i = 0; i <= N; ++i)
		{
			for(int j = 0; j <= M; ++j)
			{
				if(!products[i * j])
				{
					products[i * j] = 1;
					prodx[i * j] = i;
					prody[i * j] = j;
				}
			}
		}
		
		int mp = N * M;
		
		int v;

		out << "Case #" << (cas + 1) << ": ";
		
		bool ok = false;
		
		for(int v = A; v <= mp; ++v)
		{
			int v2 = v - A;
			if(products[v] && (v2 <= mp) && products[v2])
			{
				out << "0 0 " << prodx[v] << ' ' << prody[v2] << ' ' << prodx[v2] << ' ' << prody[v] << endl;
				ok = true;
				break;
			}
		}
		
		if(!ok)
			out << "IMPOSSIBLE" << endl;
	}
}

