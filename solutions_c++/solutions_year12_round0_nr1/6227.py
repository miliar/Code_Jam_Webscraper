#include<iostream>
#include<fstream>
#include<string>

using namespace std;

int size;
string input;
string extract;

string convert(string get_input)
{
    for(int i = 0;i < get_input.length(); i++)
        {

            switch(get_input[i])
              {
                       case 'y':
                       get_input[i] = 'a'; break;
                       case 'n':
                       get_input[i] = 'b'; break;
                       case 'f':
                       get_input[i] = 'c'; break;
                       case 'i':
                       get_input[i] = 'd'; break;
                       case 'c':
                       get_input[i] = 'e'; break;
                       case 'w':
                       get_input[i] = 'f'; break;
                       case 'l':
                       get_input[i] = 'g'; break;
                       case 'b':
                       get_input[i] = 'h'; break;
                       case 'k':
                       get_input[i] = 'i'; break;
                       case 'u':
                       get_input[i] = 'j'; break;
                       case 'o':
                       get_input[i] = 'k'; break;
                       case 'm':
                       get_input[i] = 'l'; break;
                       case 'x':
                       get_input[i] = 'm'; break;
                       case 's':
                       get_input[i] = 'n'; break;
                       case 'e':
                       get_input[i] = 'o'; break;
                       case 'v':
                       get_input[i] = 'p'; break;
                       case 'z':
                       get_input[i] = 'q'; break;
                       case 'p':
                       get_input[i] = 'r'; break;
                       case 'd':
                       get_input[i] = 's'; break;
                       case 'r':
                       get_input[i] = 't'; break;
                       case 'j':
                       get_input[i] = 'u'; break;
                       case 'g':
                       get_input[i] = 'v'; break;
                       case 't':
                       get_input[i] = 'w'; break;
                       case 'h':
                       get_input[i] = 'x'; break;
                       case 'a':
                       get_input[i] = 'y'; break;
                       case 'q':
                       get_input[i] = 'z'; break;
              }

        }

        return get_input;
    }

int main(int argc , char**argv)
{
    const char * input_file = argv[1];
    const char * output_file = argv[2];
    ifstream fileIn(input_file);//input file
    ofstream fileOut(output_file);//outputfile
    while(getline(fileIn,input))
    {
      extract = convert(input);

      if(size > 0)
        fileOut<<"Case #"<<size<<": "<< extract << " "<<endl;

      size++;
    }

}
