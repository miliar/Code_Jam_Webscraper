#include <iostream>
#include <fstream>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <sstream>
#include <math.h>

using namespace std;

int r[1010][110];
map<string, int> engine;
int e[1010];
int N,s,q;

#define filein "input.txt"
#define fileout "output.txt"

int getres()
{
	memset(r, 0, sizeof r);
	int i,j;
	for (i=1; i<=s; i++)
		r[q+1][i] = 1000000;
	for (i=q; i>=0; i--)
		for (j=1; j<=s; j++)
			if (e[i] != j)
				r[i][j] = r[i+1][j]+1;
			else
				r[i][j] = 0;
	int res = -1;
	int cure = 0;
	int pos = 0;
	e[0] = 0;
	for (pos = 0; pos <= q; pos++)
		if (e[pos] == cure)
		{
			res++;
			for (i=1; i<=s; i++)
				if (r[pos][cure] < r[pos][i])
					cure = i;		
		}
	return res;
}

int main()
{
	ifstream in(filein);
	ofstream out(fileout);
	
	in >> N;
	char buf[1000];
	in.getline(buf, 1000);

	for (int o = 1; o <= N; o++)
	{
		engine.clear();
		int res = 0;		
		in >> s;
		in.getline(buf, 1000);
		int i;
		string t;
		for (i=1; i<=s; i++)
		{
			in.getline(buf, 1000);
			t = buf;
			engine[t] = i;
		}
		in >> q;
		in.getline(buf, 1000);
		for (i=1; i<=q; i++)
		{
			in.getline(buf, 1000);
			t= buf;
			e[i] = engine[t];
		}
		res = getres();
		out << "Case #"<<o<<": " << res << endl;
	}

	return 0;
}