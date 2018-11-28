#include <stdio.h>
#include <algorithm>
#include <string.h>
using namespace std;

int main(){
  int L, D, N;
  scanf("%d%d%d",&L,&D,&N);
  char s[D][L+1];
  bool table[L][26];
  char q[10000];
  for (int i=0;i<D;i++){
    scanf("%s",s[i]);
  }
  for (int ti=0;ti<N;ti++){
    scanf("%s",q);
    int n = strlen(q);
    //build table
    memset(table,0,sizeof(table));
    int pos=0;
    for (int i=0;i<n;i++){
      if (q[i]=='('){
        int j=i+1;
        while (q[j]!=')' && j<n){
          table[pos][q[j]-'a']=true;
          j++;
        }
        i=j;
      }else{
        table[pos][q[i]-'a'] = true;
      }
      //printf("~%d %d\n",i,pos);
      pos++;
    }
    //match
    int cnt=0;
    for (int i=0;i<D;i++){
      bool possible=true;
      for (int j=0;j<L && possible;j++){
        if (table[j][s[i][j]-'a']==false)possible=false;
      }
      if (possible)cnt++;
    }
    printf("Case #%d: %d\n",ti+1,cnt);
  }

  return 0;
}
