#include<iostream>
#include<cstdio>
using namespace std;

int main()
{
    char map[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

    int t;
    cin>>t;
    getchar();
    char s[1000];
    int caseno=0;

    while(t--)
    {
        caseno++;
        gets(s);
        int i=0;
        cout<<"Case #"<<caseno<<": ";
        while(s[i]!='\0')
        {
            if(s[i]>=97 && s[i]<=122)
            cout<<map[s[i]-'a'];
            else cout<<" ";
            i++;
        }
        cout<<endl;

    }
    return 0;


}
