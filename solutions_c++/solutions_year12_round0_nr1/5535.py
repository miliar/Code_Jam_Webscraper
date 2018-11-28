#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
    int t,i,j;
    freopen ("A-small-attempt0.in","r",stdin);
    freopen ("A-small-attempt0.out","w",stdout);
    cin>>t;
    char a;
    cin>>a;
    string s1="yhesocvxduiglbkrztnwjpfmaq";
    for(i=1;i<=t;i++)
    {
     char s[101];
     gets(s);
     cout<<"Case #"<<i<<": ";
     if(i==1)
     cout<<s1[a-97];
     for(j=0;j<strlen(s);j++)
     {
                              if(s[j]>=97 && s[j]<=122)
                              {
                                          cout<<s1[s[j]-97];
                              }
                              else if(s[j]==' ')
                              {
                                   cout<<" ";
                              }
                              else;
     }cout<<endl;
     }
     
     //system("pause");
     return 0;
}
     
