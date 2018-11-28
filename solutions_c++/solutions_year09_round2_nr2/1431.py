#include <stdio.h>
int num[22];
int cn[10];
void clear(){
    int i;
    for(i=0;i<10;i++)
        cn[i]=0;
}
int main(){
    int i,t,n,j,k,min;
    char c;
    freopen("B-small-attempt3.in","rt",stdin);
    freopen("B-small-attempt0.out","wt",stdout);
    scanf("%d\n",&t);
    for(i=0;i<t;i++){
        n=0;
        clear();
        while(1){
            scanf("%c",&c);
            if(c=='\n'||c==EOF)break;
            num[n++]=c-'0';
        }
        for(j=n-2;j>=0;j--)
            if(num[j]<num[j+1])break;
        printf("Case #%d: ",i+1);
        if(j==n-1){
            for(j=0;j<n;j++)
                cn[num[j]]++;
            for(j=1;j<10;j++)
                if(cn[j]-->0)printf("%d0",j);
            for(j=0;j<10;j++){
                while(cn[j]-->0){
                    printf("%d",j);
                }
            }
        }else{
            for(k=0;k<j;k++)
                printf("%d",num[k]);
            min=num[j+1];
            for(k=j+1;k<n;k++)
                if(num[k]>num[j] && num[k]<min)min=num[k];
            printf("%d",min);
            cn[min]--;
            for(;j<n;j++)
                cn[num[j]]++;
            for(j=0;j<10;j++){
                while(cn[j]-->0){
                    printf("%d",j);
                }
            }
        }
        printf("\n");


    }
}

