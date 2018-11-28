#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<iostream>
#include<algorithm>
using namespace std;
string str="yhesocvxduiglbkrztnwjpfmaq";
string s;
int main()
{
    //freopen("A-small-attempt1.in","r",stdin);
    //freopen("A-small-attempt1.out","w",stdout);
    int T;
    cin>>T;
    cin.get();
    for(int i=1;i<=T;i++)
    {
        getline(cin,s);
        int len=s.size();
        cout<<"Case #"<<i<<": ";
        for(int i=0;i<len;i++)
        {
            if(s[i]!=' ')
            cout<<str[(int)s[i]-'a'];
            else cout<<' ';
        }
        cout<<endl;
    }
    return 0;
}
