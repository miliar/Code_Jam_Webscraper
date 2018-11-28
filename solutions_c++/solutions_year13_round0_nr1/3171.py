#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include<cstring>
using namespace std;
#define REP(i,n) for(int (i)=0;(i)<(n);(i)++)
#define FOR(i,a,b) for(int (i)=a;(i)<(b);(i)++)
#define INF 2000000000
#define INFLL (1LL<<62)
#define SS ({int x;scanf("%d", &x);x;})
#define SSL ({LL x;scanf("%lld", &x);x;})
#define _mp make_pair
#define MOD 1000000007
#define MAXN 200020
bool winCheck(char ch,vector<string>v ){

  int countD1=0,countD2=0;
  for(int i=0;i<4;i++){
     //Checking row wise
     if((v[i][0]==ch||v[i][0]=='T') && (v[i][1]==ch||v[i][1]=='T') && (v[i][2]==ch||v[i][2]=='T') && (v[i][3]==ch||v[i][3]=='T'))
         return true;
     //Checking column wise
     if((v[0][i]==ch||v[0][i]=='T') && (v[1][i]==ch||v[1][i]=='T') && (v[2][i]==ch||v[2][i]=='T') && (v[3][i]==ch||v[3][i]=='T'))
         return true;
     if(v[i][i]==ch || v[i][i]=='T'){
         countD1++;
     }
     if(v[i][3-i]==ch || v[i][3-i]=='T'){
        countD2++;
     }
  }
  if(countD1==4 || countD2==4 )
   return true;
  return false;
}


int main()
{
  //freopen("A.in","r",stdin);
  //freopen("out.txt","w",stdout);
  vector<string>v(4);
  int T,number=0;
  cin>>T;
  while(T--){
       number++;
       for(int i=0;i<4;i++)
         cin>>v[i];
       cout<<"Case #"<<number<<": ";
       if(winCheck('X',v)){
              cout<<"X won"<<endl;
       }else if(winCheck('O',v)){
              cout<<"O won"<<endl;
       }else{
              bool full=true;
              for(int i=0;i<4;i++)
                for(int j=0;j<4;j++)
                  if(v[i][j]=='.'){
                     full=false;
                     break;
                  }
              if(full){
                 cout<<"Draw"<<endl;
              }else{
                 cout<<"Game has not completed"<<endl;
              }
       }
  }

  return 0;
}
