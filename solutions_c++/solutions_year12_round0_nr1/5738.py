// reading a text file
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main () {
  string line;
  int CASE=0;
  int i=0, len, base=0;
  char az[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
  ifstream myfile ("A-small-attempt0.in");
  if (myfile.is_open())
  {
    while ( myfile.good() )
    {
      getline (myfile,line);
      if (myfile !=NULL)
      	cout << "Case #" << CASE++ << ": ";
      for(i=0;line[i]!=0;i++)
      {       
      	base=line[i]-'a';
        if(base>=0&&base<=25)
            cout << az[base];
        else
        {
            cout << " ";
        }
       }
       cout << endl ;
    }
    myfile.close();
  }

  else cout << "Unable to open file"; 

  return 0;
}
