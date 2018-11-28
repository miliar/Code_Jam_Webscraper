#include<iostream>
#include<cstdio>
#include<string>
//#include<conio.h>
using namespace std;
int main()
{
    char a[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    string s;
    int t,n,i,y,z=0;
    scanf("%d",&t);
    getchar();
    while(t--)
    {
              z++;
              getline(cin,s);
              n=s.length();
              for(i=0;i<n;i++)
              {
                              if(s[i]!=' ' && s[i]!='\0')
                              {
                                         y=s[i]-97;
                                         s[i]=a[y];
                              }
                              else if(s[i]==' ')
                              s[i]=' ';
              }
              cout<<"Case #"<<z<<": "<<s<<endl;
    }
    //getch();
    return 0;
}
                                         
                              
