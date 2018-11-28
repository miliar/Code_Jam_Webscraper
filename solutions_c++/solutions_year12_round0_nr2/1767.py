#include <cstdio>
#include <algorithm>
using namespace std;

int main(){
    int T;
    scanf("%d",&T);
    for(int i=0;i<T;i++){
        printf("Case #%d: ",i+1);
        int N,S,p;
        scanf("%d%d%d",&N,&S,&p);
        int t;
        int un=0,use=0;
        for(int j=0;j<N;j++){
            scanf("%d",&t);
            if(t%3==0){
                if(t/3>=p) un++;
                else if(t/3+1>=p&&t/3+1<=10&&t/3-1>=0) use++;
            }else if(t%3==1){
                if(t/3+1>=p&&t/3+1<=10) un++;
            }else{
                if(t/3+1>=p&&t/3+1<=10) un++;
                else if(t/3+2>=p&&t/3+2<=10) use++;
            }
        }
        printf("%d\n",un+min(use,S));
    }
}
