#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<iostream>
#include<algorithm>
using namespace std;
struct dots
{
double x,y;
}ta,tb;

struct lines
{
struct dots a,b;
}data[1005];

int iscross(struct lines m,struct lines n)
{
double v1,v2,v3,v4;
v1=(m.b.x-m.a.x)*(n.b.y-m.a.y) - (m.b.y-m.a.y)*(n.b.x-m.a.x);
v2=(m.b.x-m.a.x)*(n.a.y-m.a.y) - (m.b.y-m.a.y)*(n.a.x-m.a.x);
if(v1*v2>=0)
return 0;
v3=(n.b.x-n.a.x)*(m.b.y-n.a.y) - (n.b.y-n.a.y)*(m.b.x-n.a.x);
v4=(n.b.x-n.a.x)*(m.a.y-n.a.y) - (n.b.y-n.a.y)*(m.a.x-n.a.x);
if(v3*v4>=0)
return 0;
return 1;
}
int main (){
    int tn,ca=0,N,count,i,j;
    scanf("%d",&tn);
    while(tn--){
        scanf("%d",&N);
        for(i=0;i<N;i++){
            scanf("%d %d",&ta.y,&tb.y);
            data[i].a.y = ta.y;data[i].b.y = tb.y;
            data[i].a.x = 0;data[i].b.x = 10;
        }
        count = 0;
        for(i=0;i<N;i++){
            for(j=i+1;j<N;j++){
                if(iscross(data[i],data[j]) == 1)
                    count++;
            }
        }
        ca++;
        printf("Case #%d: %d\n",ca,count);
    }
    return 0;   
}
