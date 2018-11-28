#include<iostream>
#include<string>
using namespace std;
const string s="welcome to code jam";
int ans[20],n;
char ch[600];
void work(){
     memset(ans,0,sizeof(ans));
     ans[0]=1;
     for (int i=0;i<strlen(ch);i++)
     for (int j=0;j<19;j++)
     if (ch[i]==s[j]) ans[j+1]=(ans[j]+ans[j+1])%10000;
}
int main(){
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    cin>>n;
    gets(ch);
    for (int l=0;l<n;l++){
        gets(ch);
        work();
        cout<<"Case #"<<l+1<<": ";
        if (ans[19]<1000) cout<<"0";
        if (ans[19]<100) cout<<"0";
        if (ans[19]<10) cout<<"0";
        cout<<ans[19]<<endl;
    }
    return 0;
}
