#include	<fstream>
#include	<vector>
#include	<cmath>
#include	<algorithm>
#include	<string>
#include	<climits>

using namespace	std;

ifstream	in("A-large.in");
ofstream	out("A-large.out");

int	arr[1002][102];

struct	T
{
	string	q;
	int	num;
};

int	main(int argc, char** argv)
{
	int	N, S, Q;
	int	i, j, k, m, mmin;
	string	tmp;
	in >> N;
	vector<string>	engines;
	vector<T>	querys;
	for(k = 1; k <= N; ++k)
	{
		memset(arr, 0, sizeof(arr));
		engines.clear();
		querys.clear();
		in >> S;
		getline(in, tmp);
		engines.resize(S);
		for(i = 0; i < S; ++i)
			getline(in, engines[i]);
		in >> Q;
		getline(in, tmp);
		querys.resize(Q);
		for(i = 0; i < Q; ++i)
		{
			getline(in, querys[i].q);
			for(j = 0; j < S; ++j)
				if(engines[j] == querys[i].q)
				{
					querys[i].num = j;
					break;
				}
		}
		if(Q != 0)
			arr[0][querys[0].num] = -1;
		for(i = 1; i < Q; ++i)
		{
			for(j = 0; j < S; ++j)
			{
				if(querys[i].num == j)
				{
					arr[i][j] = -1;
					continue;
				}
				if(arr[i-1][j] == -1)
				{
					mmin = INT_MAX;
					for(m = 0; m < S; ++m)
						if((arr[i-1][m] != -1) && (arr[i-1][m] < mmin))
							mmin = arr[i-1][m];
					arr[i][j] = mmin + 1;
				}
				else
					arr[i][j] = arr[i-1][j];
			}
		}
		if(Q != 0)
		{
			mmin = INT_MAX;
			for(j = 0; j < S; ++j)
				if((arr[Q-1][j] != -1) && (arr[Q-1][j] < mmin))
					mmin = arr[Q-1][j];
		}
		else
			mmin = 0;
		out << "Case #" << k << ": " << mmin << endl;
	}
	return	0;
}