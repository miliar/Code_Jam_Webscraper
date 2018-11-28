#include <stdio.h>
#include <string.h>
int app[100];
int happy(int n, int b){
    if (n<100) app[n]=1;
    int sum=0;
    int m=n;
    if (n==1) return 1;
    else{
         while (n){
               sum+=(n%b)*(n%b);
               n/=b;
         }
         if ((sum<100) && (app[sum])) return 0;
         
         return happy(sum,b);
    }
}
int main(){
    freopen("abig.in","r",stdin);
    freopen("a.out","w",stdout);
    int T,t,p,calc,k,i,j;
    char str[200];
    int data[100];
    scanf("%d ",&T);
    for (t=1;t<=T;t++){
        gets(str);
        p=0;
        calc=0;
        while (p<strlen(str)){
              data[++calc]=str[p++]-'0';
              while (str[p]>='0' && str[p]<='9'){
                    data[calc]=data[calc]*10+str[p]-'0';
                    p++;
              }
              p++;
        }
        k=1;
        while (1){
            k++;
            for (i=1;i<=calc;i++){
                memset(app,0,sizeof(app));
                if (!happy(k,data[i])) break;
            }
            if (i==(calc+1)) break;
        }
        printf("Case #%d: %d\n",t,k);
    }
    return 0;
}
    
    
