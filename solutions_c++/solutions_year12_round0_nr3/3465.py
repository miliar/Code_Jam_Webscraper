#include <cstdlib>
#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{    
    int t,tag[3001];
    int len,tmp,min,front,back,factor,max,sum;
    int a,b;
    int i,j;
    FILE *fp,*f;
    
    fp = fopen("D:\\C-small-attempt0.in","r");
    f = fopen("D:\\ans.txt","w");
    if(fp == NULL)printf("false");
    
    fscanf(fp,"%d",&t);
    
    for(i=1;i<=t;i++){
        fscanf(fp,"%d%d",&a,&b);
        
        for(j=1;j<=b;j++)tag[j] = 0;
        while(a<=b){
            len = 1;
            tmp = a;
            while(tmp/10){
                tmp/=10;
                len++;
            }
            
            max = 1;
            for(j=0;j<len;j++)max*=10;
            
            min = a;
            factor = 10;
            for(j=1;j<len;j++){
                front = a/factor;
                back = a%factor;
                
                if(back>=factor/10){
                    tmp = back*max/factor+front;
                    if(min>tmp)min = tmp;
                }
                factor*=10;
            }
            
            tag[min]++;
            a++;
        }
        sum = 0;
        for(j=1;j<=b;j++){
            if(tag[j]>1)sum+=tag[j]*(tag[j]-1)/2;
        }
        fprintf(f,"Case #%d: %d\n",i,sum);
    }
    
    fclose(fp);
    fclose(f);
    system("pause");
    return 0;
}
