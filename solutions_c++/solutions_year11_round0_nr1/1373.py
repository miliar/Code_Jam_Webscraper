#include<iostream>

using namespace std;
struct node{
    char s[10];
    int p;
}a[1000];

void deal(void)
{
    int n;
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        scanf("%s%d",a[i].s,&a[i].p);
    }
    int t=0,t0=0,t1=0,p0=1,p1=1,z;
    for(int i=0;i<n;i++){
        if(a[i].s[0]=='B'){
            z=p0-a[i].p;
            p0=a[i].p;
            if(z<0)
                z=-z;
            t0+=z;
            if(t0<t1){
                t0=t1;
            }
            t0++;
            t=t0;
        }
        else{
            z=p1-a[i].p;
            p1=a[i].p;
            if(z<0)
                z=-z;
            t1+=z;
            if(t1<t0){
                t1=t0;
            }
            t1++;
            t=t1;
        }
    }
    printf("%d\n",t);
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
