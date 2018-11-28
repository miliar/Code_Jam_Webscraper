#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct T
{
	int bg;
	int nd;
};

vector<vector<T> > mat; 
vector<T> add;

const bool cmp(const T &a, const T &b)
{
	return a.bg<b.bg || (a.bg==b.bg && a.nd<b.nd);
}

int solve()
{
	int i, j, k, d;
	int x1, x2, y1, y2;
	int r;
	bool alldie;
	T tmp;
	cin >>r;
	mat.resize(0);
	for(i=0; i<r; ++i)
	{
		cin >>x1 >>y1 >>x2 >>y2;
		if (y2>mat.size())
			mat.resize(y2);
		tmp.bg = x1;
		tmp.nd = x2;
		for (j=y1-1; j<=y2-1; ++j)
			mat[j].push_back(tmp);
	}
	for(i=0; i<mat.size(); ++i)
	{
		if (mat[i].size()==0)
			continue;
		sort(mat[i].begin(), mat[i].end(), cmp);
		tmp= mat[i].front();
		add.resize(0);
		for(j=1; j<mat[i].size(); ++j)
		{
			if ( tmp.nd < mat[i][j].bg-1)
			{
				add.push_back(tmp);
				tmp = mat[i][j];
			}
			else
			{
				tmp.nd = max(tmp.nd, mat[i][j].nd);
			}
		}
		add.push_back(tmp);
		swap(mat[i], add);
	}
	add.resize(mat.size());
	for( d=1; true; ++d)
	{
		alldie = true;
		for(i=mat.size()-1; i>=0; --i)
		{
			if (i==0 || mat[i-1].size()==0)
			{
				for(j=mat[i].size()-1; j>=0; --j)
					mat[i][j].bg++;
			}
			else
			{
				k= mat[i-1].size()-1;
				for(j=mat[i].size()-1; j>=0; --j)
				{
					while (k>0 && mat[i][j].nd+1<mat[i-1][k].bg)
						k--;
					if (mat[i][j].nd+1>=mat[i-1][k].bg 
						&& mat[i][j].nd+1<=mat[i-1][k].nd
						)
						mat[i][j].nd++;
				}

				k= mat[i-1].size()-1;
 				for(j=mat[i].size()-1; j>=0; --j)
				{
					while (k>0 && mat[i][j].bg<mat[i-1][k].bg)
						k--;
					if (mat[i][j].bg>mat[i-1][k].nd 
						|| mat[i][j].bg<mat[i-1][k].bg)
						mat[i][j].bg++;
				}
			}
		}
		for(i=0; i<mat.size(); ++i)
		{
			k=0;
			for(j=0; j<mat[i].size(); ++j)
				if (mat[i][j].bg<=mat[i][j].nd)
				{
					mat[i][k]= mat[i][j];
					k++;
				}
			mat[i].resize(k);
			k=0;
			for(j=0; j<mat[i].size(); ++j)
			{
				if (mat[i][k].nd+1==mat[i][j].bg)
				{
					mat[i][k].nd= mat[i][j].nd;
				}
				else
				{
					mat[i][k] = mat[i][j];
					k++;
				}
			}
			mat[i].resize(k);
			if (mat[i].size())
				alldie = false;
		}
		if (alldie)
			return d;
	}
}

int main()
{
	int i, t;
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin >> t;
	for (i=1; i<=t; ++i)
	{
		cout << "Case #" <<i << ": " <<solve() <<endl;
	}
	return 0;
}