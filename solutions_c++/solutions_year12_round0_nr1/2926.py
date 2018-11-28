#include<iostream>
#include<cstdio>
#include<string.h>
using namespace std;

  int main()
    {
         freopen("input.txt","r",stdin);
         freopen("output.txt","w",stdout);

         int tc=1,len,t;
         char gvall[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
         char gvalc[] = {'Y','H','E','S','O','C','V','X','D','U','I','G','L','B','K','R','Z','T','N','W','J','P','F','M','A','Q'};
         char str[200],buff[2];
         cin>>t;
         cin.getline(buff,2);

         for(;tc<=t;tc++)
          {
              cin.getline(str,200);
              //cout<<"\n"<<str;
              len = strlen(str);
                for(int i=0;i<len;i++)
                 {
                     if(str[i]==' ')
                      continue;
                     if(str[i]>92)
                       {str[i] = gvall[str[i]-97];
                        continue;
                       }                        
                       str[i] = gvalc[str[i]-65];
                       
                 }    
              cout<<"Case #"<<tc<<": "<<str<<"\n";              
          }   
                //system("PAUSE");
                return 0;
    }    

    
