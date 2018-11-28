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
#include <ctime>

using namespace std;
 
#define EPS 1e-11
#define PI acos(-1.0)

typedef pair<int,int> pii;
typedef pair<int, pii> piii;
 
#define DEBUG(n) cout << "->" << #n << " -> " << n << '\n'
#define FILL(arr,n) memset(arr,n,sizeof(arr))
#define FORUP(i,m,n) for(int i=(m),_n=(n); i<_n; i++)
#define FORDOWN(i,m,n) for(int i=(m)-1,_n=(n); i >= _n; i--)
#define FOREACH(iter,n) for(__typeof ((n).begin()) iter=(n).begin(); iter!=(n).end(); iter++)
#define ALL(n) (n).begin(),(n).end()
#define ALLSIZE(n,jum) (n),(n)+(jum)
#define FS first
#define SC second
#define MP make_pair
#define SQR(x) ((x)*(x))

//====== ilcapt ====

char mp[30] = {"yhesocvxduiglbkrztnwjpfmaq"};

int main()
{
	int T;
	char G[128];
	scanf("%d", &T);
	gets(G);
	
	FORUP(test,1,T+1)
	{
		gets(G);
		printf("Case #%d: ", test);
		FORUP(i,0,strlen(G))
		{
			if (isalpha(G[i]))
				printf("%c", mp[G[i]-'a']);
			else printf("%c", G[i]);
		}
		printf("\n");
	}
	
	return 0;
}
