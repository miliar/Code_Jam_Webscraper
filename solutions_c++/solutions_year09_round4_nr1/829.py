#include <stdio.h>
#define max 80
int n,a[max];
void getInput(){
    int c=0,i,j;
    char x;
    scanf("%d\n",&n);
    for(i=0;i<n;i++){
        c=0;
        for(j=0;j<n;j++){
            scanf("%c\n",&x);
            if(x=='1')c=j+1;
        }
        a[i]=c-1;
    }
}
void swap(int a[],int i,int j){
    int tmp = a[i];
    a[i]=a[j];
    a[j]=tmp;
}
void run(){
    int k,c=0,j,idx,min;
    for(int i=0;i<n;i++){
        if(a[i]>i){
            for(j=i+1;j<n;j++)
                if(a[j]<=i)break;
            for(;j>i;j--){
                swap(a,j,j-1);
                c++;
            }
        }
    }
    printf("%d\n",c);
}
int main(){
    freopen("A-large.in","rt",stdin);
    freopen("A-large.out","wt",stdout);
    int ntest;
    scanf("%d\n",&ntest);
    for(int test=0;test<ntest;test++){
        getInput();
        printf("Case #%d: ",test+1);
        run();
    }
}
