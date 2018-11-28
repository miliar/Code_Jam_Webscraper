#include<cstdio>

int main(){
    int CaseNum,CN,n,k;
    scanf("%d",&CaseNum);
    for (CN=1;CN<=CaseNum;++CN){
        scanf("%d%d",&k,&n);
        bool all=true;
        while (k--){
            if (n%2==0){
                all=false;
                break;
            }
            n/=2;
        }
        printf("Case #%d: ",CN);
        if (all)
            printf("ON\n");
        else
            printf("OFF\n");
    }
    return 0;
}
