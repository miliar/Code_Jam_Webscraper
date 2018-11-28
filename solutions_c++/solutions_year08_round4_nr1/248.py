#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <fstream>
#include <vector>
#include <set>
#include <complex>
#include <map>
#include <algorithm>
#include <functional>
#include <cstdlib>
#include <cmath>
using namespace std;

ifstream fin("A.in");
ofstream fout("A.out");
const double EPS = 1e-10;

vector<bool> vals, chg;
vector<int> res;
int M, V;

int main(void)
{
	int N;
	fin >> N;
	for (int tc = 1; tc <= N; tc++)
	{
		fin >> M >> V;
		res.resize(M);
		vals.resize(M);
		chg.resize(M);
		for (int i = 0; i < (M-1)/2; i++)
		{
			int G, C;
			fin >> G >> C;
			G = G ^ V;
			vals[i] = (bool)G;
			chg[i] = (bool)C;
		}
		for (int i = (M-1)/2; i < M; i++)
		{
			int I;
			fin >> I;
			I = I ^ V;
			vals[i] = (bool)I;
			chg[i] = false;
			res[i] = -I;
		}
		for (int i = (M-1)/2 - 1; i >= 0; i--)
		{
			res[i] = M+1;
			if ((res[i*2+1]!=-1)&&(res[i*2+2]!=-1)) res[i] = min(res[i], res[i*2+1]+res[i*2+2]);
			if (((chg[i])||(vals[i]))&&((res[i*2+1]!=-1)||(res[i*2+2]!=-1)))
				res[i] = min(res[i], ((vals[i])?0:1)+(int)min((unsigned)res[i*2+1], (unsigned)res[i*2+2]));
			if (res[i] == M+1) res[i] = -1;
		}
		fout << "Case #" << tc << ": ";
		if (res[0]==-1)
			fout << "IMPOSSIBLE" << endl;
		else
			fout << res[0] << endl;
	}
	return 0;
}
