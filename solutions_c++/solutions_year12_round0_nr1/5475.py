#include<iostream>
#include<stdio.h>
#include<cstring>
using namespace std;
int main()
{
    char googleres[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    char str[101];
    long long t,i,j;
    cin>>t;
    //cin.flush();
    cin.ignore();
    for(i=1;i<=t;i++)
    {
        cin.getline(str,101);
        cout<<"Case #"<<i<<": ";
        for(j=0;j<strlen(str);j++)
        {
            if(str[j]!=' ')
                cout<<googleres[str[j]-97];
            else cout<<" ";
        }
        cout<<endl;
    }
    return 0;
}
