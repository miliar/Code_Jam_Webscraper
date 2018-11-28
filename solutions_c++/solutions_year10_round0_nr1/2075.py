/*
Author : OmarEl-Mohandes
PROG   : A
LANG   : C++
*/
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <memory.h>
using namespace std;
#define pb push_back
#define all(v) v.begin(),v.end()
#define sz size()
#define rep(i,m) for(int i=0;i<m;i++)
#define REP(i,k,m) for(int i=k;i<m;i++)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
typedef long long ll;
#define oo ((int)1e9)

int main()
{
	freopen("A.in" , "rt" , stdin);
	freopen("A.out" , "wt" , stdout);
	int c , n , k;
	scanf("%d" , &c);
	for (int i = 0; i < c; ++i) {
		scanf("%d%d" , &n , &k);
		int flag ;
		if(n > k)flag = 1;
		else flag = ((k-((1 << n)-1)) % (1 << n));
		if(!flag)
			printf("Case #%d: ON\n" , i+1);
		else
			printf("Case #%d: OFF\n" , i+1);
	}
	return 0;
}
