#include<iostream>
#include<string>
#include <sstream>
#include<cctype>
#include<fstream>

using namespace std;
string translate(string input)
{
      
       string output;
       int i=0;
       output=input;
       while(input[i])
       {
                      
                      if(isalpha(input[i]))
                      {
                                          if(input[i]=='y')
                                          output[i]='a';
                                          if(input[i]=='n')
                                          output[i]='b';
                                          if(input[i]=='f')
                                          output[i]='c';
                                          if(input[i]=='i')
                                          output[i]='d';
                                          if(input[i]=='c')
                                          output[i]='e';
                                          if(input[i]=='w')
                                          output[i]='f';
                                          if(input[i]=='l')
                                          output[i]='g';
                                          if(input[i]=='b')
                                          output[i]='h';
                                          if(input[i]=='k')
                                          output[i]='i';
                                          if(input[i]=='u')
                                          output[i]='j';
                                          if(input[i]=='o')
                                          output[i]='k';
                                          if(input[i]=='m')
                                          output[i]='l';
                                          if(input[i]=='x')
                                          output[i]='m';
                                          if(input[i]=='s')
                                          output[i]='n';
                                          if(input[i]=='e')
                                          output[i]='o';
                                          if(input[i]=='v')
                                          output[i]='p';
                                          if(input[i]=='z')
                                          output[i]='q';
                                          if(input[i]=='p')
                                          output[i]='r';
                                          if(input[i]=='d')
                                          output[i]='s';
                                          if(input[i]=='r')
                                          output[i]='t';
                                          if(input[i]=='j')
                                          output[i]='u';
                                          if(input[i]=='g')
                                          output[i]='v';
                                          if(input[i]=='t')
                                          output[i]='w';
                                          if(input[i]=='h')
                                          output[i]='x';
                                          if(input[i]=='a')
                                          output[i]='y';
                                          if(input[i]=='q')
                                          output[i]='z';
                                         
                      }
                     
                     
                    
                           
                           i++;
                         
       }
      return(output);
    
       
      
}       
int main()
{
    fstream inf;
    fstream of;
    inf.open("input.txt",ios::in);
    of.open("output.txt",ios::out);
    string input;
    string output;
    char c;
    stringstream stream;
string id;
   
 int trials=0,i=1,j=0;
 getline(inf,id);
stream<<id;
stream>>trials;

 while(i<=trials)
 {
          
          getline(inf,input);
          of<<"Case #"<<i<<": ";
          output=translate(input);
          while(output[j])
          {
                          
                          of<<output[j];
                          j++;
          }
          
          
          of<<endl;
          
          i++;
          j=0;
 }   
 inf.close();
 of.close();
 return 0;  
}    
            
