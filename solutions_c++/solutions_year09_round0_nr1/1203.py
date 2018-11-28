#include <cstdio>
#include <cstring>
using namespace std;

#define EXT 5
#define MAX_L 15
#define MAX_D 5000
#define MAX_N 500
#define NCHARS 26
#define MAX_PATLEN 512
//#define MAX_PATLEN ((26+2)*15)

int L;
int D;
int N;

char buff[MAX_PATLEN+EXT];
char dic[MAX_D+EXT][MAX_L+EXT];
bool mat[MAX_L+EXT][NCHARS+EXT];

void show_pattern(){
  //printf("pattern: ");
  for(int i = 0; i < L; i++){
    int count = 0;
    for(int k = 0; k < NCHARS; k++){
      if(mat[i][k]) count++;
    }
    if(count>1) putchar('(');
    for(int k = 0; k < NCHARS; k++){
      if(mat[i][k]) putchar('a'+k);
    }
    if(count>1) putchar(')');    
  }
  putchar('\n');
}

void update_pattern(char *str){
  memset(mat,false,sizeof(mat));
  //printf("%s\n",str);
  int k, p = 0;
  for(int i = 0; i < L; i++){
    if(str[p]=='('){
      p++;
      while(str[p]!=')'){
        k = str[p]-'a';
        mat[i][k] = true;
        p++;
      }
      p++;
    }else{   
      k = str[p]-'a';
      mat[i][k] = true;
      p++;
    }
  }
}

bool is_valid(int wind){
  for(int i = 0; i < L; i++){
    int k = dic[wind][i]-'a';
    if(!mat[i][k]) return false;
  }
  return true;
}

int main(){
  scanf("%d%d%d",&L,&D,&N);
  for(int i = 0; i < D; i++){
    scanf("%s",dic[i]);
  }
  for(int i = 0; i < N; i++){
    scanf("%s",buff);
    update_pattern(buff);
    //show_pattern();
    int count = 0;
    for(int k = 0; k < D; k++){
      if(is_valid(k)) count++;
    }
    printf("Case #%d: %d\n",i+1,count);
  }
  return 0;
}
