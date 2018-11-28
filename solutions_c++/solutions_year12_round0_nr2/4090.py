#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <cctype>
#include <algorithm>
#include <vector>
#include <numeric>
#include <set>
#include <queue>
#include <map>
#include <list>
#include <string>
#include <iostream>
#include <stack>
#include <sstream>
using namespace std; 
#define PB push_back
#define MP make_pair
#define F first
#define S second 
#define BE(a) a.begin(),a.end() 
#define CLS(a,b) memset(a,b,sizeof(a))
#define SZ(a) ((int)a.size())
const long double pi=acos(-1.0);
#define torad(a) ((a)*pi/180.0)
typedef vector<int> vi ; 
typedef vector<string> vs ; 
typedef vector<double> vd ; 
typedef pair<int,int> pii ; 
typedef long long ll ; 
typedef long double ld ; 
typedef double dl ; 
class node {public:
};
typedef vector<node> vn ; 
int cases,g;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
////////////////////////////////////////////
	int i,j,k;
	scanf("%d",&cases);
	for(g=0;g<cases;g++)
	{
    int n,s,p,ret=0;
		printf("Case #%d: ",g+1);
    scanf("%d%d%d",&n,&s,&p);
    for(i=0;i<n;i++) {
      int x,l,m;
      scanf("%d",&x);
      l = x/3;
      m = x%3;
      if(m != 0) ++l;
      if(l>=p){
        ++ret;
      } else if(m != 1 && l+1>=p && s && l) {
        --s;
        ++ret;
      }
    }
    printf("%d\n",ret);
	}

	return 0;
}