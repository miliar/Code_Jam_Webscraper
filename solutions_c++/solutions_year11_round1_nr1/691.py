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

int num,ans1;
long long n,m,g;

long long gcd(long long a,long long b)
{
    if (b==0) return a;
	return gcd(b,a%b);
}
int main()
{
	freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);

	scanf("%d\n",&num);
    while (num--){
        scanf("%I64d%I64d%I64d",&n,&m,&g);
		++ans1;
		printf("Case #%d: ",ans1);
		if (g==0){
			if (m==0) printf("Possible"); else printf("Broken");
		} else if (g==100){
			if (m!=100) printf("Broken"); else printf("Possible");
		} else {
			long long k=100/gcd(m,100);
			if (k<=n) printf("Possible"); else printf("Broken");
		}
		printf("\n");
	}
	return 0;
}

