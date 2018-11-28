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
int cases,g,n;
int s[1000];
int e[1000];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
////////////////////////////////////////////
	int i,j,k,ans;
	scanf("%d",&cases);
	for(g=0;g<cases;g++)
	{
		ans=0;
		printf("Case #%d: ",g+1);
		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%d%d",&s[i],&e[i]);
		
		for(i=0;i<n;i++)
			for(j=i+1;j<n;j++)
			{
				ans+=(((s[j]-s[i])*(e[j]-e[i]))<0);
			}
			printf("%d\n",ans);
	}

	return 0;
}