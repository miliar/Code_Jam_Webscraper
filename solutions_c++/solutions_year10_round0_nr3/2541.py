#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <queue>
#include <string>
#include <vector>
#include <stack>
#include <map>
#include <algorithm>
#define city 0
#define SIZE 500000
using namespace std;

int r , n , k ;
int ans ;
queue<int>q;
int go(void)
{
    int per=0,cnt=0;
    while(1){
        if(per+q.front()>k)break;
        if(cnt==n)break;
        cnt++;
        per+=q.front();
        q.push(q.front());q.pop();
    }
    ans+=per;
    return city;
}
int main(void)
{
    int i , j  , cases , t,g;
    freopen("C-small-attempt0.in","r",stdin);
  //  freopen("C-small-attempt0.out","w",stdout);


    scanf("%d",&cases);
    for(t=1;t<=cases;t++){
        scanf("%d%d%d",&r,&k,&n);
        while(!q.empty())q.pop();
        for(i=0;i<n;i++){
            scanf("%d",&g);
            q.push(g);
        }
        ans=0;
        while(r--)go();
        printf("Case #%d: %d\n",t,ans);
    }
    return city;
}


