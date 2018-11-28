#include<iostream>
#include<cstdio>
#include<string>
using namespace std;
char s[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
int main()
{
    freopen("A-small-attempt8.in","r",stdin);
    freopen("A-small-attempt8.out","w",stdout);
    int t;
    int cnt=0;
    cin>>t;
    string str;
    getline(cin,str);
    while(t--)
    {
        getline(cin,str);
        int len=str.length();
        string ans;
        for(int i=0;i<len;++i)
        {
            if(str[i]==' ') ans+=' ';
            else
            ans+=s[str[i]-'a'];

        }
        //ans+='\0';
        cout<<"Case #"<<++cnt<<": "<<ans<<endl;
    }
    return 0;
}
