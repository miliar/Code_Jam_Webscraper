/*
   NAME : Siwakorn Srisakaokul
   ID : ping128
   LANG : C++
   CONTEST :
   TASK :
*/
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<algorithm>
using namespace std;
char in[100],len1;
char s[100],n;
int cmp(const void *a,const void *b){
    return *(char*)a-*(char*)b;
}
int cmp1(const void *a,const void *b){
    return *(char*)b-*(char*)a;
}
int main(){
    
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    char swap;
    int T,i;
    scanf("%d",&T);
    for(int t=0;t<T;t++){
        scanf("%s",in);
        len1=strlen(in);
        for(i=len1-1;i>0;i--){
            if(in[i]<=in[i-1]) continue;
            else break;
        }
        if(i==0){
            in[len1]='0';
            len1++;
            in[len1]='\0';
            sort(in,in+len1);
            if(in[0]=='0'){
            for(int j=1;j<len1;j++){
                if(in[j]!='0'){
                    in[0]=in[j];
                    in[j]='0';
                    break;
                }
            }}
            printf("Case #%d: %s\n",t+1,in);
            
        }
        else {
            for(int j=i;j<len1;j++){
                if(in[i-1]<in[j] && in[i-1]>=in[j+1]){
                    swap=in[j];
                    in[j]=in[i-1];
                    in[i-1]=swap;
                    break;
                }
            }
            n=0;
            for(int j=i;j<len1;j++) s[n++]=in[j];
            s[n]='\0';
   //         printf("00 %s\n",s);
            qsort(s,n,sizeof s[0],cmp);
            in[i]='\0';
            printf("Case #%d: %s%s\n",t+1,in,s);
        }
    }
//while(1);
}
