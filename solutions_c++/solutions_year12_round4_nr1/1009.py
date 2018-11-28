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
int n;
int pos[10009];
int len[10009];
int best[10009];
int d;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
////////////////////////////////////////////
	int i,j,k;
	scanf("%d",&cases);
	for(g=0;g<cases;g++)
	{
    CLS(best,-1);
		printf("Case #%d: ",g+1);
    scanf("%d",&n);
    for(i=0;i<n;i++) {
      scanf("%d%d",&pos[i],&len[i]);
    }
    int d;
    scanf("%d",&d);
    len[n]=0;
    pos[n]=d;
    best[0]=pos[0];
    for(i=1;i<=n;i++) {
      for(j=0;j<i;j++) {
        int po=j;
        int pn=i;
        if(best[po] > -1 && pos[pn]-pos[po] <= best[po]) {
          best[pn]=max(best[pn],min(len[pn],pos[pn]-pos[po]));
        }
      }
    }
    if(best[n] > -1) {
      printf("YES\n");
    } else {
      printf("NO\n");
    }
	
	}

	return 0;
}