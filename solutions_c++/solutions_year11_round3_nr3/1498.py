#include <algorithm>
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <string.h>
#include <cstdio>
#include <vector>
#include <bitset>
#include <cmath>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <ctime>

using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef pair<double,double> PDD;
typedef unsigned long long ULL;

#define FOR(i,a,b) for (int i(a); i < (b); i++) 
#define REP(i,n) FOR(i,0,n) 
#define SORT(v) sort((v).begin(),(v).end())
#define UN(v) sort((v).begin(),(v).end()),v.erase(unique(v.begin(),v.end()),v.end())
#define CL(a,b) memset(a,b,sizeof(a))

int T, N, L, H;
int note[10000];

int solve()
{
	FOR(i, L, H+1)
	{
		bool is_ok = true;
		REP(j, N)
		{
			int m = note[j];
			if(!((i<m && m%i==0) ||
			   (m<=i && i%m==0)))
			{
				is_ok = false;
			}
		}
		if(is_ok) return i;
	}

	return -1;
}

int main()
{
	int i, j, k;
	ifstream in("input.txt", ios::in);
	FILE* out = fopen("output.txt", "w");

	in >> T;
	REP(k, T)
	{
		in >> N >> L >> H;
		REP(i, N)
		{
			in >> note[i];
		}

		int n = solve();
		if(n != -1)
		{
			fprintf(out, "Case #%d: %d\n", k+1, n);
		}
		else
		{
			fprintf(out, "Case #%d: NO\n", k+1, n);
		}
	}
}