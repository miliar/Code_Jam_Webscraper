#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <functional>
#include <map>
#include <set>
#include <math.h>
#include <stdio.h>
using namespace std;
FILE * in, * out;

int last(vector<int> & v)
{
	return v[v.size()-1];
}

__int64 go(vector<int> const & real, int n)
{
	vector<int> all(n);
	int i,j,k = real.size(),m;
	for(i=0;i<n;++i)
		all[i] = 1;
	__int64 res = 0;
	for(i=0;i<real.size();++i)
	{
		for(j=real[i];j<n;++j)
		{
			if(all[j]==1)
			{
				++res;
			}
			else break;				
		}
		for(j=real[i]-2;j>=0;--j)
		{
			if(all[j]==1)
			{
				++res;
			}
			else break;				
		}
		all[real[i]-1] = 0;
	}
	return res;
}

void solve(int test)
{
	int p, q, m, n, i;
	int begin, end;
	fscanf(in,"%d %d", &p, &q);
	vector<int> all(p), real(q);
	for(i=0;i<q;++i)
		fscanf(in, "%d", &real[i]);
/*	int res = 0;
	begin = 1; end = p;
	while(real.size()>0)
	{
		int x, y;
		x = real[0] - begin;
		y = -last(real) + end;
		if(x > y)
		{
			res += end - begin;
			begin = real[0]+1;
			if(real.size()==1) break;
			real.erase(real.begin());
		}
		else
		{
			res += end - begin;
			end = last(real) - 1;
			if(real.size()==1) break;
			real.erase(real.end()-1);
		}

	} */
	__int64 res = 1e18;
	do
	{
		res = min(res, go(real, p));
	}
	while(next_permutation(real.begin(), real.end()));
	fprintf(out, "Case #%d: %d\n", test, res);
	return;
}


int main()
{
	in = fopen("C-small.in", "r");
	out = fopen("C-small.out", "w+");
	int kol, n;
	fscanf(in,"%d", &kol);
	for(n=1;n<=kol;++n)
		solve(n);
	fclose(in);
	fclose(out);
}