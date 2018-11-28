#include<iostream>
#include<queue>
#include<set>
#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<math.h>
using namespace std;
#define eps 1e-8
#define QQ system("pause");
#define zero(x) (((x)>0?(x):-(x))<eps)
#define pi acos(-1.0)
int D(int x,int y){
    return abs(x-y)+1;
}
int main(){
    //freopen("A-small-attempt3.in","r",stdin);
      int pos,o1,b1,t,n,flag,ans,w=0,total;
      char ch[2];
      cin>>t;
      while(t--){
        cin>>n;
         o1=1;
         b1=1;
         ans=0;
        for(int i=1;i<=n;i++){
          scanf("%s %d",ch,&pos);
          if(i==1){
             if(ch[0]=='O') {flag=1;total=D(pos,1);ans=total;o1=pos;}
             else {flag=2;total=D(pos,1);ans=total;b1=pos;}
          }
          else{
             if(ch[0]=='O'){
                if(flag==1){
                    total+=D(pos,o1);
                    ans+=D(pos,o1);
                    
                }
                else{
                    flag=1;
                    int dis=D(pos,o1)-1;
                    if(dis<=total) {ans++;total=1;}
                    else{
                        ans+=dis-total+1;
                        total=dis-total+1;
                    }
                }
                o1=pos;

             }else{
                if(flag==2){
                    total+=D(pos,b1);
                    ans+=D(pos,b1);
                   
                }
                else{
                    flag=2;
                    int dis=D(pos,b1)-1;
                    if(dis<=total){
                        ans++; total=1;
                    }else{
                         ans+=dis-total+1;
                        total=dis-total+1;
                    }
                }
                 b1=pos;
             }
          }
        }
         printf("Case #%d: %d\n",++w,ans);
     }
    // while(1);
}
/*
3
4 O 2 B 1 B 2 O 4
3 O 5 O 8 B 100
2 B 2 B 1
*/
