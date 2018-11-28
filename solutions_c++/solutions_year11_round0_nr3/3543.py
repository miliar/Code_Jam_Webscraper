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
   int index = 0;
   int temp1 = 0;
   int temp2 = 0;
   int check = 0;
   int flag = 0;
   
   sorta(lst);

   REP(i, size) {
      temp1 = temp1 ^ lst[i];
      int j = i+1;
      loop(j, size) {
         temp2 = temp2 ^ lst[j];
         index += lst[j];
      }

      if (temp1 == temp2) {
         printf("%d", index);
         i = size;//stop the loop 
      } else {
         temp2 = 0;
         index = 0;
      }
   }
   if(temp1 != temp2)
      printf("NO");
   return;
}

int main(int argc, char **args)
{

	printf("Done\n");
   freopen("C-large.in", "r", stdin); freopen("largeC.out", "w", stdout);
   // freopen("C-small.in", "r", stdin); freopen("smallC.out", "w", stdout);

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

