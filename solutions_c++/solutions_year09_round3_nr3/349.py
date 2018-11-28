#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <ctime>
#include <cstring>
#include <climits>
#include <queue>
using namespace std;
int b[102];
char s[10002];
int main(){
    int n,q,no=1,t;
    scanf("%d",&t);
    while(t--){
        scanf("%d %d",&n,&q);
        for(int i=0;i<q;i++) scanf("%d",&b[i]);

        sort(b,b+q);
        int ans=INT_MAX;
        do{
            memset(s,0,sizeof(s));
            int sp=0;
            for(int i=0;i<q;i++){
                s[b[i]]=1;
                int sum=0;
                for(int j=b[i]-1;j>0&&s[j]==0;j--)sum++;
                for(int j=b[i]+1;j<=n&&s[j]==0;j++)sum++;
                sp+=sum;

            }
            ans<?=sp;
        }while(next_permutation(b,b+q));
        printf("Case #%d: %d\n",no++,ans);
    }

    return 0;
}

