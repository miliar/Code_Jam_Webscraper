#include <cstdio>
#include <cstring>

using namespace std;

int t,n,s,p,teste;

int main(void){

    freopen("B.in","r",stdin);

    freopen("B.out","w",stdout);

    scanf("%d",&teste);

    for(int caso=1;caso<=teste;caso++){
        printf("Case #%d: ",caso);

        scanf("%d %d %d",&n,&s,&p);

        int total=0;

        for(int i=0;i<n;i++){
            scanf("%d",&t);

            if(t == 0){
                if(p == 0){
                    total++;
                }
                continue;
            }

            int a=t/3;

            if(t%3 == 0){

                if(a>=p){
                    total++;
                }else{
                    if(!s) continue;
                    if(a+1 == p){
                        s--;
                        total++;
                    }

                }

            }else if(t%3 == 1){

                if(a+1>=p){
                    total++;
                }

            }else{

                if(a+1>=p){
                    total++;
                }
                else{
                    if(!s) continue;
                    if(a+2 == p){
                        s--;
                        total++;
                    }
                }

            }


        }

        printf("%d\n",total);

    }

    return 0;
}
