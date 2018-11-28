// Created on Apr 13, 2012 7:49:21 PM

#include <iostream>
# include <map>
# include <fstream>
# include <string>
# include <sstream>
# include <vector>

using namespace std;

string getNextLine(string filename) {
  
}

int getNumofCases(ifstream &input){
  int num; string line;
  getline(input,line);
  stringstream convert(line);
  convert >> num;
  return num;
}

void initMap (map<char,char> &myMap){
  
  myMap.insert( pair<char,char>( 	'y' , 'a' ) );
  myMap.insert( pair<char,char>( 	'n' , 'b' ) );
  myMap.insert( pair<char,char>( 	'f' , 'c' ) );
  myMap.insert( pair<char,char>( 	'i' , 'd' ) );
  myMap.insert( pair<char,char>( 	'c' , 'e' ) );
  myMap.insert( pair<char,char>( 	'w' , 'f' ) );
  myMap.insert( pair<char,char>( 	'l' , 'g' ) );
  myMap.insert( pair<char,char>( 	'b' , 'h' ) );
  myMap.insert( pair<char,char>( 	'k' , 'i' ) );
  myMap.insert( pair<char,char>( 	'u' , 'j' ) );
  myMap.insert( pair<char,char>( 	'o' , 'k' ) );
  myMap.insert( pair<char,char>( 	'm' , 'l' ) );
  myMap.insert( pair<char,char>( 	'x' , 'm' ) );
  myMap.insert( pair<char,char>( 	's' , 'n' ) );
  myMap.insert( pair<char,char>( 	'e' , 'o' ) );
  myMap.insert( pair<char,char>( 	'v' , 'p' ) );
  myMap.insert( pair<char,char>( 	'z' , 'q' ) );
  myMap.insert( pair<char,char>( 	'p' , 'r' ) );
  myMap.insert( pair<char,char>( 	'd' , 's' ) );
  myMap.insert( pair<char,char>( 	'r' , 't' ) );
  myMap.insert( pair<char,char>( 	'j' , 'u' ) );
  myMap.insert( pair<char,char>( 	'g' , 'v' ) );
  myMap.insert( pair<char,char>( 	't' , 'w' ) );
  myMap.insert( pair<char,char>( 	'h' , 'x' ) );
  myMap.insert( pair<char,char>( 	'a' , 'y' ) );
  myMap.insert( pair<char,char>( 	'q' , 'z' ) );
  myMap.insert( pair<char,char> (' ', ' '));
  
  
}

string convert(string line, map<char,char> &myMap) {
  string answer;
  for ( int i =0; i<line.size(); i++) {
    answer= answer+ myMap.find(line[i])->second;
  }
  
  return answer;
}


int main(int argc, char *argv[])
{
  map <char,char> GoogletoEngMap;
  initMap(GoogletoEngMap);
  
 
  ifstream input("A-small-practice.in");
  ofstream output("output.txt");
  string line; int numOfCases; string answer;
  if(input.is_open() && input.good()){
    numOfCases = getNumofCases(input); //get cases first
    
    for (int i =1 ; i<=numOfCases; i ++) {
      output<<"Case #"<<i<<": ";
      
      if(input.good() ) getline(input, line);
      else { cout<< "Uh oh .. faulty input .. case numbers != num of lines"; return 0; }
      
      answer = convert(line,GoogletoEngMap) ;
      output << answer<<endl;
      
    }
    
  }
  return 0;
}
