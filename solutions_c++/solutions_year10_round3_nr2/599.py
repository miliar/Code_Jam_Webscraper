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

const double PI = acos(-1.0);

int main() {
   freopen("B-small-attempt2.in", "r", stdin);
freopen("B-small-attempt0.out", "w", stdout);
    //freopen("Alarge.in", "r", stdin);
    //freopen("Alarge.out", "w", stdout);

    int i, j, k;
    int casenum;
    int least, high, factor;
    int ans,temp,value;
    scanf("%d", &casenum);
    for(i =1;i<= casenum;i++)
    {
        ans = 0;
        scanf("%d%d%d",&least, &high,&factor);
        long cur = least * factor;
        temp = 0;
        while(cur<high)
        {
            cur=cur*factor;
            temp++;
        }
        for(ans=0;;++ans)
        {
            if((1<<ans)>temp)break;
        }
        printf("Case #%d: %d\n",i, ans);
    }
	return 0;
}
