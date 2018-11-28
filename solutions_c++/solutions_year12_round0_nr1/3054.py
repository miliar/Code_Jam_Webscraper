#include <iostream>
#include <cstdio>
using namespace std;

const char dc[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    char p='a';
    char s[10000];
    int T;
    cin>>T;
    getchar();
    for (int k=1;k<=T;k++) {
        cout<<"Case #"<<k<<": ";
        gets(s);
        int n=strlen(s);
        for (int i=0; i<n; i++) {
            p = s[i];
            if (p>='a' && p<='z')
                cout<<dc[p-'a'];
            else cout<<p;
        }
        cout<<endl;
    }
    return 0;
}
