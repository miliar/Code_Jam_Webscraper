#include <cstdio>
#include <cstring>
#include <map>
using namespace std;

int T,C=1;
char winner,board[8][8];
map<char,int> m;
int cnt[8];

char checkline(int i){
  memset(cnt,0,sizeof(cnt));
  for(int j=0;j<4;j++)
    cnt[m[board[i][j]]]++;
  if(cnt[m['X']]>0 and cnt[m['O']]==0 and cnt[m['.']]==0) return 'X';
  if(cnt[m['O']]>0 and cnt[m['X']]==0 and cnt[m['.']]==0) return 'O';
  return 0;
}

char checkcol(int j){
  memset(cnt,0,sizeof(cnt));
  for(int i=0;i<4;i++)
    cnt[m[board[i][j]]]++;
  if(cnt[m['X']]>0 and cnt[m['O']]==0 and cnt[m['.']]==0) return 'X';
  if(cnt[m['O']]>0 and cnt[m['X']]==0 and cnt[m['.']]==0) return 'O';
  return 0;
}

char checkdiags(){
  memset(cnt,0,sizeof(cnt));
  for(int i=0;i<4;i++)
    cnt[m[board[i][i]]]++;
  if(cnt[m['X']]>0 and cnt[m['O']]==0 and cnt[m['.']]==0) return 'X';
  if(cnt[m['O']]>0 and cnt[m['X']]==0 and cnt[m['.']]==0) return 'O';

  memset(cnt,0,sizeof(cnt));
  for(int i=0;i<4;i++)
    cnt[m[board[i][3-i]]]++;
  if(cnt[m['X']]>0 and cnt[m['O']]==0 and cnt[m['.']]==0) return 'X';
  if(cnt[m['O']]>0 and cnt[m['X']]==0 and cnt[m['.']]==0) return 'O';
  return 0;
}


int main(){

  m['.']=0;
  m['O']=1;
  m['X']=2;
  m['T']=3;
  scanf("%d",&T);
  while(T--){
    printf("Case #%d: ",C++);
    for(int i=0;i<4;i++)
      scanf("%s",board[i]);
    for(int i=0;i<4;i++){
      winner=checkline(i);
      if(winner!=0){
        printf("%c won\n",winner);
        goto fim;
      }
      winner=checkcol(i);
      if(winner!=0){
        printf("%c won\n",winner);
        goto fim;
      }
    }

    winner=checkdiags();
    if(winner!=0){
      printf("%c won\n",winner);
      goto fim;
    }

    // check if draw or not completed
    for(int i=0;i<4;i++)
      for(int j=0;j<4;j++)
        if(board[i][j]=='.'){
          printf("Game has not completed\n");
          goto fim;
        }
    printf("Draw\n");
    fim:;
  }

  return 0;
}
