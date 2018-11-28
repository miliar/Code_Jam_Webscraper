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

int main(void)
{
    int cases,n,t;
    int i=0;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&cases);
    for(i=1;i<=cases;i++){
        scanf("%d%d",&n,&t);
        t=t%(1<<n);
        if(t!=(1<<n)-1)printf("Case #%d: OFF\n",i);
        else printf("Case #%d: ON\n",i);
    }
    return city;
}
