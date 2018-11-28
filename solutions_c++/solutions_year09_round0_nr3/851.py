#include<iostream>
#include<cstring>
using namespace std;

const int maxN=1000+5;
const string aim=" welcome to code jam";
char st[maxN];
int ans[20],t,zz,uu;

void init(){
    gets(st);
}
void work(){ 
    memset(ans,0,sizeof(ans));
    
    ans[0]=1;
    for (int i=0;i<strlen(st);i++)
        for (int j=1;j<=19;j++)
            if (st[i]==aim[j]) ans[j]=(ans[j-1]+ans[j])%10000;
}
void outans(){
    cout<<"Case #"<<t<<": ";
    if (ans[19]<1000) cout<<0;
    if (ans[19]<100) cout<<0;
    if (ans[19]<10) cout<<0;
    cout<<ans[19]<<endl;
}
int main(){
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    scanf("%d\n",&uu);
    t=1;
    while (t<=uu){
        init();
        work();
        outans();
        t++;
    }
    return 0;
    while (1>0){}
}
