#define mset(a) memset(a,0,sizeof(a))

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
int a[2000],b[2000];
int main()
{
int t,tt;
cin>>t;
for(tt=1;tt<=t;tt++)
{
    int n;
	cin >>n;
	for(int i=0;i<n;i++)
        cin>>a[i];
    memcpy(b,a,sizeof(a));
    sort(&a[0],&a[n]);
    double ans=0;
    for(int i=0;i<n;i++)
        if(a[i]!=b[i])
            ans+=1;
    printf("Case #%d: %.6f\n",tt,ans);


}

return 0;
}
