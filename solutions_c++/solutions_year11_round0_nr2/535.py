#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <stack>
#include <queue>
#include <vector>
#include <set>
#include <map>
#include <string>
#define N 30
  using namespace std;
  int comb[N][N],n;
  bool op[N][N];
  vector<int>stk;
  int c[N];
int main(){
  freopen("b.in","r",stdin);freopen("b.out","w",stdout);
  string str;
  int tc,tt;
  int i,j,k,x,y;
  bool flag;
  scanf("%d",&tc);
  for(tt=1;tt<=tc;tt++){
    printf("Case #%d: ",tt);
    memset(op,false,sizeof(op));
    memset(comb,255,sizeof(comb));
    cin>>n;    
    while(n--){
      cin>>str;
      comb[str[0]-'A'][str[1]-'A']=str[2]-'A';
      comb[str[1]-'A'][str[0]-'A']=str[2]-'A';
      }
    cin>>n;
    while(n--){
      cin>>str;
      op[str[0]-'A'][str[1]-'A']=true;
      op[str[1]-'A'][str[0]-'A']=true;
      }
    cin>>n;
    cin>>str;
    stk.clear();
    memset(c,0,sizeof(c));
    for(i=0;i<n;i++){
      x=str[i]-'A';
      //if(tt==3)printf("%d %c %c\n",stk.size(),x+'A',stk.back()+'A');
      if(stk.size()>0 && comb[stk.back()][x]>=0){
        y=stk.back();
        c[y]--;
        stk.pop_back();
        c[comb[y][x]]++;
        stk.push_back(comb[y][x]);
        }
      else{
        flag=false;
        for(y=0;y<26;y++)
          if(op[y][x] && c[y]>0){
            flag=true;
            break;
            }
        if(flag){
          stk.clear();
          memset(c,0,sizeof(c));
          }
        else{
          c[x]++;
          stk.push_back(x);
          }
        }
      }
    if(stk.size()==0)printf("[]\n");
    else{
      printf("[");
      for(i=0;i<stk.size()-1;i++)printf("%c, ",'A'+stk[i]);
      printf("%c]\n",'A'+stk.back());
      }
    }
  return 0;
}
    
      
    
    
