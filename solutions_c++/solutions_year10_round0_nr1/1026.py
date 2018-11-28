#include<cstdio>
#include<vector>
#include<algorithm>
#include<set>
#include<string>
#include<map>
#include<iostream>
using namespace std;

int t,n,k;
vector<int> rec;

int main() {
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    scanf("%d",&t);
    for (int i=0; i<t; i++) {
        scanf("%d%d",&n,&k);
        k%=1<<n;
        if (k==(1<<n)-1) printf("Case #%d: ON\n",i+1);
           else printf("Case #%d: OFF\n",i+1);
        }
    
}
