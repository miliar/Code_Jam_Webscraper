#include <iostream>
#include <vector>
#include <algorithm>
using std::cin;
using std::cout;
using std::cerr;
using std::vector;
using std::min;
using std::max;

typedef vector<int> VI;
typedef vector<VI> VVI;

typedef vector<bool> VB;
typedef vector<VB> VVB;

VI res;
VVB sq;
VVB used;

VVI hmark;
VVI vmark;

void bvis(const  VVB & sqr)
{
	for(unsigned i = 0 ; i < sqr.size(); i++)
	{
		for(unsigned j = 0; j < sqr[i].size(); j++)
			cerr << sqr[i][j];
		cerr << '\n';
	}
}

void mvis(const VVI & sqr)
{
	for(unsigned i = 0 ; i < sqr.size(); i++)
	{
		for(unsigned j = 0; j < sqr[i].size(); j++)
			cerr << sqr[i][j] << ' ';
		cerr << '\n';
	}
}

void mark()
{
	int m = sq.size();
	int n = sq[0].size();

	for(int i = 0 ; i < m; i++)
		for(int j = 0; j < n; j++)
		{
			bool next = !sq[i][j];
			bool fail = false;
			int k;
			for(k = j+1; k < n; k++)
			{
				if(sq[i][k] != next)
				{
					fail = true;
					break;
				}
				next = !next;
			}
			hmark[i][j] = k-j;
		}

	for(int i = 0 ; i < n; i++)
		for(int j = 0; j < m; j++)
		{
			bool next = !sq[j][i];
			bool fail = false;
			int k;
			for(k = j+1; k < m; k++)
			{
				if(sq[k][i] != next)
				{
					fail = true;
					break;
				}
				next = !next;
			}
			vmark[j][i] = k-j;
		}



}


void wack(int x, int y, int sz)
{
	// pee on pros
	for(int i = x; i < x+sz; i++)
		for(int j = y; j < y+sz; j++)
			if(used[i][j])
				return;

				
	for(int i = x; i < x+sz; i++)
		for(int j = y; j < y+sz; j++)
			used[i][j] = true;
//	cerr << x << ' ' << y << ' ' << sz << '\n';
	res[sz]++;
}

int main()
{
	int c;
	cin >> c;
	for(int ccc = 0; ccc < c; ccc++)
	{
		int m, n;
		cin >> m >> n;
		
		sq = VVB(m, VB(n));
		used = VVB(m, VB(n, false));

		vmark = VVI(m, VI(n, 0));
		hmark = VVI(m, VI(n, 0));

		for(int i = 0 ; i < m ;i++)
			for(int j = 0 ; j < n/4; j++)
			{
				char hx;
				cin >> hx;
				if(hx > '9')
					hx = 10 + (hx - 'A');
				else
					hx = hx - '0';

				for(int k = 3; k >= 0; k--)
				{
					int rj = j*4 + (3 -k);
					int val = (hx & (1<<k)) >> k;
					sq[i][rj] = val;
				}
			}


		if(ccc == 6)
			bvis(sq);
//		bvis(used);
//		cerr << "$$\n";

		int max_bs = min(m,n);
//		cerr << max_bs << "bs\n";
		res = VI(max_bs+1, 0);
///////////////////////

		mark();
//		mvis(hmark);
//		cerr << "$$\n";
//		mvis(vmark);
///////////////////////

	for(int sz = max_bs; sz > 0; sz--)
	{
		for(int i = 0 ; i < m; i++)
			for(int j = 0; j < n; j++)
			{
				if(used[i][j])
					continue;
				
				bool ok = true;
				for(int k = 0; k < sz; k++)
				{
					if(hmark[i+k][j] < sz)
					{
						ok =false;
						break;
					}
					if(vmark[i][j+k] < sz)
					{
						ok =false;
						break;
					}
				}

				if(ok)
					wack(i,j,sz);
			}
	}

///////////////////////
		int r = 0;
		for(int i = res.size() -1; i >0; i--)
			if(res[i] != 0)
				r++;
/*
		if(n == 1)
			res[1] = m;
		if(m == 1)
			res[1] = n;
*/

		cout << "Case #" << (ccc+1) << ": " << r <<  "\n";
		for(int i = res.size() -1; i >0; i--)
			if(res[i] != 0)
				cout << i << ' ' << res[i] << "\n";
	}
	return 0;
}

