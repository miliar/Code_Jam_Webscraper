// CodeJam.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <math.h>
#include <map>

using namespace std;

int main()
{
  string line;
  fstream myfile ("A-small-attempt0.in");
  ofstream outFile;
  outFile.open("A-small.out");

  int cases;
  myfile>>cases;
  string dummy;
  getline(myfile,dummy);
  map<char,char> decipher;
  char googlecode[27] = { 'a','b','c','d','e','f','g','h','i','j','k','l','m',
                          'n','o','p','q','r','s','t','u','v','w','x','y','z',
                          ' ' };
  char alphabet[27] = { 'y','h','e','s','o','c','v','x','d','u','i','g','l',
                        'b','k','r','z','t','n','w','j','p','f','m','a','q',
                        ' ' };

  for (int i = 0; i < 27; ++i) {
    decipher[googlecode[i]] = alphabet[i];
  }
  for( int i = 0; i < cases; i++ )
  {
  outFile<<"Case #"<<i+1<<": ";
  cout<<"Case #"<<i+1<<": ";

  // Read input.
  string line;
  getline(myfile, line);

  for (int c = 0; c < line.size(); ++c) {
    // Write output.
    char out = decipher[line[c]];
    outFile<<out;
    cout<<out;
  }
  outFile<<endl;
  cout<<endl;
}

myfile.close();
outFile.close();
return 0;
}



