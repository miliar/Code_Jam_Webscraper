#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <fstream>

///////////////////////////////////////////////////////

using namespace std;

///////////////////////////////////////////////////////

class DecryptingStr
{
public:
  DecryptingStr( string inFileName, string outFileName )
  {
    m_inFileName = inFileName;
    m_outFileName = outFileName;
  }
  
  map<char,char> getStyleFromSample();
  
  vector<string> getLineFromFile(); 
  
  void writeLineToFile( string line, map<char,char> myMap );
  
private:
  string m_inFileName;
  string m_outFileName;
};

///////////////////////////////////////////////////////

vector<string> DecryptingStr::getLineFromFile()
{
  ifstream file( m_inFileName.c_str() );
  vector<string> lines;
  std::string line;
  while(std::getline(file,line))
    lines.push_back(line);
     
  return lines;
}

///////////////////////////////////////////////////////

map<char,char> DecryptingStr::getStyleFromSample()
{
  string str1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
  string str11 = "our language is impossible to understand";
  string str2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
  string str21 = "there are twenty six factorial possibilities";
  string str3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
  string str31 = "so it is okay if you want to just give up";
  
  map<char,char> m1;
  
  for( int i = 0; i < str1.length(); i++ )
    m1.insert(make_pair(str1[i], str11[i]) );
  
  for( int i = 0; i < str2.length(); i++ )
    m1.insert(make_pair(str2[i], str21[i]) );
  
  for( int i = 0; i < str3.length();i++)
    m1.insert(make_pair(str3[i], str31[i]) );
  
  map<char,char>::iterator it;
  
  m1.insert(make_pair('q','z'));
  m1.insert(make_pair('z','q'));
  
  for( it = m1.begin(); it != m1.end(); it++)
    //cout << it->first << " " << it->second << "\n";
  
  //cout << "\n" << "\n";
  
  return m1;
}

///////////////////////////////////////////////////////

void DecryptingStr::writeLineToFile( string line, map<char,char> myMap )
{
  vector<char> v1;
  vector<char> v2;
  
  for( int i = 0; i < line.length(); i++ )
  {
    v1.push_back(line[i]);
  }
  
  map<char,char>::iterator mapIt;
  
  vector<char>::iterator it;
  for( it = v1.begin(); it != v1.end(); it++ )
  {
    mapIt = myMap.find(*it);
    v2.push_back( mapIt->second );
  }
  
  vector<char>::iterator it1;
  
  static int count = 1;
  string finalString( "" );
  
  for( it1 = v2.begin(); it1 != v2.end(); it1++ )
  {
     finalString = finalString + *it1;
  }
  
  ofstream oss( m_outFileName.c_str(), ios::out|ios::app);
  
  oss << "Case #" << count << ": " << finalString << "\n";
  count++;
}

///////////////////////////////////////////////////////

int main()
{
  DecryptingStr obj( "A-small-attempt0.in", "A-small-attempt0.out" );
  map<char,char> myMap;
  
  vector<string> lines;
  
  myMap = obj.getStyleFromSample();
  lines = obj.getLineFromFile();
  
  vector<string>::iterator it;
    
  for( it = lines.begin()+1; it != lines.end(); it++ )
  {
    //cout << "lines: " << *it << "\n";
    obj.writeLineToFile( *it, myMap );
  }
    
  return 0;
}