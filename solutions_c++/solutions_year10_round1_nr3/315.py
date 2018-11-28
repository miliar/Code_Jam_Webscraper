#include <cstdio>
#include <string>
using namespace std;

int main(){
  int T;
  scanf("%d",&T);
  
  string answers[] = {"Neither", "Blue", "Red", "Both"};
  
  
  for(int Case = 1;Case<=T; Case++){
    int A1, A2, B1, B2;
    scanf("%d%d%d%d",&A1,&A2,&B1,&B2);
    int res = 0;
    int T[100];
    for(int i = A1; i<=A2; i++)
      for(int j=B1; j<=B2; j++){
        int x = i;
        int y = j;
        if(x<y)
          swap(x,y);
        int k = 0;
        while(y>0){
          T[k++] = x/y;
          x%=y;
          swap(x,y);
        }
        if(T[0]>=2){
          res++;
          continue;
        }
        int flag = true;
        while(k--){        
          if(T[k]>=2)
            flag = true;
          else flag = !flag;                  
        }
        if(flag) res++;       
      }        
    printf("Case #%d: %d\n", Case, res);
  }    
}
