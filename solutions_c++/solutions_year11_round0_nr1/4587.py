#include<cstdio>
using namespace std;
int main(){
  int T,N,P,O,B,i,j,t;
  char C,llevo;
  freopen("A-large.in","r",stdin);
  freopen("output.out","w",stdout);
  scanf("%d",&T);
  t=T;
  while(T--){
    O=B=0;
    i=j=1;
    scanf("%d",&N);
    while(N--){
      scanf(" %c %d",&C,&P);
      if(C=='O'){
        O+=((P>i)? P-i:i-P)+1;
        i=P;
      }
      else{
        B+=((P>j)? P-j:j-P)+1;
        j=P;
      }
      if(C=='B'&&B<=O)
        B=(O==B)? B+1:O+1;
      else if(C=='O'&&O<=B)
        O=(O==B)? O+1:B+1;
    }
    if(C=='B')
      O=B;
    printf("Case #%d: %d\n",t-T,O);
  }
  return 0;
}
