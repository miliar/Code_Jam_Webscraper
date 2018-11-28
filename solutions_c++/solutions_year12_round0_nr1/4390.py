#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;



int main()
{
    char a[27]="yhesocvxduiglbkrztnwjpfmaq";
     //freopen("input.txt","r",stdin);
     //freopen("output.in ","w",stdout);
     int t;
     cin>>t;

     getchar(); int j=1;
     while(t--)
     {
         char b[105];
         cin.getline (b,105,'\n');
         int l=strlen(b);
         for(int i=0;i<l;i++)
         {
             if(b[i]>='a'&&b[i]<='z')
             b[i]=a[b[i]-97];
         }
         cout<<"Case #"<<j<<": "<<b<<endl;j++;

     }
}
