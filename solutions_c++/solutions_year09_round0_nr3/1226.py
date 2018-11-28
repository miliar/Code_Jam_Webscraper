#include <iostream>
#include <cstdio>
#include <string>

using std::cout ;
                      
char S[600],str[50]={"welcome to code jam"};
bool vis[506][30];
int  dp[506][30],cases=0;
int times;
int input(){
 gets(S);
 memset(vis,0,sizeof(vis));
}
int go(int lv,int pos){
// printf("%d %d %c %c\n",lv,pos,S[lv],str[pos]);
 if(pos==19)
 return 1;
 else if(!S[lv])
 return 0;
 else if(vis[lv][pos])
 return dp[lv][pos];
 else {
   int i,ans=0 ;
   ans=go(lv+1,pos);
   if(S[lv]==str[pos])
   ans+=go(lv+1,pos+1);
   ans%=10000;
   vis[lv][pos]=1;
   dp[lv][pos]=ans;
   return ans;      
 }   
}
int sol(){
 int i,ans=0 ;
 for(i=0;S[i];i++)
   if(S[i]=='w')
   ans+=go(i,1),ans%=10000;
   cases++;
   cout<<"Case #"<<cases<<':'<<' ';      
   int d[4]={0};
   for(i=0;i<4;i++)
   d[i]=ans%10,ans/=10;
   for(i=3;i>=0;i--)cout<<d[i];
   cout<<'\n';        
}
int main (){
 scanf("%d",&times);
 gets(S);
 while(times--){
   input();
   sol();               
 }   
}
