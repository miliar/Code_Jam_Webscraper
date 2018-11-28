#include <cstdlib>
#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
    int t,s,p,n,d;
    int count;
    int i,j;
    int ban1,ban2;
    FILE *fp,*f;
    
    fp = fopen("D:\\B-large.in","r");
    f = fopen("D:\\ans.txt","w");
    if(fp == NULL)printf("false");
    
    fscanf(fp,"%d",&t);
    
    for(i=1;i<=t;i++){
        fscanf(fp,"%d%d%d",&s,&p,&n);
        ban1 = 3*n-2;
        ban2 = 3*n-4;
        count = 0;
        for(j=0;j<s;j++){
            fscanf(fp,"%d",&d);
            if(d>=n){
                if(d>=ban1)count++;
                else if(d>=ban2&&p){
                     count++;
                     p--;
                }
            }
        }
        fprintf(f,"Case #%d: %d\n",i,count);
    }
    
    fclose(fp);
    fclose(f);
    system("pause");
    return 0;
}
