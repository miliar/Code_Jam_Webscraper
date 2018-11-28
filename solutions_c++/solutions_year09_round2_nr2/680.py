#include <cstdio>
#include <algorithm>
using namespace std;
int main(){
  int T;
  scanf("%d", &T);
  getchar();
  for(int i=1; i<=T; i++){
    int Tab[50];
    for(int j=0; j<50; j++)
      Tab[j]=0;
    int j=1;
    char t = getchar();
    while(t>='0' && t<='9'){
      Tab[j++]=t-'0';
      t=getchar();
    }
    next_permutation(Tab, Tab+j);
    printf("Case #%d: ", i);
    if(Tab[0]==0){
      for(int y=1; y<j; y++)
	printf("%d", Tab[y]);
    }else{
      for(int y=0; y<j; y++)
	printf("%d", Tab[y]);
    }
    printf("\n");
  }
  return 0;
}
