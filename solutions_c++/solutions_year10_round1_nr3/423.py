#include<iostream>
#include<cmath>
#include<algorithm>
#include<string>
#include<cstring>
using namespace std;
bool solve(int a,int b){
     if(a==b)return 0;
     if(a<=0||b<=0)return 0;
     if(a>=2*b)return 1;
     int x,y;
     x=b,y=a-b;
     if(x<y)swap(x,y);
     return !solve(x,y);
}
int main()
{
     freopen("C-small-attempt1.in","r",stdin);//A-small-attempt0.in
     freopen("1.txt","w",stdout);
     int T,i,j,k,a1,a2,b1,b2;
     scanf("%d",&T);
     for(int test=0;test<T;test++){
          scanf("%d%d%d%d",&a1,&a2,&b1,&b2);
          int cnt=0;
          for(i=a1;i<=a2;i++)
          for(j=b1;j<=b2;j++){
             int a=i,b=j;
             if(a<b)swap(a,b);
             if(solve(a,b))cnt++;
          }
          printf("Case #%d: %d\n",test+1,cnt);
     }
}
