#include<cstdio>
#include<algorithm>
#include<string>
#include<iostream>
using namespace std;
//char s[30]="abcdefghijklmnopqrstuvwxyz";
char s[30]="yhesocvxduiglbkrztnwjpfmaq";
string ss;
int main()
{
    freopen("AAA.in","r",stdin);
    freopen("BBB.txt","w",stdout);
    int t,l;
    char c;
    cin>>t;
    while((c=getchar())!=EOF&&c!='\n');
    for(int j=1;j<=t;j++)
    {
        cout<<"Case #"<<j<<": ";
        getline(cin,ss);
        l=ss.size();
        for(int i=0;i<l;i++)
        {
            if(ss[i]>='a'&&ss[i]<='z')
                cout<<s[ss[i]-'a'];
            else cout<<ss[i];
        }
        cout<<endl;
    }
    return 0;
}
