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
	int lim = sqrt(a) + 1;
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

int compare(vector<int> v1, vector<int> v2)
{
	for(int i = 0; i < v1.size(); i++)
		if(v1[i] != v2[i])
			return (v1[i] < v2[i]) ? -1 : 1;
	return 0;
}

int main()
{
	setup(1);
	
	int cases;
	cin >> cases;
	for(int q = 0; q < cases; q++)
	{
		string str;
		cin >> str;
		vector<int> vi1, vi2;
		vi1.push_back(0);
		vi2.push_back(0);
		for(int i = 0; i < str.size(); i++)
		{
			int temp = str[i] - '0';
			vi1.push_back(temp);
			vi2.push_back(temp);
		}

		for(int i = vi1.size()-1; i >= 0; i--)
		{
			sort(vi2.begin() + i, vi2.end());
			int j;
			for(j = i; j < vi2.size(); j++)
				if(vi2[j] > vi1[i])
					break;
			if(j == vi2.size())
				continue;

			int temp = vi2[j];
			for(int k = j; k > i; k--)
				vi2[k] = vi2[k-1];
			vi2[i] = temp;
			int start = 1;
			if(!i)
				start = 0;
			cout << "Case #" << q+1 << ": ";
			for(int j = start; j < vi2.size(); j++)
				cout << vi2[j];
			cout << "\n";
			break;
		}
	}

	return 0;
}