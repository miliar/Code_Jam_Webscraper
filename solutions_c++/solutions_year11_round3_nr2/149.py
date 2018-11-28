#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;
typedef __int64 i64;

ifstream input("input.txt");
ofstream output("output.txt");

i64 min(i64 a, i64 b) { return (a<b)?a:b; }

int L, N, C;
i64 t, res;
int a[1000];
int r[1000000];
int nr;


int main()
{
	int T;
	input >> T;
	for (int z=0;z<T;++z)
	{
		input >> L >> t >> N >> C;
		for (int i=0;i<C;++i)
		{
			input >> a[i]; a[i]*=2;
		}
		nr = 0; res = 0;
		int ix = 0, k = 0;
		i64 add = 0;
		while (t && k<N)
			for (int i = 0; i<C && t && k<N; ++i)
			{
				ix = i;
				add = __min(t, a[i]);
				t -= add;
				res += add;
				++k;
			}

		if (a[ix]-add)
		{
			r[nr++] = a[ix]-(int)add;
			if (add==0) ++k;
		}
		if (++ix == C) ix=0;
		for (;ix<C && k<N;++ix)
		{
			r[nr++]=a[ix]; ++k;
		}

		while (k<N)
		{
			for (int i=0; i<C && k<N; ++i)
			{
				r[nr++] = a[i];
				++k;
			}
		}

		sort(r, r+nr);

		for (int j=nr-1; j>=0; --j)
		{
			if (L) { res+=r[j]/2; --L; }
			else res+=r[j];
		}
		output << "Case #" << z+1 << ": " << res << endl;
	}
	return 0;
}