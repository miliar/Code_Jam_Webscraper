#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cstring>
#include <cassert>
#include <climits>
#include <iostream>
#include <iomanip>
#include <utility>
#include <vector>
#include <deque>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <string>
#include <sstream>

using namespace std;

int s, p;
int a[301][301];
int ma[301], mb[301];

int k[301];

int augment (int h)
{
	k[h] = 1;
	for (int i = 0; i < p; i++)
	{
		if (a[h][i] == 1 && mb[i] == -1)
		{
			ma[h] = i;
			mb[i] = h;
			return 1;
		}
	}
	
	for (int i = 0; i < p; i++)
	{
		if (a[h][i] == 1 && k[mb[i]] == 0)
		{
			if (augment (mb[i]))
			{
				ma[h] = i;
				mb[i] = h;
				return 1;
			}
		}
	}
	
	//k[h] = 0;
	return 0;
}

void match()
{
	memset (ma, 0xff, 301 * sizeof (int));
	memset (mb, 0xff, 601 * sizeof (int));
	
	for (int i = 0; i < s; i++)
	{
		if (ma[i] == -1)
		{
			memset (k, 0, 301 * sizeof (int));
			augment (i);
		}
	}
}

typedef pair <int, int> schd;
#define start first
#define finish second

int main()
{
	int C;
	cin >> C;
	for (int cn = 1; cn <= C; cn++)
	{
		int T;
		cin >> T;
		int A,B;
		cin >> A >> B;
		vector <schd> LA, LB;
#define INP(P) \
		for (int i = 0; i < P; i++) \
		{ \
			string st, en; \
			cin >> st >> en; \
			int t,q,r,s; \
			sscanf (st.c_str(), "%ld:%ld", &t, &q); \
			sscanf (en.c_str(), "%ld:%ld", &r, &s); \
			L##P.push_back (schd ( 60*t + q, 60*r + s)); \
		}
		INP(A);
		INP(B);
		int n = A+B;
		vector <schd> L;
		for (int i = 0; i < A; i++) L.push_back (LA[i]);
		for (int i = 0; i < B; i++) L.push_back (LB[i]);
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++) if ((i < A && j >= A) || (i >= A && j < A))
				a[i][j] = (L[j].start >= L[i].finish + T);
			else a[i][j] = 0;
		/*
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
				cout << graph[i][j] << " ";
			cout << endl;
		}
		*/
		s = p = n;
		match();
		int ca = 0, cb = 0;
		for (int i = 0; i < A; i++)
			if (mb[i] == -1) ca++;
		for (int i = A; i < n; i++)
			if (mb[i] == -1) cb++;
		cout << "Case #" << cn << ": " << ca << " " << cb << endl;
	}
	return 0;
}
