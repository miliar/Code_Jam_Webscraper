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
int main()
{
  //  freopen("in.txt","r",stdin);
   // freopen("B-small-attempt0.in","r",stdin);
   // freopen("B-small-attempt1.in","r",stdin);
    //freopen("B-small-attempt2.in","r",stdin);
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    
    int t,flag,ans,tmp,l,p,c,sum;
    
    scanf("%d",&t);
    for(flag=1;flag<=t;flag++) {
        printf("Case #%d: ",flag);
        scanf("%d%d%d",&l,&p,&c);
        ans=0;
        tmp=p;
        while(tmp>l) {
            ans++;
            if(tmp%c==0) tmp=tmp/c;
            else tmp=tmp/c+1;
        }
        sum=0;
        while(ans!=1) {
            if(ans%2==0) ans/=2;
            else ans=ans/2+1;
            sum++;
        }
        printf("%d\n",sum);
    }
    return 0;
}
