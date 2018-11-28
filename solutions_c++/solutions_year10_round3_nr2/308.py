/*
 *	E-Mail : khaled.samy@fci-cu.edu.eg
 *	TopCoder Handle : Khaled91
 *	Another buggy code by Khaled Samy ;)
 */
#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <bitset>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <fstream>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <valarray>
using namespace std;
#define PB                      push_back
#define MP                      make_pair
#define ALL(v)                  v.begin(),v.end()
#define SZ(v)					(int)v.size()
#define CLR(v, d)               memset(v, d, sizeof(v))
#define loop(i,n) 		        for(int i=0;i<(int)n;i++)
#define loop2(i,n,m)            for(int i=n;i<(int)(m);i++)

typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vi> vvi;
typedef vector<vd> vvd;
typedef vector<string> vs;
typedef long long ll;
typedef stringstream SS;
typedef pair<int, int> pii;
typedef vector<pii> vpii;

const int OO = (int) 1e9;
const double PI = 2 * acos(0);
const double EPS = 1e-9;

int dcmp(double a, double b) {
	return fabs(a - b) <= EPS ? 0 : a > b ? 1 : 2;
}

int DI[] = { -1, 0, 1, 0, 1, -1, -1, 1 };
int DJ[] = { 0, 1, 0, -1, 1, -1, 1, -1 };

int main() {
	freopen("a.in","rt",stdin);
	freopen("b.out","wt",stdout);
	int l, p, c,tt;
	scanf("%d",&tt);
	for(int t = 0 ; t < tt ; t++)
	{
		cin >> l >> p >> c;
		double res = 1;
		while(ceil((double)p/c)>l)
		{
			res+=1;
			int s = p%c;
			p/=c;
			if(s)p+=1;

		}
		int r;
		if(res==0)r=0;
		else r = ceil(log2(res));

		printf("Case #%d: %d\n",t+1,r);
	}
	return 0;
}
