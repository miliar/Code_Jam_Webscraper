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
int n;
bool p[2000];
int l,r;
int x;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&T);
    for (int i=2;i<=1000;i++)
        if (!p[i])
            for (int j=2*i;j<=1000;j+=i) p[j]=true;
    for (int k=1;k<=T;k++){
        scanf("%d",&n);
        if (n==1) l=1,r=1;
        else{
            l=0;r=1;
            for (int i=2;i<=n;i++)
                if (!p[i]){
                    l++;
                    x=i;
                    while (x<=n){
                        x*=i;r++;
                    }
                }
        }
        printf("Case #%d: %d\n",k,r-l);
    }
    return 0;
}
