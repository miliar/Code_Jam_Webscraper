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

int num,x,n,ans1;
void init()
{
    scanf("%d",&num);
	while (num--){
        int sum=0, check=0, Min=INF;
		scanf("%d",&n);
		for (int i=1; i<=n; i++){
			scanf("%d",&x);
			sum+=x;
			check=check^x;
			Min=min(Min,x);
		}
		
		++ans1;
		if (check!=0) printf("Case #%d: NO\n",ans1); else printf("Case #%d: %d\n",ans1,sum-Min);
	}
}
int main()
{
	freopen("cc.in","r",stdin);
	freopen("cc.out","w",stdout);
	init();
	return 0;
}

