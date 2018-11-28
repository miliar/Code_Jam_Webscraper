#include<iostream>
#include<cstring>
using namespace std;

char st[1000];
int v[1000],t,c;
__int64 ans,k;

void work(){
    cin>>st;
    //if (c==12) puts(st);
    memset(v,-1,sizeof(v));
    int i;
    int base=0;
    int len=strlen(st);
    v[int(st[0])]=1;
    
    for (i=0;i<len;i++)
        if (v[int(st[i])]==-1) 
        {v[int(st[i])]=base;if (base==0) base=2;else base++;}
    if (base<2) base=2;
    ans=0;k=1;
    for (i=len-1;i>=0;i--){
        ans+=v[int(st[i])]*k;
        if (i!=0) k=k*base;
    }
    cout<<"Case #"<<c<<": "<<ans<<endl;
}
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    cin>>t;
    for (c=1;c<=t;c++)
    work();
    return 0;
}

