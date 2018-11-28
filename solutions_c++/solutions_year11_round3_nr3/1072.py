#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <queue>
#include <list>
#include <stack>
#include <map>
#include <iomanip>
#include <sstream>
#include <set>
#include <deque>
#include <climits>
 
using namespace std;
 
#define EPS 1e-11
#define PI acos(-1.0)
 
#define DEBUG(n) cout << "->" << #n << " -> " << n << '\n'
#define FILL(arr,n) memset(arr,n,sizeof(arr))
#define FORUP(i,m,n) for(int i=(m),_n=(n); i<_n; i++)
#define FORDOWN(i,m,n) for(int i=(m)-1,_n=(n); i >= _n; i--)
#define FOREACH(iter,n) for(__typeof ((n).begin()) iter=(n).begin(); iter!=(n).end(); iter++)
#define ALL(n) (n).begin(),(n).end()
#define ALLSIZE(n,jum) (n),(n)+(jum)
#define FS first
#define SC second
#define SQR(x) ((x)*(x))
#define MP make_pair

//====== ilcapt ====

int N, L, H;
int freq[105];

int look()
{
	FORUP(i,L,H+1)
	{
		bool bisa=true;
		FORUP(j,0,N)
		{
			if (i==freq[j]) continue;
			else if (i>freq[j] && i%freq[j]!=0) bisa=false;
			else if (i<freq[j] && freq[j]%i!=0) bisa=false;
			
			if (!bisa) break;
		}
		if (bisa) return i;
	}
	return -1;
}

int main()
{
	int T;
	scanf("%d", &T);
	
	FORUP(test,1,T+1)
	{
		scanf("%d%d%d", &N, &L, &H);
		FORUP(i,0,N)
			scanf("%d", &freq[i]);
		
		sort(ALLSIZE(freq,N));
		
		int ans = look();
		if (ans==-1) printf("Case #%d: NO\n", test);
		else printf("Case #%d: %d\n", test, ans);
	}
	
	return 0;
}
