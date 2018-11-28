#include<iostream>
using namespace std;

#define abs(x) ((x)<0?(-(x)):(x))

int isOk(int a,int b,int c){
    if(abs(b-a)==2) return 1;
    if(abs(c-a)==2) return 1;
    if(abs(c-b)==2) return 1;
    return 0;
}

int N,S,p;
int best;
int score[105];

void solve(int step,int numS,int nump){
     if(step==N){
         if(numS==S){
             if(nump>best)
                best=nump;
         }
         return ;
     }
     if(numS>S) return ;
     int a,b,c;
     for(a=0;a<=10;a++)
        for(b=a;b-a<=2;b++)
           for(c=b;c-a<=2&&c-b<=2;c++){
                if(a+b+c!=score[step]) continue;
                int k1=0,k2=0;
                if(isOk(a,b,c)) k1=1;
                if(c>=p) k2=1;
                solve(step+1,numS+k1,nump+k2);                       
           }
     return ;
}

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("data.out","w",stdout);
    int t;
    scanf("%d",&t);
    int ca;
    for(ca=1;ca<=t;ca++){
        scanf("%d %d %d",&N,&S,&p);     
        best=0;
        int i;
        for(i=0;i<N;i++)
           scanf("%d",&score[i]);
        solve(0,0,0);
        printf("Case #%d: %d\n",ca,best);           
    }
}
