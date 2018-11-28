#include <string>    
#include <vector>    
# define loop(i, a, b) for(int i=a ; i<b ; ++i) 
using namespace std;    

int main(){
  int a[500][19];
  int n, res;
  freopen("C-large.in", "rt", stdin);
  freopen("C-small.out", "wt", stdout);
  scanf("%d\n",&n);
  char cj[]="welcome to code jam";
  loop(num,0,n){
    
    loop(q,0,500){
      loop(w,0,19){
        a[q][w]=0;}}
    char s[500];

    int t=0;
    //scanf("%c",&s);
    gets(s);
    int i=0,r1;
    while (s[i]){
      if (s[i]=='w'){
        a[i][0]=1;
      }
      if (s[i]!='w'){
        loop(j,1,19){
          if (s[i]==cj[j]){
            r1=0;
            loop(k,0,i){
              r1+=a[k][j-1];
              r1%=10000;
            }
            a[i][j]=r1;
          }
        }
      }
      ++i;
    }
    res=0;
    loop(k,0,i){
      res+=a[k][18];
      res%=10000;
    }
    printf("Case #%d: %04d\n",num+1,res);
  }
  fflush(stdout);
  return 0;
}