#include<iostream>
#include<fstream>
#include<string>

using namespace std;

string converter(string input);

int main()
{
int lines = 0;
int count_line = 0;
string input_string;

    ifstream in;
    ofstream out;
   
    in.open("A-small-attempt3.in");
    out.open("Output.txt");
   
    in>>lines;
    
    getline(in, input_string);
    
    if(1<=lines<=30)
    {
     for(int i=0;i<lines;i++)
     {
             getline(in, input_string); 
             
             cout<<input_string<<endl;
             if((input_string.length())<=100)
             {
              out<<"Case #"<<(i+1)<<": "<<(converter(input_string))<<endl;           
             }
     }
    }
    
    
return 0;
}
string converter(string input)
{

string converted_string = input;
char converted_alph = 0;
char outputc[27] ={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
char inputc[27]  ={'y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t','h','a','q'};



     for(int i=0;i<input.length();i++)
     {
      for(int j=0;j<27;j++)
      {
       if(input[i]==inputc[j])
       {
        converted_alph = outputc[j];
        break;
       }
       else
       {
        converted_alph = 32;
       }
      }
      converted_string[i] = converted_alph;
     }
     
return converted_string;
}
