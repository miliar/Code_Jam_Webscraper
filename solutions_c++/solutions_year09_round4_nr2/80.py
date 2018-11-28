#include <vector>
#include <algorithm>
#include <math.h>
#include <string>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <utility>
#include <numeric>
#include <fstream>

using namespace std;

#define		ALL(c)	(c).begin(),(c).end()
#define		SZ(c)	int((c).size())
#define		LEN(s)	int((s).length())
#define		FOR(i,n)	for(int i=0;i<(n);++i)
#define		FORD(i,a,b)	for(int i=(a);i<=(b);++i)
#define		FORR(i,a,b)	for(int i=(b);i>=(a);--i)
#define		MP	make_pair
#define		PB	push_back

typedef istringstream iss;
typedef ostringstream oss;
typedef long double ld;
typedef long long i64;
typedef pair<int,int> pii;

typedef vector<i64> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<vvvi> vvvvi;

int R, C, F;
vector<string> A;
int f[10][6][1<<6][1<<6];
int W[12];

struct vrtx
{
	int r, c, msk1, msk2;
};

int& fff(vrtx& v)
{
	return f[v.r][v.c][v.msk1][v.msk2];
}

int fall(int r, int c, int msk)
{
	if (msk & (1<<c)) return 0;
	int cnt = 1;
	FORD(i, r+2, R-1)
	{
		if (A[i][c] == '#') break;
		++cnt;
	}
	return cnt;
}

int main()
{
	ifstream fin("B.in"); ofstream fout("B.out");
	int T;
	fin >> T;
	FOR(tt, T)
	{
		fin >> R >> C >> F;
		A.resize(R);
		FOR(i, R) fin >> A[i];

		FOR(i, R) FOR(j, C) 
			FOR(msk1, 1<<C) FOR(msk2, 1<<C) f[i][j][msk1][msk2] = 10000000;

		FOR(i, R)
		{
			W[i] = 0;
			FOR(j, C) if (A[i][j] == '#') W[i] += (1<<j);
		}
		W[R] = 0;

		vrtx v;
		v.r = 0;
		v.c = 0;
		v.msk1 = W[0];
		v.msk2 = W[1];

		deque<vrtx> deq;
		deq.push_back(v);
		fff(v) = 0;

		int res = -1;

		while (!deq.empty())
		{
			v = deq.front();
			deq.pop_front();

			if (v.r == R-1)
			{
				res = fff(v);
				break;
			}

			if (v.c < C-1 && (v.msk1 & (1<<(v.c+1))) == 0 && (v.msk2 & (1<<(v.c+1))) != 0)
			{
				vrtx nv;
				nv.r = v.r;
				nv.c = v.c;
				nv.msk1 = v.msk1;
				nv.msk2 = v.msk2 ^ (1<<(v.c+1));
				if (fff(nv) > fff(v)+1)
				{
					deq.push_back(nv);
					fff(nv) = fff(v)+1;
				}
			}

			if (v.c > 0 && (v.msk1 & (1<<(v.c-1))) == 0 && (v.msk2 & (1<<(v.c-1))) != 0)
			{
				vrtx nv;
				nv.r = v.r;
				nv.c = v.c;
				nv.msk1 = v.msk1;
				nv.msk2 = v.msk2 ^ (1<<(v.c-1));
				if (fff(nv) > fff(v)+1)
				{
					deq.push_back(nv);
					fff(nv) = fff(v)+1;
				}
			}

			if (v.c < C-1 && (v.msk1 & (1<<(v.c+1))) == 0)
			{
				int fd = fall(v.r, v.c+1, v.msk2);
				if (fd <= F)
				{
					vrtx nv;
					nv.r = v.r + fd;
					nv.c = v.c + 1;
					if (fd == 0)
					{
						nv.msk1 = v.msk1;
						nv.msk2 = v.msk2;
					}
					else if (fd == 1)
					{
						nv.msk1 = v.msk2;
						nv.msk2 = W[nv.r+1];
					}
					else
					{
						nv.msk1 = W[nv.r];
						nv.msk2 = W[nv.r+1];
					}

					if (fff(nv) > fff(v))
					{
						deq.push_front(nv);
						fff(nv) = fff(v);
					}
				}
			}

			if (v.c > 0 && (v.msk1 & (1<<(v.c-1))) == 0)
			{
				int fd = fall(v.r, v.c-1, v.msk2);
				if (fd <= F)
				{
					vrtx nv;
					nv.r = v.r + fd;
					nv.c = v.c - 1;
					if (fd == 0)
					{
						nv.msk1 = v.msk1;
						nv.msk2 = v.msk2;
					}
					else if (fd == 1)
					{
						nv.msk1 = v.msk2;
						nv.msk2 = W[nv.r+1];
					}
					else
					{
						nv.msk1 = W[nv.r];
						nv.msk2 = W[nv.r+1];
					}

					if (fff(nv) > fff(v))
					{
						deq.push_front(nv);
						fff(nv) = fff(v);
					}
				}
			}
		}

		if (res == -1)
		{
			fout << "Case #" << tt+1 << ": No" << endl;
			cout << "Case #" << tt+1 << ": No" << endl;
		}
		else
		{
			fout << "Case #" << tt+1 << ": Yes " << res << endl;
			cout << "Case #" << tt+1 << ": Yes " << res << endl;
		}
	}
	return 0;	
}
