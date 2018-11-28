#include <iostream>
#include <map>
#include <vector>
#include <list>
#include <queue>
#include <set>
#include <string>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <cassert>

using namespace std;

typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;

#define _CRT_SECURE_NO_WARNINGS
#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define Rep(i,n) for (int i(0),_n(n); i < _n; ++i)
#define Repd(i,n) for (int i((n)-1); i >= 0; --i)
#define Fill(a,c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))
#define All(v) (v).begin(), (v).end()

template<typename T, typename S> T cast(S s) {
	stringstream ss;
	ss << s;
	T res;
	ss >> res;
	return res;
}

template<typename T> inline T sqr(T a) { return a*a; }
template<typename T> inline int Size(const T& c) { return (int)c.size(); }
template<typename T> inline void checkMin(T& a, T b) { if (b < a) a = b; }
template<typename T> inline void checkMax(T& a, T b) { if (b > a) a = b; }

struct GP 
{
	int x, y;
	GP(int _x, int _y) : x(_x), y(_y){}
};
vector<GP> gps;

void printgps()
{
	for(int i = 0 ;i < gps.size(); i++)
	{
		cout << gps[i].x << " " << gps[i].y << endl;
	}
}

bool validTri(GP l, GP m, GP n)
{
	double centrex, centrey;
	centrex = (double)(l.x + m.x + n.x)/3;
	centrey = (double)(l.y + m.y + n.y)/3;
	//cout << centrex << " " << centrey

	//return !(((int)centrex < centrex) || ((int)centrey) < centrey); 
	return (floor(centrex) == ceil(centrex)) && (floor(centrey) == ceil(centrey));
}

int main()
{
	int N;
	cin >> N;
	long long int n, A, B, C, D, x0, y0, M;
	int l, m, p;
	Rep(i, N)
	{
		cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
		gps.clear();
		gps.push_back(GP(x0, y0));
		for(int j = 1; j <= n-1; j++)
		{
			x0 = ((A%M)*(x0%M) + B%M)%M;
			y0 = ((C%M)*(y0%M) + (D%M))%M;
			
			gps.push_back(GP(x0, y0));
		}
		//printgps();
		int count = 0;
		for(int l = 0; l < n-2; l++)
		{
			for(int m = l+1; m < n -1; m++)
			{
				for(p = m +1; p < n; p++)
				{
					if(validTri(gps[l], gps[m], gps[p])) count++;
				}
			}
		}
		cout << "Case #" << i + 1 << ": " << count << endl;
	}
	return 0;
}

