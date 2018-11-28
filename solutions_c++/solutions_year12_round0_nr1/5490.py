#include <fstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <string.h>
using namespace std;
using std::cout;

using std::cin;
using std::endl;


int main() {
long int a=1,j;
  const char* filename = "A-small-attempt0.in";
  std::ifstream inFile(filename);
  std::ofstream outFile("Solution.txt");
  string s;
  char w;
  // Make sure the file stream is good
  if(!inFile) {
    cout << endl << "Failed to open file " << filename;
    system("PAUSE");
    return 1;
  }
  char map[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
  
  long n = 0;
  inFile>>n;
  
   inFile.ignore(100, '\n');
  string x="0";
  while(!inFile.eof()){
  outFile<<"Case #"<<a<<": ";a++;
  std::getline(inFile,s);
  
  s=s+x;
  
  for(j=0;s[j]!=0;j++){if(std::isalpha(s[j])){outFile<<map[s[j]-97];}else outFile<<" ";}
  outFile<<"\n";
  }

   system("PAUSE");
  
  
  return 0;
  
}
