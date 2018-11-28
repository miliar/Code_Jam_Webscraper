#include <cstdio>
using namespace std;
int T,N;
int S,s;
char c;
int O[1050],B[1050],mem[1050];
int ret;
int o,b,mv;
int abs(int a){
  if(a>0)
  return a;
  return -a;
}
int mx(int a,int b){
    //if (a<0) a=-a;
    //if (b<0) b=-b;
    if (a>b)
    return b;
    return a;
}
int step(int src,int dst,int rg){
    if(dst==src) return src;
    if (dst>src)
    return mx(src+rg,dst);
    return -mx(-src+rg,-dst);
}
int main(){
    scanf("%d",&T);
    for(int t=0;t<T;t++){
        scanf("%d",&N);
        O[0]=1;B[0]=1;
        for(int i=0;i<N;i++){
          scanf(" %c %d",&c,&s);
          O[i+1]=O[i];
          B[i+1]=B[i];
          if (c=='O'){
            O[i+1]=s;
            s=-s;
          }else{
            B[i+1]=s;
          }
          mem[i]=s;

        }
        for(int i=N-1;i>=0;i--){
          O[i]=O[i+1];
          B[i]=B[i+1];
          if (mem[i]>0){
              B[i]=mem[i];
          }else{
              O[i]=-mem[i];
          }

        }
        o=1;
        b=1;
        ret=0;
        for(int i=0;i<=N;i++){
            if(mem[i]>0)
              mv=abs(B[i]-b);
            else mv=abs(O[i]-o);
            //printf("%d\n",mv);
            ret+=mv;
            o=step(o,O[i],mv+1);
            b=step(b,B[i],mv+1);
        }
        for(int i=0;i<N;i++)
        ;//printf("%d %d\n",O[i],B[i]);
        printf("Case #%d: %d\n",t+1,ret+N);
    }

}
