/*

*/
#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <string>
using namespace std;
int Case,n,l,h,a[110],t;
int can()
{
    int t1,t2;
    for (int i=l;i<=h;i++) {
        bool flag=true;
        for (int j=1;j<=n;j++) {
            t1=max(a[j],i);
            t2=min(a[j],i);
            if (t1%t2!=0) flag=false;
        }
        if (flag) return i;
    }
    return -1;
}
void display()
{
    scanf("%d",&Case);
    for (int ca=1;ca<=Case;ca++) {
        printf("Case #%d: ",ca);
        scanf("%d%d%d",&n,&l,&h);
        for (int i=1;i<=n;i++)
            scanf("%d",&a[i]);
        if ((t=can())==-1) printf("NO\n");
        else printf("%d\n",t);
    }
}
int main()
{
    //freopen("C-small-attempt1.in","r",stdin);
    //freopen("C-small-attempt1.out","w",stdout);
    display();
    return 0;
}

