#include <cstdlib>
#include <iostream>
#include <fstream>
using namespace std;

int test;
string s;  //abcdefghijklmnopqrstuvwxyz
string map= "yhesocvxduiglbkrztnwjpfmaq";


string solve (string s)
{
     string res="";
   for(int i=0;i<s.length();i++){
   if(!isalpha(s[i]))
   res+=s[i];        
   else
   res+=map[(int)s[i]-97];
   }   
   return res;
}

void input()
{
     
      ifstream cin("A-small.in");
      ofstream cout("A-small.out");
     
     
     cin>>test;
     getline(cin,s);
     for(int i=1;i<=test;i++){
        getline(cin,s);
      cout<<"Case #"<<i<<": "<<solve(s)<<endl;        
     }
      
      cin.close();
      cout.close();     
}


int main(int argc, char *argv[])
{    
    
     input();
     
    
    system("PAUSE");
    return EXIT_SUCCESS;
}
