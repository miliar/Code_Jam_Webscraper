#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
char a[27]="yhesocvxduiglbkrztnwjpfmaq";
int main()
{
    int t,i,j;
    char g[101];
    freopen("A-small-attempt7.in","r",stdin);
    freopen("A-small-attempt7.out","w",stdout);
    cin>>t;
    getchar();
    for (i=1;i<=t;i++)
    {
        gets(g);
        cout<<"Case #"<<i<<": ";
        for (j=0;j<strlen(g);j++)
            if (islower(g[j])) cout<<a[g[j]-'a'];
            else cout<<g[j];
        cout<<endl;
    }
    return 0;
}
