#include <iostream>
#include <string>
#include <stdio.h>
using namespace std;
int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    int n;
    char b[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    cin>>n;
    string str;
    getline(cin,str);
    for (int i=0;i<n;i++)
    {
        getline(cin,str);
        cout<<"Case #"<<i+1<<": ";
        for (int j=0;j<str.length();j++)
            if (str[j] == ' ') cout<<" ";
            else  cout<<b[ str[j]-'a' ];
        cout<<endl;
    }
    return 0;
}
