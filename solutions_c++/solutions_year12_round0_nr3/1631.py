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

int a, b;

int main()
{
	freopen("C:\\Users\\Віталік\\Desktop\\GCJ 2012\\Qual\\C-small-attempt0.in", "r", stdin);
	freopen("C:\\Users\\Віталік\\Desktop\\GCJ 2012\\Qual\\C-small-attempt0.out", "w", stdout);

	int T;
	cin >> T;
	FOR (tt,0,T)
	{
		cin >> a >> b;

		int len = 0;
		int t = a;
		while (t > 0)
		{
			len++;
			t /= 10;
		}

		int p = 1;
		FOR (j,0,len-1)
			p *= 10;

		int res = 0;
		
		FOR (i,a,b)
		{
			int t = i;
			set <int> S;
			FOR (j,0,len-1)
			{
				int d = t % 10;
				t /= 10;
				t = p*d + t;
				if (t > i && t <= b)
				{
					if (S.find(t) != S.end())
						continue;
					S.insert(t);
					res++;
				}
			}
		}

		cout << "Case #" << tt+1 << ": " << res << endl;
	}
	return 0;
} 