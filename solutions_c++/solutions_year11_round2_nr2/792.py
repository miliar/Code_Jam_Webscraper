#include<iostream>

using namespace std;

struct node{
    int p;
    int v;
    int idx;
}a[300];
int c,d,s;

int f(double t)
{
    double pos;
    for(int i=0,j=0;i<s;i++){
        if(i>=a[j].idx){
            j++;
        }
        if(i==0){
            pos=(double)a[j].p - t;
            continue;
        }
        pos+=d;
        //cerr<<"time="<<t<<" i="<<i<<" j="<<j<<" pos="<<pos<<endl;
        if(a[j].p-t>pos){
            pos=(double)a[j].p-t;
        }
        if(pos>a[j].p+t){
            return 0;
        }
    }
    return 1;
}

void deal(void)
{
    s=0;
    scanf("%d%d",&c,&d);
    for(int i=0;i<c;i++){
        scanf("%d%d",&a[i].p,&a[i].v);
        s+=a[i].v;
        a[i].idx=s;
    }
    double l=0.0,r=(double)s*d,mid;
    while(l+1e-8<r){
        mid=(l+r)/2;
        //cerr<<"mid = "<<mid<<endl;
        if(f(mid)==1){
            r=mid;
        }
        else{
            l=mid;
        }
    }
    printf("%lf\n",mid);
}

int main(void)
{
    int num=0;
    scanf("%d",&num);
    for(int i=1;i<=num;i++){
        printf("Case #%d: ",i);
        deal();
    }
    return 0;
}
/* vim: set expandtab ts=4 sw=4 sts=4 tw=100: */
