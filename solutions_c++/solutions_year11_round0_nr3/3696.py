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
#include <string.h>

using namespace std;


typedef vector<int> vi;
#define all(a) a.begin(),a.end()
#define sorta(a) sort(all(a))
#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define loop(i,n) for(;i<(int)(n);(i)++)
#define forit(a,b) for(typeof((b).end()) a=(b).begin();a!=(b).end();a++)

//Global Values
const int maxsize=100000000;

int item[maxsize];
int n;

void solve(int size, int ary[])
{
   int i;
   vi lst (ary, ary+size);
   int count = 0;
   int tmp1 = 0;
   int tmp2 = 0;
   int check = 0;
   int flag = 0;
   
   sorta(lst);

   REP(i, size) {
      tmp1 = tmp1 ^ lst[i];
      int j = i+1;
      loop(j, size) {
         tmp2 = tmp2 ^ lst[j];
         count += lst[j];
      }

      if (tmp1 == tmp2) {
         printf("%d", count);
         i = size;//stop the loop 
      } else {
         tmp2 = 0;
         count = 0;
      }
   }
   if(tmp1 != tmp2)
      printf("NO");
   return;
}

int main(int argc, char **args)
{


   // freopen("C-large.in", "r", stdin); freopen("largeC.out", "w", stdout);
   freopen("C-large.in", "r", stdin); freopen("largeC.out", "w", stdout);

   int testcase, i;
   scanf("%d", &testcase);
   
   for(int caseId=1;caseId<=testcase;caseId++)
   {
      printf("Case #%d: ", caseId);
      scanf("%d", &n);
      REP(i, n) {scanf("%d", &item[i]);};
      
      solve(n, item);
      
      printf("\n");
      fflush(stdout);
   }
   return 0;
}

