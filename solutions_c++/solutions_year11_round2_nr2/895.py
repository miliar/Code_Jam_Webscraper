#include<iostream>
#include<stdio.h>
#include<map>
#include<stdlib.h>
#include<algorithm>
#include<vector>
#include<string>
#include<math.h>
using namespace std;
struct f
{
    int p,v;
}node[1000000];
int sum,n,d;
int cmp(const void *a,const void *b)
{
    return (*(struct f*)a).p-(*(struct f*)b).p;
}
bool check(double t)
{
    double pos=node[0].p-t;
    int i,j;
    for(i=0;i<n;i++) {
        for(j=0;j<node[i].v;j++) {
           // if(t==6.0/2) cout<<pos<<"a"<<endl;
            if(node[i].p>=pos) {
                if(node[i].p-t>=pos) pos=node[i].p-t+d;
                else pos+=d;
            }
            else {
                if(node[i].p+t>=pos) pos=pos+d;
                else return false;
            }
        }
    }
    return true;
}

double bs(double left,double right)
{
    if(right-left<=0.000001) {
        if(check(left)) return left;
       // return -1;
    }
    double mid=(left+right)/2;
    if(check(mid)) return bs(left,mid);
    return bs(mid+1e-6,right);
}
int main()
{
    //freopen("B-small-attempt1.in","r",stdin);
    //freopen("out.txt","w",stdout);
    int t,k,i;
    double ans,pos,dis;
    scanf("%d",&t);
    for(k=1;k<=t;k++) {
        scanf("%d%d",&n,&d);
        sum=0;
        for(i=0;i<n;i++) {
            scanf("%d%d",&node[i].p,&node[i].v);
            sum+=node[i].v;
        }
        qsort(node,n,sizeof(node[0]),cmp);
        printf("Case #%d: ",k);
        //cout<<(double)(sum-1)*d<<endl;
        cout<<bs(0,(double)(2*sum)*d)<<endl;
    }
    //system("pause");
    return 0;
}
