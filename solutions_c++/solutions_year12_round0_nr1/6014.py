#include <iostream>
#include <string>
#include <string.h>
using namespace std;
int main()
{
    int i,j,t;
    char s[201],*g="yhesocvxduiglbkrztnwjpfmaq";
    cin>>t;
    cin.getline(s,100);
    for (i=1;i<=t;i++)
    {
        cin.getline(s,120);
        for (j=0;j<strlen(s);j++)
        {
            if (s[j]>='a'&&s[j]<='z') s[j]=g[s[j]-'a'];
        }
        cout<<"Case #"<<i<<": "<<s<<endl;
    }
}
