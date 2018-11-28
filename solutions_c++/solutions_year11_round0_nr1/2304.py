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

int main()
{
	int T, N;
	vector<int> Or, Bl;
	pair<int,char> Board[105];
	scanf("%d", &T);
	
	FORUP(test,1,T+1)
	{
		FILL(Board,0);
		Or.clear();
		Bl.clear();
	
		scanf("%d ", &N);
		FORUP(i,0,N)
		{
			char a; int b;
			scanf("%c %d ", &a, &b);
			if (a=='O') Or.push_back(b);
			else if (a=='B') Bl.push_back(b);
			Board[i] = MP(a,b);
		}
		
		int ans = 0, Onow = 1, Bnow = 1;
		FORUP(i,0,N)
		{
			int next = Board[i].SC;
			if (Board[i].FS=='O')
			{
				Or.erase(Or.begin());
				int move = max(Onow,next)-min(Onow,next)+1;
				ans += move;
				Onow = next;
				
				if (!Bl.empty())
				{
					int sel = max(Bl[0],Bnow)-min(Bl[0],Bnow);
					if (Bl[0]<Bnow) Bnow = Bnow - min(sel,move);
					else Bnow = Bnow + min(sel,move);
				}
			}
			else if (Board[i].FS=='B')
			{
				Bl.erase(Bl.begin());
				int move = max(Bnow,next)-min(Bnow,next)+1;
				ans += move;
				Bnow = next;
				
				if (!Or.empty())
				{
					int sel = max(Or[0],Onow)-min(Or[0],Onow);
					if (Or[0]<Onow) Onow = Onow - min(sel,move);
					else Onow = Onow + min(sel,move);
				}
			}
		}
		
		printf("Case #%d: %d\n", test, ans);
		
	}
	
	return 0;
}
