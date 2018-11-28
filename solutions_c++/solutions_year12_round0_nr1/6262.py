# include<iostream>
# include<string>
# include<cstdio>
using namespace std;
int main()
{
    int t,f=1;
    char b[27]="yhesocvxduiglbkrztnwjpfmaq";
    scanf("%d\n",&t);
    for(int i=0;i<t;i++)
    {
        string s;
        getline(cin,s);
        int l=s.length();
        for(int j=0;j<l;j++)
        {
           if(s[j]!=' ')
           {
               s[j]=b[s[j]-'a'];
           }
        }
        cout<<"Case #"<<f++<<": ";
        for(int i=0;i<l;i++)
        cout<<s[i];
        cout<<"\n";
    }
}
