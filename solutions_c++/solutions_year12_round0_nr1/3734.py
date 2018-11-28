#include<iostream>
#include<string>

using namespace std;

int main()
      {
          char key[]={"yhesocvxduiglbkrztnwjpfmaq"};
          int T;
          cin>>T;
          cin.ignore();
          int CASE=1;
          int i=0;
          string G;
          char c;
          //getline(cin,G);
          while(T--)
          {
                   getline(cin,G);
                   cout<<"Case #"<<CASE<<": ";
                   CASE++;
                   for(i=0;i<G.length();i++)
                   {
                         c=(G[i]>='a')?key[G[i]-'a']:' ';
                         cout<<c;
                   
                   } 
                   cout<<endl;
                    }
          
      return 0;
      }
//yhesobvxduiglckrztnwjpfmaq
//abcdefghijklmnopqrstuvwxyz
