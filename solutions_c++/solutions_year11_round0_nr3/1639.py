#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstring>

using namespace std;

#define ll long long

int T,n;
int sum,mn;
int r[50];
int c;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&T);
    for (int k=1;k<=T;k++){
        scanf("%d",&n);
        memset(r,0,sizeof(r));
        sum=0;
        for (int i=0;i<n;i++){
            scanf("%d",&c);
            if (i==0||mn>c) mn=c;
            sum+=c;
            for (int j=0;j<50;j++){
                if (c==0) break;
                r[j]+=c%2;
                c/=2;
            }
        }
        bool p=true;
        for (int i=0;i<50;i++)
            if (r[i]%2!=0){
                p=false;
                break;
            }
        printf("Case #%d: ",k);
        if (p) printf("%d\n",sum-mn);
        else printf("NO\n");
    }
    return 0;
}
