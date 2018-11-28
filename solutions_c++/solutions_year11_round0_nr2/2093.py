#include <cstdio>
#include <algorithm>

using namespace std;

int main(){
    int ncas;
    scanf("%d",&ncas);
    for(int m=1;m<=ncas;m++){
        int c,d,n;
        char cs[100][4];
        char ds[100][4];
        char str[1001];
        scanf("%d",&c);
        for(int i=0;i<c;i++) scanf("%s",cs[i]);
        scanf("%d",&d);
        for(int i=0;i<d;i++) scanf("%s",ds[i]);
        scanf("%d",&n);
        scanf("%s",str);

        while(n>=2){
            int idx;
            int oidx;
            int mode;
            int lb,rb;
            for(oidx=1;oidx<n;oidx++){
                for(idx=0;idx<c;idx++){
                    if(str[oidx] == cs[idx][0] && str[oidx-1] == cs[idx][1] ||
                        str[oidx] == cs[idx][1] && str[oidx-1] == cs[idx][0] ){
//                        printf("jizz : %d\n",oidx);
                        break;
                    }
                }
                if(idx != c){
                    mode = 1;
                    break;
                }


                for(idx=0;idx<d;idx++){
                    mode = 0;
                    lb = -1;   

                        for(int i=0;i<=oidx;i++){
                            if(str[i] == ds[idx][1]){
                                lb = i;
//                                printf("%d\n",i);
                            }
                            if((lb != -1) && str[i] == ds[idx][0]){
 //                               printf("=%d\n",i);
                                mode = 2;
                                break;
                            }
                        }
                    if(mode == 2) break;

                    lb = -1;
                        for(int i=0;i<=oidx;i++){
                            if(str[i] == ds[idx][0]){
                                lb = i;
                            }else if(lb != -1 && str[i] == ds[idx][1]){
                                mode = 2;
                                break;
                            }
                        }
                    if(mode == 2) break;
                }
                if(idx != d){
                    mode = 2;
                    break;
                }                
            }

            if(oidx != n){
                if(mode == 1){
                    str[oidx-1] = cs[idx][2];
                    for(int i=oidx;i<n;i++){
                        str[i] = str[i+1];
                    }
                    oidx -= 2;
                    if(oidx<1) oidx = 1;
                    --n;
                }else if(mode == 2){
                    for(int i=0;i<n-oidx;i++){
                        str[i] = str[i+oidx+1];
                    }
                    n = n - oidx - 1;
                    oidx = 0;
   //                 printf("%s %d\n",str,oidx);
                }
            }else{
                break;
            }
        }

        
        printf("Case #%d: ",m);
        printf("[");
        for(int i=0;i<n;i++){
            printf("%c",str[i]);
            if(i!=n-1) printf(", ");
        }
        printf("]\n");
    }
    return 0;
}
