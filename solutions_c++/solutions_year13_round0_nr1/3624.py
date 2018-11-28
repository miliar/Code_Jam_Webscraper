#include<cstdio>
//#include<conio.h>
#include<set>
#include<cstring>
#include<algorithm>
#include<queue>
#include<cmath>
#include<iostream>
#include<vector>
using namespace std;
typedef long long LL;
typedef pair<int,int> pi;
typedef vector<int> vi;
typedef pair<int,int> pi;
typedef vector<pi> vpii;
#define pb push_back
#define nd second
#define st first
#define mp make_pair
#define rep(i,n) for(int i=0;i<n;i++)
#define inf 9999999999
#define MAX 1000000

      
int n,m,k,l,cas=1,empty=0;
string s[5];  
int actx = 0, acto = 0,act=0;
pair<int,int> p;
void read()
{
    rep(iii,4)
    { s[iii].clear();
        cin>>s[iii];      
    } 
}      
      
void solve()
{
     rep(i,4)
     {
             actx=acto=act=0;
             rep(j,4){
                if(s[i][j]=='X') actx++;
                if(s[i][j]=='O') acto++;
                if(s[i][j]=='T') act++;
                if(s[i][j]=='.') empty++;
                      }
                if(actx == 4 || (actx == 3 && act ==1))
                {
                   cout<<"Case #"<<cas<<": X won\n";  
                   return;        
                 }      
                  if(acto == 4 || (acto == 3 && act ==1))
                {
                   cout<<"Case #"<<cas<<": O won\n";  
                    return;           
                 }              
     }
      rep(i,4)
     {
             actx=acto=act=0;
             rep(j,4){
                if(s[j][i]=='X') actx++;
                if(s[j][i]=='O') acto++;
                if(s[j][i]=='T') act++;
                if(s[j][i]=='.') empty++;
                      }
                if(actx == 4 || (actx == 3 && act ==1))
                {
                   cout<<"Case #"<<cas<<": X won\n";
                    return;             
                 }      
                  if(acto == 4 || (acto == 3 && act ==1))
                {
                   cout<<"Case #"<<cas<<": O won\n";
                    return;             
                 }              
     }
     
      rep(i,4)
     {
             actx=acto=act=0;
             rep(j,4){
                if(s[j][j]=='X') actx++;
                if(s[j][j]=='O') acto++;
                if(s[j][j]=='T') act++;
                if(s[j][j]=='.') empty++;
                      }
                if(actx == 4 || (actx == 3 && act ==1))
                {
                   cout<<"Case #"<<cas<<": X won\n";  
                    return;           
                 }      
                  if(acto == 4 || (acto == 3 && act ==1))
                {
                   cout<<"Case #"<<cas<<": O won\n";  
                    return;           
                 }              
     }
     
     rep(i,4)
     {
             actx=acto=act=0;
             rep(j,4){
                if(s[j][3-j]=='X') actx++;
                if(s[j][3-j]=='O') acto++;
                if(s[j][3-j]=='T') act++;
                if(s[j][3-j]=='.') empty++;
                      }
                if(actx == 4 || (actx == 3 && act ==1))
                {
                   cout<<"Case #"<<cas<<": X won\n";  
                    return;           
                 }      
                  if(acto == 4 || (acto == 3 && act ==1))
                {
                   cout<<"Case #"<<cas<<": O won\n";  
                    return;           
                 }              
     }

   if(empty == 0) cout<<"Case #"<<cas<<": Draw\n";   
   else cout<<"Case #"<<cas<<": Game has not completed\n";   
     
}
int main()
{
          cin>>n;
          
          rep(ii,n)
          {
               read();
               empty=0;
               solve();
               cas++;
         }
                   
       //  getch();
          return 0;
}
