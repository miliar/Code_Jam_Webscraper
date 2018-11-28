#include <cstdlib>
#include <iostream>
#include <string>

using namespace std;

char checkChar (char& letter){
  switch (letter){
  case 'a':
    return 'y';
  case 'b':
    return 'h';
  case 'c':
    return 'e';
  case 'd':
    return 's';
  case 'e':
    return 'o';
  case 'f':
    return 'c';
  case 'g':
    return 'v';
  case 'h':
    return 'x';
  case 'i':
    return 'd';
  case 'j':
    return 'u';
  case 'k':
    return 'i';
  case 'l':
    return 'g';
  case 'm':
    return 'l';
  case 'n':
    return 'b';
  case 'o':
    return 'k';
  case 'p':
    return 'r';
  case 'q':
    return 'z';
  case 'r':
    return 't';
  case 's':
    return 'n';
  case 't':
    return 'w';
  case 'u':
    return 'j';
  case 'v':
    return 'p';
  case 'w':
    return 'f';
  case 'x':
    return 'm';
  case 'y':
    return 'a';
  case 'z':
    return 'q';
  default:
    break;

  }
}


int main(int argc, char *argv[])
{
    int row;
  int lng;
  string line;
  getline(cin,line);
  row = atoi(line.c_str());
  int all = row;
  
  while (row!=0){
        string word;
    getline(cin,word);
    lng = word.size();
    string translate ="";
    for (int i=0;i<lng;i++){
            if (word[i]!=' '){
               translate = translate +checkChar(word[i]);
               }
            else{
                translate = translate +" ";
                }
    }
    row=row-1;
    cout <<"Case #"<<all-row<<": "<<translate <<"\n";
  }
    return EXIT_SUCCESS;
} 
