#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <iomanip>
#include <cmath>
using namespace std;

void replaceline(string &line);
void replace(char &letter);

int main(){
    ifstream patternfile("A-small-attempt0.in");
    ofstream myfile("result.txt");
    string line;
    int T;
    int casenumber= 0;
    
    getline(patternfile,line);
    T=atoi(line.c_str());
    

    do{
         getline(patternfile,line);
         casenumber++;   
         replaceline(line); 
         if(line.length()!=0){ 
         myfile<<"Case #"<<casenumber<<": "<<line<<endl;
         }                    
    }while(!patternfile.eof());
    patternfile.close();
    myfile.close();
system("pause");

}

void replaceline(string &line){
     for(int i=0;i<line.length(); ++i){
          replace(line[i]);
          cout<<line[i];   
      }
}
void replace(char &letter){
     switch(letter){
      case 'a':
           letter='y';
           break;
      case 'b':
           letter='h';
           break;
      case 'c':
           letter='e';
           break;
      case 'd':
           letter='s';
           break;
      case 'e':
           letter='o';
           break;
      case 'f':
           letter='c';
           break;
      case 'g':
           letter='v';
           break;
      case 'h':
           letter='x';
           break;
      case 'i':
           letter='d';
           break;
      case 'j':
           letter='u';
           break;
      case 'k':
           letter='i';
           break;
      case 'l':
           letter='g';
           break;
      case 'm':
           letter='l';
           break;
      case 'n':
           letter='b';
           break;
      case 'o':
           letter='k';
           break;
      case 'p':
           letter='r';
           break;
      case 'q':
           letter='z';
           break;
      case 'r':
           letter='t';
           break;
      case 's':
           letter='n';
           break;
      case 't':
           letter='w';
           break;
      case 'u':
           letter='j';
           break;
      case 'v':
           letter='p';
           break;
      case 'w':
           letter='f';
           break;
      case 'x':
           letter='m';
           break;
      case 'y':
           letter='a';
           break;
      case 'z':
           letter='q';
           break;
      default:
              break;
      }
      
}



