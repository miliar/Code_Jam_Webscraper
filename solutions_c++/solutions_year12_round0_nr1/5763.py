#include <cstdlib>
#include <iostream>
#include <iostream>
#include <fstream>

using namespace std;

char line[1000];
char map[26] ={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};


int main(int argc, char *argv[])
{
    
    ifstream read;
    read.open("A-small-attempt0.in");
    ofstream write;
    write.open("output.txt");
    
    read.getline(line,1000);
    int T = atoi(line);
    
    int j=1;
    
    while(T--){
      write << "Case #"<<j++<<": ";
      read.getline(line,1000);
      cout << line;
      int i=0;
      while(line[i] != '\0'){
          if(line[i] == ' '){
            write << line[i];
          }
          else{
            write << map[line[i]-'a'];
          }
          i++;  
      }
      write << '\n';
    }
    write.flush();
}
