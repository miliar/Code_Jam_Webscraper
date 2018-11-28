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
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int pr[105];
int p,q;
int dp[105][105];
int f(int left,int right)
{
  int ret=pr[right]-pr[left];
  if(left>0)
  ret+=pr[left]-pr[left-1]-1;
  else
  ret+=pr[left]-1;
  if(right<q-1)
  ret+=pr[right+1]-pr[right]-1;
  else
  ret+=p-pr[right];
  return ret;
    
}

int go(int left,int right)
{
    if(left>right)return 0;
 if(left==right)return f(left,right);
 int &ret=dp[left][right];
 if(ret==-1)
 {
  ret=20000000;
  for(int i=left;i<=right;++i)
  {
   int temp=f(left,right);
   temp+=go(left,i-1);
   temp+=go(i+1,right);
   if(ret>temp)ret=temp;
  }
 }
 return ret;
}

int main()
{

//	freopen("A.in","r",stdin);
//	freopen("C:\\data\\C-small.in","r",stdin);freopen("C:\\data\\C-small1.out","w",stdout);
	freopen("C:\\data\\C-large.in","r",stdin);freopen("C:\\data\\C-large.out","w",stdout);	
//	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
//	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
   int t;
   scanf("%d",&t);
   for(int cas=1;cas<=t;++cas)
   {
    scanf("%d%d",&p,&q);
    for(int i=0;i<q;++i)
            scanf("%d",&pr[i]);
    sort(pr,pr+q);
    memset(dp,255,sizeof(dp));
    int ret=go(0,q-1);
    printf("Case #%d: %d\n",cas,ret);
   }
    return 0;
}
