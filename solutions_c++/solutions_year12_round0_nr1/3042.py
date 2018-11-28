#include <fstream>
#include<iostream>
#include<conio.h>
#include <strings.h>
using namespace std;
int main()
{
     int T,len;
     char str[102],ch;
     char alpha[26] ={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};//just for reference
     char result[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
     ifstream fi("qualify1.in");
     ofstream fo("qualify1.out");
     fi>>T;     
     cout<<T;
     fi.get(ch); //bring get pointer to next line
     for(int i=0;i<T;i++)
     {
          fi.getline(str,102,'\n');   
          len=strlen(str);
          fo<<"Case #"<<i+1<<": ";             
          for(int k=0;k<len;k++)
          {
               if(str[k]==' ') continue;   
               str[k]=result[str[k]-'a'];
          }
          fo<<str<<endl;     
     }
     cout<<"Completed";
     fi.close();
     fo.close();
     getch();
     return 0;     
}
