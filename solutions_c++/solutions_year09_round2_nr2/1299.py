#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <queue>
#include <set>
#include <cmath>
#include <stack>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
const int inf=(1<<30);
#define mset(a,x) memset(a,x,sizeof(a))
#define ABS(a) ((a) >= 0 ? (a) : -(a))
#define dbg(x) cerr<<#x<<" : "<<x<<endl
int T;

int main() 
{
    freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	scanf("%d", &T);
	int cnt=0;
	while (T--) {
	       ll num;
		   ll num2;
		   vector<int> vec;
		   stack<int> stk;
		   scanf("%I64d", &num);
		   num2=num;
		   while (num) {
		          stk.push(num%10);
				  num/=10;
		   }
		   while (!stk.empty()) {vec.push_back(stk.top());stk.pop();}
		   printf("Case #%d: ", ++cnt);
		   if (next_permutation(vec.begin(), vec.end())) {
		       for (int i = 0; i < vec.size(); i++) {
		            printf("%d", vec[i]);
		       }
		       puts("");
		   }
		   else {
		       while (vec[0]==0) {
			          next_permutation(vec.begin(), vec.end());
			   }
			   printf("%d", vec[0]);
			   printf("0");
			   for (int i = 1; i < vec.size(); i++)
				    printf("%d", vec[i]);
			   puts("");
		   }
		   
	}
    return 0;
}
