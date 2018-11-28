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

//#include "bigint.h"

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
inline T gcd(T a, T b, T zero)
{
	return (a == zero)?b:gcd(b % a, a, zero);
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

vector< vector<int> > vvi;
vector< vector<int> > vvi2;

struct rect {
    int x1;
    int x2;
    int y1;
    int y2;
};

bool intersect(int x1, int x2, int x3, int x4) {
    return (x3 <= x2) && (x1 <= x4);
}

int main()
{
    setup(1);
    
    int P[1001];
    int rank[1001];
    int C;
    cin >> C;
    for (int q = 0; q < C; q++) {
        int R;
        cin >> R;
        vector<rect> vr;
        for (int j = 0; j < R; j++) {
            rect r;
            cin >> r.x1 >> r.y1 >> r.x2 >> r.y2;
            vr.push_back(r);
        }

        for (int i = 0; i < R; i++)
            create_set(i, P, rank);

        for (int i = 0; i < R; i++)
            for (int j = i + 1; j < R; j++) {
                bool flag = intersect(vr[i].x1, vr[i].x2, vr[j].x1, vr[j].x2) && 
                            intersect(vr[i].y1, vr[i].y2, vr[j].y1, vr[j].y2);

                if (q == 3)
                {
                    int value = 1;
                }
                if (!flag) {
                    bool val1 = intersect(vr[i].x1 - 1, vr[i].x2 + 1, vr[j].x1, vr[j].x2);
                    bool val2 = intersect(vr[i].y1 - 1, vr[i].y2 + 1, vr[j].y1, vr[j].y2);
                    bool val3 = ((vr[i].x1 - vr[j].x2) == 1 && (vr[i].y1 - vr[j].y2) == 1);
                    bool val4 = ((vr[j].x1 - vr[i].x2) == 1 && (vr[j].y1 - vr[i].y2) == 1);
                    flag = val1 && val2 && (!(val3 || val4));
                }

                if (flag)
                    merge_sets(i,j,P,rank);

            }
       
        int result = -1000000000;
        for (int i = 0; i < R; i++) {
            rect r;
            int x = -1000000;
            int y = -1000000;
            for (int j = 0; j < R; j++)
                if (find_set(j, P) == find_set(i,P)) {
                    x = max(x, vr[j].x2);
                    y = max(y, vr[j].y2);
                }

            for (int j = 0; j < R; j++)
                if (find_set(j, P) == find_set(i,P)) {
                    result = max(result, (x - vr[j].x1) + (y - vr[j].y1) + 1);
                }
        }

        std::cout << "Case #" << q+1 << ": " << result << std::endl;
    }

	return 0;
}