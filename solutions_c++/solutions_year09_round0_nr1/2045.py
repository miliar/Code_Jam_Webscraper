#include<iostream>
#include<stdio.h>
using namespace std;
char str[6000][20]={0};
int main(void)
{
    FILE *fin=fopen("A-large.in","r");
    FILE *fout=fopen("A-large.out","w");
    int l,d,n,ok,num;
    char s[1500]={0};
    fscanf(fin,"%d%d%d",&l,&d,&n);
    for(int i=0;i<d;i++)
        fscanf(fin,"%s",str[i]);
    for(int i=1;i<=n;i++){
        fscanf(fin,"%s",s);
        num=0;
        for(int j=0;j<d;j++){
            ok=0;
            for(int k=0,kk=0;k<l;k++,kk++){
                if(s[kk]!='('){
                    if(s[kk]!=str[j][k]){
                        ok=-1;
                        break;
                    }    
                }    
                else{
                    for(kk++;s[kk]!=str[j][k]&&s[kk]!=')';kk++);
                    if(s[kk]==')'){
                        ok=-1;
                        break;
                    }    
                    for(kk++;s[kk]!=')';kk++);
                }    
            }    
            if(ok!=-1)
                num++;
        }   
        fprintf(fout,"Case #%d: %d\n",i,num);
    }    
    fclose(fin);
    fclose(fout);
    system("pause");
    return 0;
}    
