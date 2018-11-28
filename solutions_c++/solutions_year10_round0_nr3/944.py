#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <sstream>
#include <queue>
#include <set>
#include <map>
#include <vector>
#include <complex>

#define mp make_pair
#define pb push_back
#define sqr(x) ((x)*(x))
#define foreach(it,c) for(typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)

using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int,int> PII;
typedef long long LL;
typedef complex<double> Point;

template<typename T> inline int size(const T &a) { return a.size(); }
template<typename T> inline bool operator<(const int &a,const vector<T> &b) { return a<b.size(); }

typedef vector<vector<LL> > Tmat;

vector<vector<LL> > matr,tmp,res;

void matmul(const Tmat &in1, const Tmat &in2, Tmat &tmp)
{
	int n = in1.size();
	tmp = Tmat(n, vector<LL>(n, 0));

	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n;j++)
		{
			for(int k=0;k<n;k++)
			{
				tmp[i][j] += in1[i][k] * in2[k][j];
			}
		}
	}
}

void matmull(vector<vector<LL> > &in, int mulx)
{
	res = matr;
	mulx--;

	while(mulx)
	{
		if( (mulx & 1))
		{
			matmul(res,matr,tmp);
			res.swap(tmp);
		}
		matmul(matr,matr,tmp);
		matr.swap(tmp);
		mulx >>= 1;
	}

	in.swap(res);
}

int trace(VI &g, int cur, int max, int &nn)
{
	nn=0;
	for(int i=cur;;i=(i+1)%size(g))
	{
		if(nn != 0 && i == cur)
			return i;

		nn += g[i];
		if(nn > max)
		{
			nn -= g[i];
			return i;
		}
	}
	return -1;
}

bool process(void)
{
	int R,k,N;
	vector<int> group;
	scanf("%d %d %d", &R, &k, &N);
	group.resize(N);
	for(int i=0;i<N;i++)
		scanf("%d", &group[i]);

	matr = vector<vector<LL> >(size(group)+1, vector<LL>(size(group)+1,0));
	for(int i=0;i<N;i++)
	{
		int sz = 0;
		int idx = trace(group, i, k, sz);
		matr[idx][i] = 1;
		matr[size(group)][i] = sz;
	}

	matr[size(group)][size(group)]=1;

	matmull(matr, R);

	cout << matr[size(group)][0] << endl;

	return true;
}

int main(void)
{
	int N;
	scanf("%d",&N);
	for(int i=1;i<=N;i++)
	{
		printf("Case #%d: ",i);
		process();
	}
	return 0;
}

