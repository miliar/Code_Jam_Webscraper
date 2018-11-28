#include<cstdio>
#include<algorithm>

using namespace std;
int TC;
int N;int P;
int S;
int scores[110];
int main(){
    int i,j,k;
    int tc;
    int m=0;
    scanf("%d",&TC);
    for(tc=1;tc<=TC;tc++){
        m=0;
        scanf("%d%d%d",&N,&S,&P);
        for(i=0;i<N;i++){
            scanf("%d",&scores[i]);
        }
        int tmp;
        for(i=0;i<N;i++){
            if(scores[i]%3==0){
                tmp=scores[i]/3;
                if(tmp>=P)m++;
                else if(scores[i]>0&&S>0&&tmp==P-1){
                    m++;S--;
                }
            }
            else if(scores[i]%3==1){
                tmp=scores[i]/3+1;
                if(tmp>=P)m++;
            }
            else if(scores[i]%3==2){
                tmp=scores[i]/3+1;
                if(tmp>=P)m++;
                else if(S>0&&tmp==P-1){
                    m++;S--;
                }
            }
        }
        printf("Case #%d: %d\n",tc,m);

    }
    return 0;


}
