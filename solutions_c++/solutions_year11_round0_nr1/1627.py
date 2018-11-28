#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<algorithm>
using namespace std;
void solve(int test){
    int n;
    scanf("%d",&n);
    int ot=0,bt=0;
    char tmp[10];
    int nowo=1,nowb=1;
    for(int i=0;i<n;i++){
        int p;
        scanf("%s %d",tmp,&p);
        if(tmp[0]=='O'){
            ot+=abs(nowo-p)+1;
            nowo=p;
            if(ot<=bt)ot=bt+1;

        }
        else{
            bt+=abs(nowb-p)+1;
            nowb=p;
            if(bt<=ot)bt=ot+1;

        }
        //printf(" [%d]\n",max(ot,bt));
    }
    printf("Case #%d: %d\n",test,max(ot,bt));
}
int main(){
    freopen("A-large.in","r",stdin);
    //freopen("A-large.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++){
        //t--;
        solve(i);
    }
}
