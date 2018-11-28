#include <iostream>
#include <stdio.h>
#include<string.h>

using namespace std;
int main()
{
    char trans[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    char final[100];
    char init[100];
    int t,f=1;
    cin>>t;
    t++;
    while(t--)
    {
              cin.getline(init,101);
              for(int i=0;i<strlen(init);i++)
              {
                      if(init[i]==' ')
                                    final[i]=' ';
                      else
                          final[i]=trans[init[i]-97];
              }
              cout<<"Case #"<<f-1<<": ";
              for(int i=0;i<strlen(init);i++)
                      cout<<final[i];
              cout<<endl;
    f++;
    }
    return 0;
}
                          
                      
