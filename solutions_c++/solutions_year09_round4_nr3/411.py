#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <iostream>
#include <sstream>
#include <cstddef>
#include <algorithm>
#include <utility>
#include <iterator>
#include <numeric>
#include <list>
#include <complex>
#include <cstdio>
#include <ctime>
using namespace std;

#define all(x) (x).begin(), (x).end()
#define sz(x) ((int)(x).size())
#define init(st) memset(st, 0, sizeof(st))
#define ll long long

//String operations
template<class T>
void splitstr(const string &s, vector<T> &out)
{
    istringstream in(s);
    out.clear();
    copy(istream_iterator<T>(in), istream_iterator<T>(), back_inserter(out));
}
template<class T>
void initArray(T *arr, int size, T value)
{
	for(int i = 0; i < size; i++)
		arr[i] = value;
}
template<class T>
T readValue(string s)
{
	T result;
	istringstream sin(s);
	sin >> result;
	return result;
}

//Arithmetic operations
template<class T>
inline T gcd(T a, T b)
{
	return (!a)?b:gcd(b % a, a);
}

template<class T>
inline T mod(T a, T p)
{
	a %= p;
	return (a<0)?a+p:a;
}

template<class T>
inline T numbits(T n)
{
	return (!n)?0:1+numbits(n&(n-1));
}

template<class T>
inline T inverse(T a, T m)
{
	a = mod<T>(a,m);
	return (a==1)?1:mod<T>((1-m*inverse<T>(m%a,a)) / a,m);
}

template<class T>
inline bool isPrime(T a)
{
	int lim = sqrt((double)a) + 1;
	for(T i = 2; i < lim; i++)
		if(a % i == 0)
			return false;
	return true;
}

template<class T>
inline T power(T a, T p, T mod)
{
	if(!p) return 1;
	T temp = power(a, p>>1, mod);
	temp = (temp * temp) % mod;
	if(p&1)
		temp = (temp * a) % mod;
	return temp;
}

void get_primes(int start, int end, vector<int> &vi)
{
	int *p = new int[end + 1];
	initArray<int>(p, end+1, 0); p[1] = 1;

	for(int i = 2; i <= end; i++)
	{
		if(!p[i])
		{
			if(i >= start)
				vi.push_back(i);

			for(int j = 2*i; j <= end; j += i)
				p[j] = 1;
		}
	}
	delete [] p;
}

//Graph operations
bool dfs(int current, int final, int total, int* visited, int **edges, bool flow)
{
	if(current == final)
		return true;
	if(visited[current])
		return false;
	visited[current] = true;
	for(int i = 0; i < total; i++)
		if(edges[current][i] && dfs(i, final, total, visited, edges, flow))
		{
			if(flow)
			{
				edges[current][i]--;
				edges[i][current]++;
			}
			return true;
		}
	return false;
}

int flow(int in, int out, int total, int **edges)
{
	int result = 0;
	int *visited = new int[total];
	while(initArray<int>(visited, total, 0), dfs(in, out, total, visited, edges, true))
		result++;
	return result;
}

//Disjoint datasets
void create_set(int x, int *P, int *rank)
{
	P[x] = x;
	rank[x] = 0;
}

int find_set(int x, int *P)
{
	if(x != P[x])
		P[x] = find_set(P[x], P);
	return P[x];
}

bool merge_sets(int x, int y, int *P, int *rank)
{
	int Px = find_set(x, P);
	int Py = find_set(y, P);
	if(Px == Py)
		return false;
	if(rank[Px] > rank[Py]) P[Py] = Px;
	else P[Px] = Py;
	if(rank[Px] == rank[Py])
		rank[Py]++;
	return true;
}

//Binary tree operations
int read_cum_freq(int index, int *tree)
{
	int sum = 0;
	while(index)
	{
		sum += tree[index];
		index -= (index & -index);
	}
	return sum;
}

void upd_freq(int index, int mxIndex, int value, int *tree)
{
	while(index <= mxIndex)
	{
		tree[index] += value;
		index += (index & -index);
	}
}

int read_freq(int index, int *tree)
{
	return read_cum_freq(index, tree) - read_cum_freq(index-1, tree);
}

//Setup
FILE *stream1, *stream2;
void setup(int value)
{
	freopen("in.txt", "r", stdin);
	if(value)
		freopen("out.txt", "w", stdout);
}

vector< vector<ll> > vvi;
int arr[16];

bool intersection(int i, int j)
{
	int n = vvi[0].size();
	for(int k = 1; k < n; k++)
		if( (vvi[i][k] - vvi[j][k]) * (vvi[i][k-1] - vvi[j][k-1]) <= 0)
			return true;
	return false;
}
int result;

void go(int cur, int num)
{
	int n = vvi.size();

	if(num >= result)
		return;

	if(cur == n)
	{
		result = min(num, result);
		return;
	}

	for(int i = 0; i <= num; i++)
	{
		bool can = true;
		for(int j = 0; j < cur; j++)
		{
			if((arr[j] == i) && intersection(j,cur))
				can = false;
		}

		if(can)
		{
			arr[cur] = i;
			go(cur+1, num);
		}
	}
	arr[cur] = num + 1;
	go(cur+1, num + 1);
}

 
int main()
{
	setup(1);
	int cases;
	cin >> cases;
	
	for(int q = 0; q < cases; q++)
	{
		int n,k;
		cin >> n >> k;
		vvi.clear();
		init(arr);
		for(int i = 0; i < n; i++)
		{
			int temp;
			vector<ll> vi;
			for(int i = 0; i < k; i++)
			{
				cin >> temp;
				vi.push_back(temp);
			}
			vvi.push_back(vi);
		}

		result = 1000000;
		go(1,0);

		cout << "Case #" << q + 1 << ": " << result + 1 << "\n";
	}

	return 0;
}