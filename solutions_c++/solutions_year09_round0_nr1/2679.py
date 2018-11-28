#include <string>    
#include <vector>    
# define loop(i, a, b) for(int i=a ; i<b ; ++i) 
using namespace std;    

int res=0;
int l,d,n;
char q[100][100];
int e[100];
char a[100][100];
int pd[5000];
int last;

int pereb2(int j){
  if (j==l){
    res+=last;
    return 0;
  }
  loop(i,0,d){
    if (pd[i]){
      int ee=0;
      loop(k,0,e[j]) {if (a[i][j]==q[j][k]){++ee;}}
      if (!ee) {pd[i]=0; --last;}
    }
  }
  if (last>0) pereb2(j+1);
  return 0;
}

int main(){
  freopen("A-small-attempt1.in", "rt", stdin);
  freopen("A-small.out", "wt", stdout);

  scanf("%d %d %d/n",&l,&d,&n);

  loop(i,0,d){
    scanf("%s",&a[i]);
  }

  char str[100];
  loop(m,0,n){
    scanf("%s",&str);
    loop(h,0,100) {e[h]=0;}
    int w=0;
    int j=0;
    int i=0;
    while (str[i]) {
      switch (str[i]) {
        case '(':
          w=1;
          break;
        case ')':
          ++j;
          w=0;
          break;
        default :
          if (w==0) {
            e[j]=1;
            q[j][0]= str[i];
            ++j;
          }
          if (w==1) {
            q[j][ e[j] ]=str[i]; 
            ++e[j];
          }
      }
      ++i;
    }
    res=0;
    loop(hh,0,d){pd[hh]=1;}
    last=d;
    pereb2(0);
    printf("Case #%d: %d\n",m+1,res);
    fflush(stdout);
  }
  
  return 0;
}