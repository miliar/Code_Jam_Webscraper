#include <iostream>   
#include <sstream>   
#include <cstdio>   
#include <cstdlib>   
#include <cmath>   
#include <memory>   
#include <cctype>   
#include <string>   
#include <vector>   
#include <list>   
#include <queue>   
#include <deque>   
#include <stack>   
#include <map>   
#include <set>   
#include <algorithm>   
using namespace std;  
   
#define FOR(i,a,b) for(int (i) = (a); (i) < (b); ++(i))  
#define RFOR(i,a,b) for(int (i) = (a)-1; (i) >= (b); --(i))  
#define CLEAR(a) memset((a),0,sizeof(a))  
#define INF 1000000000  
#define PB push_back  
#define ALL(c) (c).begin(), (c).end()  
#define pi 2*acos(0.0)  
#define SQR(a) (a)*(a)  
#define MP make_pair  
#define MAX 75000
#define MOD 1000000007
   
typedef long long Int;  

int n, s, p;
vector <int> A[47];
vector <int> B[47];
int S[MAX];
int R[101][101];

int main()
{
	//freopen("C:\\Users\\Віталік\\Desktop\\GCJ 2012\\Qual\\C-large.in", "r", stdin);
	//freopen("C:\\Users\\Віталік\\Desktop\\GCJ 2012\\Qual\\C-large.out", "w", stdout);

	FOR (i,0,11)
		FOR (j,0,11)
			FOR (k,0,11)
			{
				if (abs(i-j) > 2)
					continue;
				if (abs(i-k) > 2)
					continue;
				if (abs(j-k) > 2)
					continue;

				bool ok = false;
				if (abs(i-j) == 2)
					ok = true;
				if (abs(i-k) == 2)
					ok = true;
				if (abs(j-k) == 2)
					ok = true;

				if (!ok)
					A[i+j+k].PB(max(i, max(j, k)));
				else
					B[i+j+k].PB(max(i, max(j, k)));
			}


	int T;
	cin >> T;
	FOR (tt,0,T)
	{
		cin >> n >> s >> p;
		FOR (i,0,n)
			cin >> S[i];
		FOR (i,0,101)
			FOR (j,0,101)
				R[i][j] = -INF;
		R[0][0] = 0;
		FOR (i,0,n)
			FOR (j,0,i+1)
			{
				if (R[i][j] < 0)
					continue;
				FOR (k,0,A[S[i]].size())
				{
					int t = 0;
					if (A[S[i]][k] >= p)
						t = 1;
					R[i+1][j] = max(R[i+1][j], R[i][j] + t);
				}

				FOR (k,0,B[S[i]].size())
				{
					int t = 0;
					if (B[S[i]][k] >= p)
						t = 1;
					R[i+1][j+1] = max(R[i+1][j+1], R[i][j] + t);
				}
			}
		cout << R[n][s] << endl;
	}
	return 0;
} 