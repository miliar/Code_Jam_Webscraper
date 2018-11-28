#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
  int cases;
  string s;
  char c;
  
  ifstream myfile("A-small-attempt0.in");
  ofstream answer;
  answer.open ("answer.out");
  
  myfile >> cases;
  getline(myfile,s);
  
  for(int i=0; i < cases; ++i)
  {
    getline(myfile, s);
	answer << "Case #" << i+1 << ": ";
	for(int k=0; k < s.size(); ++k)
	{
	  c = s.at(k);
	  if(c == 'a')
	    answer << 'y';
      else if(c == 'b')
	    answer << 'h';
	  else if(c == 'c')
	    answer << 'e';
	  else if(c == 'd')
	    answer << 's';
	  else if(c == 'e')
	    answer << 'o';
      else if(c == 'f')
	    answer << 'c';
      else if(c == 'g')
	    answer << 'v';
      else if(c == 'h')
	    answer << 'x';
      else if(c == 'i')
	    answer << 'd';
	  else if(c == 'j')
	    answer << 'u';
	  else if(c == 'k')
	    answer << 'i';
      else if(c == 'l')
	    answer << 'g';
	  else if(c == 'm')
	    answer << 'l';
      else if(c == 'n')
	    answer << 'b';
      else if(c == 'o')
	    answer << 'k';
      else if(c == 'p')
	    answer << 'r';
	  else if(c == 'q')
	    answer << 'z';
      else if(c == 'r')
	    answer << 't';
      else if(c == 's')
	    answer << 'n';
	  else if(c == 't')
	    answer << 'w';
	  else if(c == 'u')
	    answer << 'j';
	  else if(c == 'v')
	    answer << 'p';
	  else if(c == 'w')
	    answer << 'f';
      else if(c == 'x')
	    answer << 'm';
      else if(c == 'y')
	    answer << 'a';
	  else if(c == 'z')
	    answer << 'q';
      else if(c == ' ')
	    answer << ' ';
	}
	answer << endl;
  }
  
  return 0;
}