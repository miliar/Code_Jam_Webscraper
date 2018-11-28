#include<stdio.h>
int main(){
    int C,c,d,n,S,Case=1;
    char cc[40][4],dd[30][3],stack[101],input[101];
    scanf("%d",&C);
    while(C--){
        scanf("%d",&c);
        for(int i=0;i<c;i++)
            scanf("%s",cc[i]);
        scanf("%d",&d);
        for(int i=0;i<d;i++)
            scanf("%s",dd[i]);
        scanf("%d%s",&n,input);
        S=0;
        for(int i=0;i<n;i++){
            int ok=0;
            for(int j=0;j<c;j++)
                if(S>0){
                    if(cc[j][0]==input[i]&&stack[S-1]==cc[j][1]){
                        stack[S-1]=cc[j][2],ok=1;
                        break;
                    }else if(cc[j][1]==input[i]&&stack[S-1]==cc[j][0]){
                        stack[S-1]=cc[j][2],ok=1;
                        break;
                    }
                }
            if(ok==0){
                for(int j=0;j<d;j++)
                    if(S>0){
                        char temp;
                        if(dd[j][0]==input[i])
                            temp=dd[j][1];
                        else if(dd[j][1]==input[i])
                            temp=dd[j][0];
                        else continue;
                        for(int k=0;k<S;k++)
                            if(stack[k]==temp)
                                S=0,ok=1;
                    }
            }
            if(ok==0)
                stack[S++]=input[i];
        }
        printf("Case #%d: [",Case++);
        for(int i=0;i<S;i++)
            if(i==0)
                printf("%c",stack[i]);
            else printf(", %c",stack[i]);
        puts("]");
    }
}
