#include<cstdio>
#include<cstring>
#include<map>

using namespace std;

int main(){
    int lines;
    scanf("%d",&lines);
    for(int i=0;i<lines;i++){
        int N,S,p,out=0;
        scanf("%d%d%d",&N,&S,&p);
        int t[N];
        for(int j=0;j<N;j++){
            scanf("%d",t+j);
            //printf("%d",t[j]);
            if(t[j]%3==0){
                if(t[j]/3>=p){
                    out++;
                }
                else if(t[j]/3+1>=p && S>0 && t[j]/3>1){
                    out++;
                    S--;
                }
            }
            else if((t[j]+1)%3==0){
                if((t[j]+1)/3>=p)
                    out++;
                else if((t[j]+1)/3+1>=p&&S>0){
                    out++;
                    S--;
                }
            }
            else if((t[j]-1)%3==0){
                if(((t[j]-1)/3)+1>=p)
                    out++;
            }
        }
        printf("Case #%d: %d\n",i+1,out);
    }
    return 0;
}