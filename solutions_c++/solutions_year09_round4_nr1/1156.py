#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <list>
#include <deque>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <functional>
#include <cmath>
#include <memory.h>

using namespace std;

#define FOR(i,a,b) for(int i=a; i<b; ++i)
#define RFOR(i, a, b) for(int i=b-1; i>=a; --i)
#define FILL(a, val) memset(a, val, sizeof(a))

#define pb push_back
#define sz(c) (int)c.size()
#define all(c) c.begin(),c.end()

#define mp make_pair
#define X first
#define Y second

typedef long int Int;
typedef vector<int> VI;
typedef pair<int, int> PII;

const int INF = 1000000000;
const double PI = acos(-1.0);

int a[100][100];
PII b[100];
int p[100];

int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	FOR(t, 0, T){
		int n;
		scanf("%d", &n);
		FOR(i, 0, n)
			FOR(j, 0, n){
				char c;
			cin >> c;
			if ( c =='1')
				a[i][j]  = 1;
			else
				a[i][j] = 0;

		}

		FOR(i, 0, n){
			p[i] = 0;
			FOR(j, 0, n)
				if (a[i][j] == 1)
					p[i] = j;
		}

		/*
		FOR(i, 0, n){
			RFOR(j, 0, n)
				if (a[i][j]==1){
					//b[i] = mp(j, i);
					p[i] = j;
					break;
				}
		}


		FOR(i, 0, n*n)
			RFOR(j, 0, n-1)
				if (b[j].X>j)
					swap(b[j], b[j+1]);
				

		int res = 0;
		FOR(i, 0, n)
			FOR(j, 0, n){
				if (i<j && b[i].Y>b[j].Y)
					res++;
				if (i>j && b[i].Y<b[j].Y)
					res++;
		}
		res /=2;
*/
			
		int res = 0;
		
		FOR(i, 0, n){
			if (p[i]>i){
				int j=i+1;
				while( p[j] > i)
                    j++;
				for(j; j!=i; j--){
                    swap(p[j], p[j-1]);
                    res++;
                }
			}
		}

		printf("Case #%d: %d\n", t+1, res);
	}
	return 0;
}