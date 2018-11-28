#include<iostream>
#include<cstring>

using namespace std;

string a="yhesocvxduiglbkrztnwjpfmaq";

int main()
{
      freopen("A1.in","r",stdin);
    freopen("GCJO1.txt","w",stdout);
    
    int t,i,x=0;
    cin>>t;
    char p[101];
    gets(p);
    while(t--)
    {
           char s[105];
           gets(s);
           
           
           for(i=0;i<strlen(s);i++)
           {
                   if(s[i]>='a' && s[i]<='z')
                   s[i]=a[s[i]-97];
           }
           cout<<"Case #"<<++x<<": "<<s<<endl;
    }
}                  
