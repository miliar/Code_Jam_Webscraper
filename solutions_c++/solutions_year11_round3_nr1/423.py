#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <cstring>
using namespace std;

#define MP make_pair
#define PB push_back
#define two(X) (1<<(X))
#define SIZE(A) ((int)(A.size()))
#define LENGTH(A) ((int)A.length())
#define random(x) (rand()%x)
#define randomize() (srand((int)time(0)))

typedef long long int64;
typedef vector<int> VI;
typedef vector<string> VS;

const int INF=0x7FFFFFFF;
const double eps=1e-10;
const double pi=acos(-1.0);

const int maxn=1000;
int num,n,m,ans1;
char ch[maxn][maxn];

void solve()
{
	++ans1;
	printf("Case #%d:\n",ans1);

	for (int i=1; i<=n; i++)
		for (int j=1; j<=m; j++) 
			if (ch[i][j]=='#')
				if ((ch[i][j+1]=='#') && (ch[i+1][j]) && (ch[i+1][j+1])){
					ch[i][j]='/'; ch[i][j+1]='\\'; ch[i+1][j]='\\'; ch[i+1][j+1]='/';	
				} else {
					printf("Impossible\n");
					return;
				}
				 
	for (int i=1; i<=n; i++){
		for (int j=1; j<=m; j++) printf("%c",ch[i][j]);
		printf("\n");
	}
  
}
void init()
{
	scanf("%d",&num);
	while (num--){
		scanf("%d%d\n",&n,&m);
		for (int i=0; i<=n+1; i++) 
			for (int j=0; j<=m+1; j++) ch[i][j]='.';

		for (int i=1; i<=n; i++){
			for (int j=1; j<=m; j++) scanf("%c",&ch[i][j]);
			scanf("\n");
        }
		solve();
	}
}
int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	init();
	return 0;
}

