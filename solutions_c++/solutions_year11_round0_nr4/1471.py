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

int num,n,ans,ans1,x;
void init()
{
    scanf("%d",&num);
    while (num--){
		ans=0;
		scanf("%d",&n);
		for (int i=1; i<=n; i++){
			scanf("%d",&x);
			if (x!=i) ++ans;
		}
		++ans1;
		printf("Case #%d: %d.000000\n",ans1,ans);
	}
}
int main()
{
	freopen("dd.in","r",stdin);
	freopen("dd.out","w",stdout);
	init();
	return 0;
}

