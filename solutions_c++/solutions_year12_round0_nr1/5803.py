#include <iostream>
#include <fstream>
#include <map>
#include <algorithm>
#include <vector>
#include <set>
#include <string>

using namespace std;


 char charMap(char x) {
        switch (x) {
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
        }
        return x;
    }

int main()
{

  ifstream rdfile;
  std::ofstream ofile("output.txt");
  string str;


  rdfile.open("A-small-attempt0.in");
  
  int count, ic = 0;

  rdfile >> count;
  char r;
  getline(rdfile,str);
  while(ic != count)
  {
	  string output = "";
	  getline(rdfile,str);

	  //cout <<str<<endl;
	  for(int i=0;i<str.length();i++)
	  {
		  r = str[i];
		  if(r == ' ')
		  {
			  output = output + r;
			  continue;
		  }
		  else
		  {
			  output = output+charMap(r);
		  }
	  }

	  //cout << "Case #"<<ic+1<<": "<<output<<endl;
      ofile<<"Case #"<<ic+1<<": "<<output<<endl;
	  ic++;

  }

  cin.get();

}