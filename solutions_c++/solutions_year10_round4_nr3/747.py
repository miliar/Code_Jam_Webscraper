#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>

using namespace std;

typedef __int64 int64;
#define two(X) (1<<(X))
#define twoL(X) (((int64)(1))<<(X))
#define contain(S,X) (((S)&two(X))!=0)
#define containL(S,X) (((S)&twoL(X))!=0)
const double pi=acos(-1.0);
const double eps=1e-11;
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}
template<class T> inline T min(T a,T b){return a<b?a:b;}
template<class T> inline T max(T a,T b){return a>b?a:b;}
template<class T> inline T sqr(T x){return x*x;}
typedef pair<int,int> ipair;
#define SIZE(A) ((int)A.size())
#define LENGTH(A) ((int)A.length())
#define MP(A,B) make_pair(A,B)


bool tb[110][110];

int main()
{
	freopen("C-small-attempt0.in","r",stdin);freopen("C-small-output.txt","w",stdout);
	//freopen("A-small-attempt1.in","r",stdin);freopen("A-small-output.txt","w",stdout);
	//freopen("A-large.in","r",stdin);freopen("A-large-output.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int Case=1;Case<=T;Case++)
	{
		memset(tb,false,sizeof(tb));
		int ret = 0;
		int k,i,j,R;
		scanf("%d",&R);
		for(k=0;k<R;k++)
		{
			int x1,x2,y1,y2;
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			for(i=x1;i<=x2;i++)for(j=y1;j<=y2;j++)
				tb[i][j]=true;
		}
		bool go=true;
		while(go)
		{
			go=false;
			ret++;
			for(i=108;i>0;i--)for(j=108;j>0;j--)
			{
				if(tb[i][j])go=true;
				if(tb[i-1][j] && tb[i][j-1])tb[i][j]=true;
				if(!tb[i-1][j] && !tb[i][j-1])tb[i][j]=false;
			}
		}
		printf("Case #%d: %d\n",Case,ret-1);
	}
}