#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;
char a[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l',
            'b','k','r','z','t','n','w','j','p','f','m','a','q'};

int main()
{
    freopen("result.out","w",stdout);
    freopen("aa.in","r",stdin);
    int T;
    cin>>T;
    cin.get();
    for (int n=1; n<=T; n++)
    {
        char st[300];
        cin.getline(st,200);
        cout<<"Case #"<<n<<": ";
        for (int i=0; i<strlen(st); i++)
            if ((st[i]>='a') && (st[i]<='z')) cout<<a[st[i]-'a'];
            else cout<<st[i];
        cout<<endl;
    }
}
