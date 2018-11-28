#include <iostream>
#include <fstream>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

int picked[505][505];

long long field[505][505];
int R, C;

long long rsums[505][505];
long long csums[505][505];

int do_things_row(const long long *psum, const int K, const int ROW)
{
	long long sum_to_sub = 0;
	long long esum = 0;
	long long sum_to_div = 0;
	long long qq = 0;
	long long vv = 0;
	//initial
	for(int i=1;i<K;++i)
	{
		sum_to_sub += psum[i];
		esum += 2*i*psum[i];
	}
	for(int tt=0;tt+K<=C;++tt, ++psum)
	{
		qq = field[ROW][tt+K-1] + field[ROW+K-1][tt+K-1];
		vv = field[ROW][tt] + field[ROW+K-1][tt];

		sum_to_div = sum_to_sub + psum[0] - qq - vv;

		if(esum - 2*(K-1)*qq == (K-1)*sum_to_div)
		{
			picked[ROW][tt]++;
			if(picked[ROW][tt] == 2)
			{return 1;}
		}
		//increment
		esum -= 2*sum_to_sub;
		sum_to_sub -= psum[1];
		sum_to_sub += psum[K];
		esum += 2*(K-1)*psum[K];
	}
	return 0;
}

int do_things_col(const long long *psum, const int K, const int COL)
{
	long long sum_to_sub = 0;
	long long sum_to_div = 0;
	long long esum = 0;
	long long qq = 0;
	long long vv = 0;
	//initial
	for(int i=1;i<K;++i)
	{
		sum_to_sub += psum[i];
		esum += 2*i*psum[i];
	}
	for(int tt=0;tt+K<=R;++tt, ++psum)
	{
		qq = field[tt+K-1][COL] + field[tt+K-1][COL+K-1];
		vv = field[tt][COL] + field[tt][COL+K-1];
		sum_to_div = sum_to_sub + psum[0] - qq - vv;

		if(esum - 2*(K-1)*qq == (K-1)*sum_to_div)
		{
			picked[tt][COL]++;
			if(picked[tt][COL] == 2)
			{return 1;}
		}
		//increment
		esum -= 2*sum_to_sub;
		sum_to_sub -= psum[1];
		sum_to_sub += psum[K];
		esum += 2*(K-1)*psum[K];
	}
	return 0;
}

bool has_size(const int K)
{
	memset(picked, 0, sizeof(picked));
	static long long arr[555];
	//row
	for(int i=0;i+K<=R;++i)
	{
		for(int j=0;j<C;++j)
		{
			arr[j] = csums[i+K][j] - csums[i][j];
		}
		do_things_row(arr, K, i);
	}
	for(int i=0;i+K<=C;++i)
	{
		for(int j=0;j<R;++j)
		{
			arr[j] = rsums[j][i+K] - rsums[j][i];
		}
		if(do_things_col(arr, K, i)){return true;}
	}
	return false;
}

int solve(void)
{
	memset(rsums, 0, sizeof(rsums));
	memset(csums, 0, sizeof(csums));
	for(int i=0;i<R;++i)
	{
		for(int j=0;j<C;++j)
		{
			rsums[i][j+1] = rsums[i][j] + field[i][j];
		}
	}
	for(int j=0;j<C;++j)
	{
		for(int i=0;i<R;++i)
		{
			csums[i+1][j] = csums[i][j] + field[i][j];
		}
	}
	for(int K=min(R,C);K>=3;--K)
	{
		if(has_size(K)){return K;}
	}
	return -1;
}


int main(int argc, char **argv)
{
	if(argc > 1){freopen(argv[1], "r", stdin);}
	int CNUM;
	cin >> CNUM;
	for(int cn=1;cn<=CNUM;++cn)
	{
		long long D;
		cin >> ::R >> ::C >> D;
		string s;
		for(int i=0;i<R;++i)
		{
			cin >> s;
			for(int j=0;j<C;++j)
			{
				field[i][j] = D + s[j]-'0';
			}
		}
		int x = solve();
		if(x != -1)
			printf("Case #%d: %d\n", cn, x);
		else
			printf("Case #%d: IMPOSSIBLE\n", cn);

	}
	return 0;
}
