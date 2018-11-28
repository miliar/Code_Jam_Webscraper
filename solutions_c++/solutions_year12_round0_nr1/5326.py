/******************************************************************************
Author: Jonathan Lam
Project Name: googlerese.cpp
Compiler: Dev C++
Due Date: 4/13/2012
******************************************************************************/
#include <iostream>
#include <cstdlib>
#include <string>
#include <fstream>

using namespace std;

int main()
{
    string junk = "abcdefghijklmnopqrstuvwxyz 1234567890",
           normal="yhesocvxduiglbkrztnwjpfmaq 1234567890",
           output = "";
    int counter = 1, num = 0;
    ifstream file;
    ofstream ofile;
    
    file.open("a.in");
    ofile.open("answer.in");    
    getline(file,output);   
    output = "";
    
    while (!file.eof())
    {        
          for (char temp = file.get(); temp != '\n' && !file.eof(); temp = file.get())
                output += normal[junk.find_first_of(temp)];
          if (file.eof())
             break;            
          ofile<<"Case #"<<counter<<": "<<output<<endl;
          output = "";       
          counter++;   
    }    
    file.close();
    ofile.close();
    system("pause");
    return 0;
}
