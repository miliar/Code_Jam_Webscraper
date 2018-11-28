#include<stdio.h>
#include<string.h>
const int size = 20;
const int size2 = 5500;
const int size3 = 550;

char w[size2][size];
char ne[28*15+10];

bool ce(int x){
    int len = strlen(w[x]);
    int i = 0;
    int key = 0;
    for(int k = 0 ; k <strlen(ne) ; k++){
        if(ne[k] == '('){
                int key2 = 0;
                int now;
                for(now = k+1 ;;now++){
                    if(ne[now]==')' ){
                        break;
                    }
                    else{
                        if(ne[now] == w[x][i] && key2 == 0){
                            i++;
                       //     printf(" now: %d\n",now);
                            key2 = 1;
                        }
                    }
                }
                k = now;
                if(key2 == 0){
                    key =1;
                 //   printf("why? %d\n",i+1);
                    break;
                }
        }
        else{
            if(ne[k] == w[x][i]){
                i++;
            //    printf(" now: %d\n",k);
            }
            else{
                key = 1;
                break;
            }
        }
    }
    if(i!= len) key = 1;
    if(key) return false;
    else return true;
}

int main(){
    freopen("large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int l,d,n;
    while(scanf("%d%d%d",&l,&d,&n)!=EOF){
        for(int i = 1 ; i <= d ;i++ ){
            scanf("%s",w[i]);
        }
        int _case = 1;
        for(int i = 1 ; i <= n ; i++ ){
            scanf("%s",ne);
            printf("Case #%d: ",_case++);
            int num = 0;
            for(int j = 1 ; j<=d ; j++){
           //     printf("   %d %d\n",j,ce(j));
                if(ce(j)) num++;
            }
            printf("%d\n",num);
        }
    }
    return 0;
}
