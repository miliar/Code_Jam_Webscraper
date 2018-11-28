#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string.h>
#include <string>
#include <vector>
#include <map>
#include <cmath>
#include <set>
#include <algorithm>
#include <queue>
#include <cassert>
#include <fstream>
#include <sstream>
#include <bitset>
#include <stack>
#include <list>
#include <hash_map>
using namespace std;
#define debug1(x) cout << #x" = " << x << endl;
#define debug2(x, y) cout << #x" = " << x << " " << #y" = " << y << endl;
#define debug3(x, y, z) cout << #x" = " << x << " " << #y" = " << y << " " << #z" = " << z << endl;
#define debug4(x, y, z, w) cout << #x" = " << x << " " << #y" = " << y << " " << #z" = " << z << " " << #w" = " << w << endl;
template <class T>
ostream & operator << (ostream & out, const vector<T> & t)
{	out << t.size() << " {";	for (int i = 0; i < t.size(); ++i) 		out << t[i] << " ";	out << "}";	return out;}

template <class T>
ostream & operator << (ostream & out, const set<T> & t)
{	out << "{";	for (set<T>::iterator itr = t.begin(); itr != t.end(); ++itr)		out << *itr << " ";	out << "}";	return out;}


////////////////////////////////////////////////////
// BASIC OPERATIONS
////////////////////////////////////////////////////
// a ^ b mod c , c >= 1, b >= 0, a >= 0
inline long long getmod(long long a, unsigned int b, long long c)
{
	if (a == 0) return 0;
	if (c == 1) return 0;
	if (b == 0) return 1;
	if (b == 1) return a % c;

	long long ret = 1;
	for (int i = 31; i >= 0; --i)
		if ((b & (1U << i)) > 0)
		{
			ret = (ret * ret) % c;
			ret = (ret * a) % c;
		}
		else
			ret = (ret * ret) % c;
	return ret;
}

/** 
 * @warning gcd(2, -3) = -1
 */
int gcd(int x, int y)
{
  if (!x || !y) return x > y ? x : y;
  for (int t; t = x % y; x = y, y = t);
  return y;
}

/** 
 * ax + by = gcd(a, b)
 * x, y may be negative 
 */
int extgcd(int a, int b, int & x, int & y)
{
  if (b == 0) { x = 1; y = 0; return a; }
  int d = extgcd(b, a % b, x, y);
  int t = x; x = y; y = t - a / b * y;
  return d;
}

/** 
 * a * x mod p = 1 , (a,p) = 1
 */
int getReverse(int a, int p)
{
	if (a == 1) return 1;
	int x, y;
	extgcd(a, p, x, y);
	return (x % p + p) % p;
}

//////////////////////////////////////////////////////////////////////
// Algorithm about primes 
//////////////////////////////////////////////////////////////////////
class Prime 
{
    public:
        /** The Primes */
        vector<int> primes;

		Prime()
		{
			genPrime(10000000);
		}

        /** Generate the primes from [2,N] */
        int genPrime(int N) {
            bool * mk = new bool[N + 2];
            memset(mk , 0 , N + 1);
            for (int i = 2 , k = 4 ; i <= N ; i++ , k += i + i - 1) {
                if (!mk[i]) 
                {
                    primes.push_back(i);
                    if (k <= N) for (int j = i + i ; j <= N ; j += i) mk[j] = 1;
                }
            }
            delete [] mk;
            return primes.size();
        }
        
        /** Return the factors of the given long long number 
         *  Remember to call GenPrime first 
         */
        map<long long ,int> getFactors(long long N) 
		{ 
            map<long long ,int> factors;
            long long root = ((long long) sqrt((double)N)) + 1;
            for(unsigned int i = 0 ; N > 1 && i < primes.size() && primes[i] <= root ; ++i) {
                if (N % primes[i] == 0) {
                    factors[ primes[i] ] = 0;
                    while (N % primes[i] == 0)
                       N /= primes[i] , factors[ primes[i] ]++ ; 
                }
            }
            if (N > 1) factors[N] = 1; 
            return factors; 
        }

