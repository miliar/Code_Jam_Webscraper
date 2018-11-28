using namespace std;
#include<iostream>
#include<string>
#include<string.h>
#include<stdio.h>
#include<stdlib.h>
int main()
{
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("A-small-attempt10.ans", "w", stdout);
   int test_case,case_no=0;
   cin>>test_case;
   char str1[]="yhesocvxduiglbkrztnwjpfmaq";
   char s1[1],s2[1];
   gets(s1);
   gets(s2);
   while(test_case--)
   {
       char str[10005];
       gets(str);
       cout<<"Case #"<<++case_no<<": ";
       for(int i=0;i<strlen(str);i++)
       {
           if(str[i]==' ')cout<<" ";
           else cout<<str1[str[i]-'a'];
       }
       cout<<endl;
   }
}
