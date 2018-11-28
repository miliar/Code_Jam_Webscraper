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

bool have[5000];
int M[1100];
int len[5000];


int dfs(int index)
{
	if(len[index]!=-1)return len[index];
	if(index==0)return 0;
	return dfs((index-1)/2)+1;
}
void buildLen()
{
	int i=0;
	for(i=1100;i>=0;i--)
	{
		len[i]=dfs(i);
	}
}
int main()
{
	//freopen("B-small-attempt0.in","r",stdin);freopen("B-small-output.txt","w",stdout);
	freopen("B-small-attempt1.in","r",stdin);freopen("B-small-output.txt","w",stdout);
	//freopen("A-large.in","r",stdin);freopen("A-large-output.txt","w",stdout);
	int T;
	scanf("%d",&T);
	memset(len,-1,sizeof(len));
	buildLen();
	for(int Case=1;Case<=T;Case++)
	{
		memset(have,false,sizeof(have));
		int P;
		scanf("%d",&P);
		int i=0,j=0;
		for(i=0;i<two(P);i++)
		{
			scanf("%d",&M[i]);
		}
		for(i=P-1;i>=0;i--)
		{
			int tmp;
			for(j=0;j<two(i);j++)
				scanf("%d",&tmp);
		}
		if(P==1)
		{
			if(M[0]==0 || M[1]==0)
				printf("Case #%d: 1\n",Case);
			else
				printf("Case #%d: 0\n",Case);
			continue;
		}
		for(i=0;i<two(P);i++)
		{
			int index = two(P)+i-1;
			//if(P==1)index = i+1;
			int l = 0;
			index = (index-1)/2;
			while(true)
			{
				if(l>=M[i])
					have[index]=true;
				if(index==0)break;
				index=(index-1)/2;
				l++;
			}
		}
		int ret = 0;
		for(i=0;i<2100;i++)if(have[i])ret++;
		printf("Case #%d: %d\n",Case,ret);
	}
}