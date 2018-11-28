#include <cstdlib>
#include <iostream>
#include <fstream>
#include<conio.h>
#include <string>
using namespace std;

int main(int argc, char *argv[])
{
    using std::string;
   using std::cout;
   using std::endl;
   using std::replace;
   
    ifstream  in(argv[1],ios::in| ios::binary);
    ifstream file(argv[1],ios::in| ios::binary);
    if(!in)
	     {
		 cout<<"cannot open file";
	     return 1;
         }
    ofstream  out(argv[2],ios::out| ios::binary);
    int t;
    in>>t;
    int cases=0;
    string str;
    getline(in, str ); ////appended for newline
    while(cases<t)
          {      
                  getline(in, str );
                  //cout<<str;
                  for (int i = 0; i < str.length(); i++) 
                  {
                    if (str[i] == 'y')str[i] = 'a'; else
                    if (str[i] == 'n')str[i] = 'b'; else
                    if (str[i] == 'f')str[i] = 'c'; else
                    if (str[i] == 'i')str[i] = 'd'; else
                    if (str[i] == 'c')str[i] = 'e'; else
                    if (str[i] == 'w')str[i] = 'f'; else
                    if (str[i] == 'l')str[i] = 'g'; else
                    if (str[i] == 'b')str[i] = 'h'; else
                    if (str[i] == 'k')str[i] = 'i'; else
                    if (str[i] == 'u')str[i] = 'j'; else
                    if (str[i] == 'o')str[i] = 'k'; else
                    if (str[i] == 'm')str[i] = 'l'; else
                    if (str[i] == 'x')str[i] = 'm'; else
                    if (str[i] == 's')str[i] = 'n'; else
                    if (str[i] == 'e')str[i] = 'o'; else
                    if (str[i] == 'v')str[i] = 'p'; else
                    if (str[i] == 'z')str[i] = 'q'; else
                    if (str[i] == 'p')str[i] = 'r'; else
                    if (str[i] == 'd')str[i] = 's'; else
                    if (str[i] == 'r')str[i] = 't'; else
                    if (str[i] == 'j')str[i] = 'u'; else
                    if (str[i] == 'g')str[i] = 'v'; else
                    if (str[i] == 't')str[i] = 'w'; else
                    if (str[i] == 'h')str[i] = 'x'; else
                    if (str[i] == 'a')str[i] = 'y'; else
                    if (str[i] == 'q')str[i] = 'z';
                    
                  }
                  cases++;
                  out<<"Case #"<<cases<<": "<<str<<endl;
                  
          }

    
    return 1;
    
}
