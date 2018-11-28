#include <iostream>
#include <set>

#include <sstream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
using namespace std;
typedef long long LL;

void readInput(char tn)
{
   ostringstream oss;
   oss<<"C-small-attempt"<<tn<<".in";
   string inputName = oss.str();
   oss.clear();
   oss<<"C-small-attempt"<<tn<<".txt";
   string outputName = oss.str();

   freopen(inputName.c_str(), "r", stdin);
   freopen(outputName.c_str(),"w",stdout);

}

int getLen(int n)
{
   int ret = 0;
   while(n) {
      n/=10;
      ret++;
   }
   return ret;
}
LL p10[10];
LL mark[2000010];


LL solve(int a, int b)
{

   int len = getLen(b);
   LL ret = 0;
   for(int i = a; i <= b; i++) {
      set<int> snms;
      for(int j = 1; j <= len - 1; j++) {
         int right = i%p10[j];
         int left = i/p10[j];
         right*=p10[len-j];
         right+=left;
         if(right<p10[len-1]) continue;
         if(right>i&&right<=b) {
            snms.insert(right);
         }
      }
      ret+=snms.size();


   }
   return ret;
}

void precal()
{
   p10[0]=1;
   for(int i = 1; i <= 7; i++) p10[i]=p10[i-1]*10;
}


int main()
{
  // readInput(0);
   freopen("C-large.in","r",stdin);
   freopen("C-large.out","w",stdout);
   precal();
   int T;
   scanf("%d",&T);
   for(int tc = 1; tc <= T; tc++) {
      memset(mark,0,sizeof(mark));
      int a, b;
      scanf("%d %d",&a,&b);
      printf("Case #%d: %lld\n", tc, solve(a,b));
   }
   return 0;
}