		map<int, int> getFactorsInt(int N)
		{
            map<int ,int> factors;
            int root = ((int) sqrt((double)N)) + 1;
            for(unsigned int i = 0 ; N > 1 && i < primes.size() && primes[i] <= root ; ++i) {
                if (N % primes[i] == 0) {
                    factors[ primes[i] ] = 0;
                    while (N % primes[i] == 0)
                       N /= primes[i] , factors[ primes[i] ]++ ; 
                }
            }
            if (N > 1) factors[N] = 1; 
            return factors; 
		}

		map<int, int> getJieFactors(int x)
		{
			map<int, int> ret;
			for (int i = 0; x >= Prime::prime.primes[i]; ++i)
			{
				int p = Prime::prime.primes[i];int t = x;
				while (t >= p)	{	ret[p] += t / p; 	t /= p;	}
			}
			return ret;
		}

		/** Return the divisiors of the given number */
		vector<long long> getDivisors(long long N)
		{
			map<long long, int> factors = getFactors(N);
			vector<long long> p;
			vector<int> maxi;
			for (map<long long, int>::iterator itr = factors.begin(); itr != factors.end(); ++itr)
				p.push_back(itr->first), maxi.push_back(itr->second);

			vector<long long> ret;
			vector<int> nowi(p.size(), 0);
			int nowp = p.size() - 1;

			while (true)
			{
				long long now = 1;
				for (int i = 0; i < p.size(); ++i)
					for (int j = 1; j <= nowi[i]; ++j)
						now = now * p[i];
				ret.push_back(now);

				nowp = p.size() - 1;
				nowi[nowp]++;
				while (nowi[nowp] > maxi[nowp])
				{
					nowp--;
					if (nowp < 0) return ret;
					nowi[nowp]++;
				}

				for (int i = nowp + 1; i < p.size(); ++i)
					nowi[i] = 0;
			}
			return ret;
		}

		static Prime prime;
};

Prime Prime::prime;


// 求欧拉函数 < x 互质的个数
int getPhi(int x)
{
	map<long long, int> factors = Prime::prime.getFactors(x);
	for (map<long long, int>::iterator itr = factors.begin(); itr != factors.end(); ++itr)
		x = x / (itr->first) * (itr->first - 1);
	return x;
}

/////////////////////////
// template finished
/////////////////////////
int T, testid;

int P, W;
bool graph[100][100];
bool nowthe[100];
int minDepth;
int maxThres;
bool visit[100];
void search(int now, int depth)
{
	int thres = 0;
	for (int i = 0; i < P; ++i)
		if (nowthe[i]) thres++;

	if (depth > minDepth) return;
	if (nowthe[1])
	{
		if (depth < minDepth || depth == minDepth && thres > maxThres) 
		{
			minDepth = depth;
			maxThres = thres;
		}
		return;
	}

	for (int i = 0; i < P; ++i)
		if (graph[now][i] && !visit[i])
		{
			visit[i] = true;
			bool temp[40];
			for (int k = 0; k < P; ++k) temp[k] = nowthe[k];
			for (int j = 0; j < P; ++j)
				if (graph[i][j]) 
					nowthe[j] = true;
			search(i, depth + 1);

			visit[i] = false;
			for (int k = 0; k < P; ++k) nowthe[k] = temp[k];
		}
}

void init()
{
	cin >> P >> W;
	memset(graph, false, sizeof(graph));
	memset(visit, false, sizeof(visit));
	memset(nowthe, false, sizeof(nowthe));
	for (int i = 0; i < W; ++i)
	{
		int a, b;
		scanf("%d,%d", &a, &b);
		//debug2(a, b);
		graph[a][b] = graph[b][a] = true;
	}

	for (int i = 0; i < P; ++i)
		if (graph[0][i]) 
			nowthe[i] = true;

	//debug1(nowthe[1]);

	visit[0] = true;
	minDepth = 9999;
	maxThres = 0;
	search(0, 0);

	printf("Case #%d: %d %d\n", testid, minDepth, minDepth == 0 ? maxThres : maxThres - minDepth - 1);
}

void york()
{
}

int main()
{
	cin >> T;
	for (testid = 1; testid <= T; ++testid)
	{
		init();
		york();
	}
	return 0;
}