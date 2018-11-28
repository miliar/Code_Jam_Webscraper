#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int count;

void solve(int now,int a,int b){
    int x=0;
    int j=0;
    char buffer[10];
    char temp[10];
    itoa(now,buffer,10);
    int len=strlen(buffer);
    for(int i=1;i<len;i++){
        x=0;
        j=i;
        do{
            temp[x++]=buffer[j];
            j=(j+1)%len;
        }while(j!=i);
        int tc=atoi(temp);
        if(tc<=b&&tc>now) {
            count++;
            //printf("%d : %d-%d\n",count,now,tc);
        }
    }
}

int main(){
    FILE* in;
    FILE* out;
    in=fopen("d:/input.in","r");
    out=fopen("d:/output.out","w");
    int n,a,b,digit;
    fscanf(in,"%d",&n);
    for(int i=1;i<=n;i++){
        fprintf(out,"Case #%d: ",i);
        count=0;
        fscanf(in,"%d %d",&a,&b);
        for(int now=a;now<=b;now++){
            solve(now,a,b);
        }
        fprintf(out,"%d\n",count);
    }
    
    //system("pause");   
}
