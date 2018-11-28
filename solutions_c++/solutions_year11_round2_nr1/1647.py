#include <algorithm>
#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <map>
#include <cmath>
#include <cstdlib>
#include <cstdio>

using namespace std;

#define FORI(_i, _j, _size) for (size_t _i = _j; _i < _size; ++_i)
#define FORI1(_i, _j, _size, _inc) for (size_t _i = _j; _i < _size; _i += _inc)
#define FORVI(_i, _j, _v) FORI(_i, _j, _v.size())
#define FORVI1(_i, _j, _v, _inc) FORI1(_i, _j, _v.size(), _inc)
#define FOR(_i, _size) FORI(_i, 0, _size)
#define FOR1(_i, _size, _inc) FORI1(_i, 0, _size, _inc)
#define FORV(_i, _v) FOR(_i, _v.size())
#define FORV1(_i, _v, _inc) FOR1(_i, _v.size(), _inc)
#define MEMZ(_array) memset(_array, 0, sizeof(_array))
#define OUT(_i, _n) cout << "Case #" << _i << ": " << _n << endl 

int main()
{

  int T;
  cin >> T;

  FOR(__t, T)
  {
    int N;
    cin >> N;

    int a[N][N];
    double wp[N];
    double owp[N];
    int wonA[N];
    int lostA[N];
    double sumOwp = 0;
    MEMZ(a);
    MEMZ(wonA);
    MEMZ(lostA);

    FOR(__n, N)
    {
      long long won = 0;
      long long lost = 0;
      string s;
      cin >> s;
      FOR(i, N)
      {
	switch(s.at(i))
	{
	case '1':
	  a[__n][i] = 1;
	  ++won;
	  ++wonA[__n];
	  break;
	case '0':
	  a[__n][i] = 2;
	  ++lostA[__n];
	  ++lost;
	  break;
	}
      }
      wp[__n] = ((double)(won)) / (won + lost);
    }

    FOR(__n, N)
    {
      owp[__n] = 0;
      int con = 0;
      FOR(i, N)
      {
	if (i == __n) continue;
	if (!a[__n][i]) continue;

	++con;
	if (a[__n][i] == 1)
	{
	  owp[__n] += (wonA[i] / ((double) (wonA[i] + lostA[i] - 1)));
	}
	else
	{
	  owp[__n] += ((wonA[i] - 1) / ((double) (wonA[i] + lostA[i] - 1)));
	}
      }
      owp[__n] /= con;
      sumOwp += owp[__n];
    }

    cout << "Case #" << (__t + 1) << ":" << endl;
    FOR(i, N)
    {
      //cout << wp[i] << endl;
      //cout << owp[i] << endl;
      double oowp = 0;
      int count = 0;
      FOR(j, N)
      {
	if (i == j) continue;
	if (!a[i][j]) continue;

	oowp += owp[j];
	++count;
      }
      oowp /= count;
      double ans = (0.25 * wp[i]) + (0.5 * owp[i]) + (0.25 * oowp);
      cout << ans << endl;
    }
  }

  return 0;
}
