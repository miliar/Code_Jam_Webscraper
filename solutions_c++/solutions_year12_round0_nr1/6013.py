#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <map>
using namespace std;

void translate(string temp, ofstream& res_str, map < char, char > trans){
  for(int i = 0; i < temp.length(); i++){
    if(temp[i] == ' '){
      res_str << ' ';
      i++;
    }
    res_str << trans[temp[i]];
  }
}

int main()
{
  //reading from a file
  std::ifstream in_str("A-small-attempt0.in");
  if ( !in_str )
    {
      std::cerr << "Can't open the query file " << '\n';
      return 1;
    }
  //outputing the file
  std::ofstream res_str("stdout");
  if ( !res_str )
    {
      std::cerr << "Can't open the result file " << '\n';
      return 1;
    }
  string abc = "abcdefghijklmnopqrstuvwxyz";
  string goo = "yhesocvxduiglbkrztnwjpfmaq";
  map< char, char > trans;
  for(int i = 0; i < abc.length(); ++i){
    trans[abc[i]]=goo[i];
  }
  string temp;
  int foo;
  in_str >> foo;
  getline(in_str, temp);//too get ride of firs \n
  for(int i = 0; i < foo; i++){
    res_str << "Case #" << i+1 << ": ";
    getline(in_str, temp);
    translate(temp, res_str, trans);
    res_str << endl;
  }
  return 0;
}