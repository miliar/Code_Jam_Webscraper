#include <iostream>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <vector>
#include <stack>
#define maxn 1000000007
#define VI vector<int>
#define VS vector<string>
#define MSI map<string,int>
#define N 100
  using namespace std;
  int pd,pg;
  long long n;
  int d,g;

int main(){
  freopen("a.in","r",stdin);freopen("a.out","w",stdout);
  int i;
  int tc,tt;
  scanf("%d",&tc);
  for(tt=1;tt<=tc;tt++){
    printf("Case #%d: ",tt);
    scanf("%lld%d%d",&n,&pd,&pg);
    if(pd<100 && pg==100 || pd>0 && pg==0){
      printf("Broken\n");
      continue;
    }
    for(d=1;d<=100;d++)
      if(pd*d % 100 ==0)break;
    if(d>n)
      printf("Broken\n");
    else
      printf("Possible\n");
  }

  
  return 0;
}
