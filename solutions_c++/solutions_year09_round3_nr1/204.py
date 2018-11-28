/*
   NAME : Siwakorn Srisakaokul
   ID : ping128
   LANG : C++
   CONTEST : Google CodeJam -- Round 1C
   TASK : 
*/
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int T;
int a;
int num[100];
int have[100];
char in[100];
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int len,s=2,j;
    scanf("%d",&T);
    for(int t=0;t<T;t++){
        scanf("%s",in);
        len=strlen(in);
        
        for(int i=0;i<100;i++){ num[i]=0; have[i]=-1; }
        for(int i=0;i<len;i++){
            if(in[i]<='9' && in[i]>='0'){
                num[in[i]-'0']++;
            } else {
                num[in[i]-'a'+10]++;
            }
        }
        int ch=0;
        for(int i=0;i<40;i++) if(num[i]) ch++;
        if(in[0]<='9' && in[0]>='0'){
            have[in[0]-'0']=1;
        } else {
            have[in[0]-'a'+10]=1;
        }
        for(j=1;j<len;j++){
            if(in[j]<='9' && in[j]>='0'){
                if(have[in[j]-'0']==-1){
                    have[in[j]-'0']=0;
                    break;
                }
            } else {
                if(have[in[j]-'a'+10]==-1){
                    have[in[j]-'a'+10]=0;
                    break;
                }
            }
        }
        int sol=2;
        for(;j<len;j++){
          //  printf("** %d  %c %d",j,in[len-1],len);
            if(in[j]<='9' && in[j]>='0'){
                if(have[in[j]-'0']==-1){
                    have[in[j]-'0']=sol++;
                    
                }
            } else {
                if(have[in[j]-'a'+10]==-1){
                    have[in[j]-'a'+10]=sol++;
                    
                }
            }
        }
        if(ch==1) ch++;
        long long p=0,sss=1;
        for(int j=len-1;j>=0;j--){
            if(in[j]<='9' && in[j]>='0'){
                p+=have[in[j]-'0']*sss;
            } else {
                p+=have[in[j]-'a'+10]*sss;             
            }
            sss*=ch;
        }
        printf("Case #%d: %I64d\n",t+1,p);
    //    while(1);
    }
    //while(1);
return 0;
}
