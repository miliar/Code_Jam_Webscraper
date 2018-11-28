#include <iostream>
#include <string>
#include <cstring>

using namespace std;


void createMap()
{

  char map[26];
  
  memset(map, '?', sizeof(map));
  
  string enc[3];
  string dec[3];


  enc[0] = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
  enc[1] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
  enc[2] = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
  
  dec[0] = "our language is impossible to understand";
  dec[1] = "there are twenty six factorial possibilities";
  dec[2] = "so it is okay if you want to just give up";
  
  for(int i=0; i < 3; ++i)
  {
  
    for(int j=0; j < enc[i].length(); ++j)
    {
    
      map[enc[i][j]-'a'] = dec[i][j];
      
    }
  
  }
  
  cout << "char map[26] = {";
  
  for(int i=0; i < 26; ++i)
  {
    cout << "'" << map[i] << "',";
  }
  
  cout << "}" << endl;

}



int main()
{
  //createMap();
  
  int T;
  cin >> T;
  cin.ignore();
  
  string line;
  
  char map[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
  
  int caseNum = 1;
  
  while(caseNum <= T)
  {
    getline(cin, line);
    
    for(int i=0; i < line.length(); ++i)
    {
      if(line[i] != ' ')
      {
        line[i] = map[line[i]-'a'];
      }
    }
    
    cout << "Case #" << caseNum << ": " << line << endl;
    
    ++caseNum;
  }
}
