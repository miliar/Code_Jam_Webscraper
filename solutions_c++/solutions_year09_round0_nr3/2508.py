#include<stdio.h>
#include<string.h>
char m[]= "welcome to code jam";
char c[1000];
int count(int indexc,int indexm){
    int tmp = 0;
    if(indexm > strlen(m) || indexc > strlen(c)){
     //if(c[indexc] == m[indexm]) return 1;
     return 0;
     }    
    if(c[indexc] == m[indexm]){                     
        tmp += count(indexc+1,indexm+1);
        tmp += count(indexc+1,indexm);     
        if(indexm == strlen(m)-1) return tmp+1;   
    }else{        
        tmp += count(indexc+1,indexm);
    }
    return tmp;
}
int main(int argc,char **argv){
    int n,i,sum;
    scanf("%d\n",&n);
    for(i=0; i<n; i++){
        scanf("%[^\n]s",c);
        scanf("\n");
        //printf("%s\n",c);
        sum = count(0,0);
        sum %= 10000;
        if(sum < 10)
            printf("Case #%d: 000%d\n",i+1,sum);
        else if(sum < 100)
            printf("Case #%d: 00%d\n",i+1,sum);
        else if(sum < 1000)
            printf("Case #%d: 0%d\n",i+1,sum);
        else
            printf("Case #%d: %d\n",i+1,sum);
    }
    return 0;
}
