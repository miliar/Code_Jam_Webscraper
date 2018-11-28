#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstring>

using namespace std;

#define ll long long

int T;
int n,l,h;
int a[200];
int ans;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&T);
    for (int k=1;k<=T;k++){
        scanf("%d%d%d",&n,&l,&h);
        for (int i=0;i<n;i++) scanf("%d",&a[i]);
        ans=-1;
        for (int i=l;i<=h;i++){
            bool p=true;
            for (int j=0;j<n;j++)
                if ((a[j]%i!=0)&&(i%a[j]!=0)){
                    p=false;
                    break;
                }
            if (p){
                ans=i;
                break;
            }
        }
        printf("Case #%d: ",k);
        if (ans==-1) printf("NO\n");
        else printf("%d\n",ans);
    }
    return 0;
}
