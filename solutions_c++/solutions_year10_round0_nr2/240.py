#include"iostream"
using namespace std;
int dat[1001];
int gcd(int a,int b){
    if(b==0)return a;
    else return gcd(b,a%b);
}
int ab(int x){
    return x<0?-x:x;
}
int main(){
    int T,N,gc,y;
    freopen("B-small-attempt1.in","r",stdin);
    freopen("outB2test3.txt","w",stdout);
    scanf("%d",&T);
    for(int i=1;i<=T;i++){
        scanf("%d",&N);
        for(int j=0;j<N;j++){
           scanf("%d",&dat[j]);
           if(j==1)gc=ab(dat[1]-dat[0]);
           else if(j>1)gc=gcd(gc,ab(dat[j]-dat[j-1]));
        }
        int max;
        if(gc==1 || dat[0]%gc==0)max=0;
        else{
         max=0;
         for(int j=0;j<N;j++){
          y=dat[j]%gc;
          if(y<0)y+=gc;
         }
         y=gc-y;
         if(y>max)max=y;
        }
        printf("Case #%d: %d\n",i,max);
        //if(gc<gc-y)cout<<1<<endl;
        //printf("Case %d: %d\n",i,gc);
        //printf("Case %d: %d\n",i,gc-y);
    }
 //   system("pause");
    return 0;
}
