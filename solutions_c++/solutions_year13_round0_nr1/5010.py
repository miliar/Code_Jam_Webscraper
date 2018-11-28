#include<cstdio>
#include<cmath>
#include<iostream>
#include<ctime>
#include<cstring>
#include<algorithm>
#include<string>
#include<queue>
#define L(r) (r<<1)
#define R(th) (th<<1|1)
#define LL long long
using namespace std;
#define MA 100005

 //priority_queue<int, vector<int>,greater<int> > q;
char map[10][10],tmap[10][10];
int heng(int h){
   if(tmap[h][1]==tmap[h][0] && tmap[h][2]==tmap[h][0]&& tmap[h][3]==tmap[h][0])
     return 1;
   return 0;
}
int shu(int s){
    if(tmap[0][s]==tmap[1][s]&& tmap[0][s]==tmap[2][s]&&tmap[0][s]==tmap[3][s])
       return 1;
    return 0;
}
int xie(){
    if(tmap[0][0]==tmap[1][1]&& tmap[0][0]==tmap[2][2]&&tmap[0][0]==tmap[3][3])
       return 1;
    return 0;
}
int xie2(){
    if(tmap[3][0]==tmap[2][1]&& tmap[3][0]==tmap[1][2]&&tmap[3][0]==tmap[0][3])
       return 1;
    return 0;
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

   int cas;
   int cc=0;
   scanf("%d",&cas);
      while(cas--){
       int ans=-1;
       for(int i=0;i<4;++i){
        scanf("%s",map[i]);
       }
       for(int i=0;i<4;++i)
         for(int j=0;j<4;++j)
            if(map[i][j]=='T')
                tmap[i][j]='X';
            else
                tmap[i][j]=map[i][j];
       for(int i=0;i<4;++i){
           if(tmap[0][i]=='X')
             if(shu(i))
             {
                 ans=0;
                 break;
             }
           if(tmap[i][0]=='X')
              if(heng(i))
             {
                 ans=0;
                 break;
             }
           if(i==0 && tmap[0][0]=='X')
             if(xie()){
                ans=0;
                break;
             }
           if(i==0 && tmap[3][0]=='X')
             if(xie2()){
                ans=0;
                break;
             }
       }
       if(ans==-1){
       for(int i=0;i<4;++i)
         for(int j=0;j<4;++j)
            if(map[i][j]=='T')
                tmap[i][j]='O';
            else
                tmap[i][j]=map[i][j];
       for(int i=0;i<4;++i){
           if(tmap[0][i]=='O')
             if(shu(i))
             {
                 ans=1;
                 break;
             }
           if(tmap[i][0]=='O')
              if(heng(i))
             {
                 ans=1;
                 break;
             }
           if(i==0 && tmap[0][0]=='O')
             if(xie()){
                ans=1;
                break;
             }
            if(i==0 && tmap[3][0]=='O')
             if(xie2()){
                ans=1;
                break;
             }
       }
       }
       if(ans==-1){
          for(int i=0;i<4;++i)
            for(int j=0;j<4;++j)
              if(map[i][j]=='.')
              {
                ans=3;break;
              }
          if(ans==-1)
            ans=2;
       }
       printf("Case #%d: ",++cc);
       if(ans==0){
           printf("X won\n");
       }
       else if(ans==1){
          printf("O won\n");
       }
       else if(ans==2){
          printf("Draw\n");
       }
       else {
          printf("Game has not completed\n");
       }
   }
   return 0;
}
/*
LL x,y;
LL exgcd(LL a,LL b,LL &x,LL &y){
    LL res,t;
    if(b==0)
    {
        x=1;y=0;
        return a;//·µ»ØµÄÊÇgcd£»
    }
    res=exgcd(b,a%b,x,y);
    t=x;
    x=y;
    y=t-(a/b)*y;
    return res;
}
LL fast_mod(__int64 js,__int64 cs,__int64 mod) {
    __int64 t=js%mod,res=1;
    while(cs) {
        if(cs&1)
           res=res*t%mod;
        t=t*t%mod;
        cs>>=1;
    }
    return res;

}
*/
