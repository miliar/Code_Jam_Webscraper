#include <cstdio>
#include <cstdlib>
#include <memory.h>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <cmath>
#include <queue>
#include <cassert>
using namespace std;
int T, N;
int save_position = 1;

int old_position = 1;
int cur_position = 1;

int wait_time = 0;
long long int ans = 0;

int main() {
  freopen("A-large.in" , "r" , stdin);
  freopen("A-large-out" , "w" , stdout);
   int i;
   int Case = 1;
   scanf("%d", &T);
   char cur_type = 'B';
   char old_type = 'O';
   while (T --) {
     ans = 0;
     scanf("%d", &N);
     scanf("%s", &old_type);
     scanf("%d", &old_position);
     save_position = 1;
     ans += old_position;
     wait_time = old_position;
      
     for (i = 1; i < N; i ++) {
       scanf("%s", &cur_type);
       scanf("%d", &cur_position);
       
       if(cur_type == old_type) {
	 ans += abs(cur_position - old_position) + 1;
	 wait_time += abs(cur_position - old_position) + 1;
	 old_position = cur_position;
       } else {
	 
	 if(wait_time <= abs(cur_position - save_position)) {
	   ans += abs(cur_position - save_position) - wait_time + 1;
	   wait_time = abs(cur_position - save_position) - wait_time + 1;
	 }
	 else  {
	   ans += 1;
	   wait_time = 1;
	 }
	 save_position = old_position;
	 old_type = cur_type;
	 old_position = cur_position;
       }
     }
     printf("Case #%d: %lld\n", Case ++, ans);
   }
   return 0;
}
