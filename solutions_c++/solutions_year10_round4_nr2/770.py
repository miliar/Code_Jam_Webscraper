#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<math.h>
#include<map>
using namespace std;
int ans,a[1100],b[1100];
int solve(int l,int r)
{
    int i,flag,mid;
    flag=0;
    for(i=l;i<=r;i++) {
        if(a[i]!=0) {
            flag=1;
            break;
        }
    }
    if(flag==0) return 0;
    mid=(l+r)>>1;
    for(i=l;i<=r;i++) {
        if(a[i]!=0) a[i]--;
    }
    return 1+solve(l,mid)+solve(mid+1,r);
}

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
  //  freopen("B-small-attempt1.in","r",stdin);
  //  freopen("B-small-attempt2.in","r",stdin);
  //  freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    
    int t,p,i,num,k;
    scanf("%d",&t);
    for(k=1;k<=t;k++) {
        scanf("%d",&p);
        num=(int)pow(2,p);
        for(i=0;i<num;i++) {
            scanf("%d",&a[i]);
            a[i]=p-a[i];
        }
        
        for(i=num-1;i>0;i--) scanf("%d",&b[i]);
        ans=solve(0,num-1);
        printf("Case #%d: %d\n",k,ans);
    }
    return 0;
}
