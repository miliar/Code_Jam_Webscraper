#include <stdio.h>
#include <string.h>
#include <stdint.h>
int ch[62];
bool check[62];
char line[64];
void clear(){
    int i;
    for(i=0;i<62;i++){
        check[i]=false;
        ch[i]=-1;
    }

}
int cToi(char c){
    int t=c-'0';
    if(t>=0 && t<=9)return t;
    else return c-'a'+10;
}
int main(){
    int i,t,l,j,k,count;
    int64_t fac,ans,num;
    char c;
    freopen("A-large.in","rt",stdin);
    freopen("A-large.out","wt",stdout);
    scanf("%d\n",&t);
    for(i=0;i<t;i++){
        clear();
        ans=0;
        scanf("%s",line);
        count=0;
        l=strlen(line);
        for(j=0;j<l;j++){
            k=cToi(line[j]);
            if(!check[k])count++;
            check[k]=true;
        }
        count;
        if(count==1)count=2;
        for(j=0,fac=1;j<l-1;j++)
            fac*=count;
        ch[cToi(line[0])]=1;
        num=0;
        ans=fac;

        for(j=1;j<l;j++){
            fac/=count;
            if(ch[cToi(line[j])]==-1){
                ch[cToi(line[j])]=num;
                if(num==0)num=2;
                else num++;
            }
            ans+=ch[cToi(line[j])]*fac;

        }
        printf("Case #%d: %I64d\n",i+1,ans);
    }
}

