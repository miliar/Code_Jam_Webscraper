#include<iostream>
using namespace std;

long long input[10003][2];
//int col[10003];

struct node{
       long long ind,len;
};
node queue[10005];
int head,tail;

#define _min(x,y) ((x)<(y)?(x):(y))

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("data.out","w",stdout);
    
    int t;
    cin>>t;
    int ca;
    for(ca=1;ca<=t;ca++){
        int n;                 
        cin>>n;
        int i;
        for(i=0;i<n;i++)
          scanf("%I64d%I64d",&input[i][0],&input[i][1]);
//        memset(col,0,sizeof(col));
        long long D;
        scanf("%I64d",&D);
        head=tail=0;
        int res=0;
        node u;
        u.ind=input[0][0];
        u.len=_min(input[0][0],input[0][1]);
        int ind=1;
        queue[tail++]=u;
        while(head<tail){
            u=queue[head++];
            if(u.ind+u.len>=D){res=1;break;}
            for(;ind<n;ind++){
               if(input[ind][0]<=u.ind+u.len){
                   node v;
                   v.ind = input[ind][0];
                   v.len = _min(input[ind][1],input[ind][0]-u.ind);
                   queue[tail++]=v;
               }
               else break;
            }
        }
        if(res) printf("Case #%d: YES\n",ca);
        else printf("Case #%d: NO\n",ca);
    }
}
