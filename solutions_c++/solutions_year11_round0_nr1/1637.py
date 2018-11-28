#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstring>

using namespace std;

#define ll long long

int n;
int T;
char r[200];
int p[200];
int t;
int t1,t2;
int p1,p2;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&T);
    for (int k=0;k<T;k++){
        scanf("%d ",&n);
        for (int i=0;i<n;i++) scanf("%c %d ",&r[i],&p[i]);
        t=0;t1=0;t2=0;
        p1=1;p2=1;
        for (int i=0;i<n;i++)
            if (r[i]=='O'){
                t=max(t,t1+abs(p[i]-p1))+1;
                p1=p[i];t1=t;
            }else{
                t=max(t,t2+abs(p[i]-p2))+1;
                p2=p[i];t2=t;
            }
        printf("Case #%d: %d\n",k+1,t);
    }
    return 0;
}
