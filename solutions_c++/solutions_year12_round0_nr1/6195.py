#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main () {

  char G[110];
  string T;
  int count=0;
  int i=0;
  

  ifstream myfile ("A-small-attempt2.in");
  ofstream outfile ("results.in");

  if (myfile.is_open() && outfile.is_open())
  {
	 getline (myfile,T);
	 
    while (count < 30 )
    {
      myfile.getline(G,110);
	  outfile<<"Case #"<<count+1<<": ";
	  i=0;

	  while(i<strlen(G))
	  {
        switch(G[i])
		{
		case 'a':
			outfile<<'y';
			break;
		case 'b':
			outfile<<'h';
			break;
		case 'c':
			outfile<<'e';
			break;
		case 'd':
			outfile<<'s';
			break;
		case 'e':
			outfile<<'o';
			break;
		case 'f':
			outfile<<'c';
			break;
		case 'g':
			outfile<<'v';
			break;
		case 'h':
			outfile<<'x';
			break;
		case 'i':
			outfile<<'d';
			break;
		case 'j':
			outfile<<'u';
			break;
		case 'k':
			outfile<<'i';
			break;
		case 'l':
			outfile<<'g';
			break;
		case 'm':
			outfile<<'l';
			break;
		case 'n':
			outfile<<'b';
			break;
		case 'o':
			outfile<<'k';
			break;
		case 'p':
			outfile<<'r';
			break;
		case 'q':
			outfile<<'z';
			break;
		case 'r':
			outfile<<'t';
			break;
		case 's':
			outfile<<'n';
			break;
		case 't':
			outfile<<'w';
			break;
		case 'u':
			outfile<<"j";
			break;
		case 'v':
			outfile<<'p';
			break;
		case 'w':
			outfile<<'f';
			break;
		case 'x':
			outfile<<'m';
			break;
		case 'y':
			outfile<<'a';
			break;
		case 'z':
			outfile<<'q';
			break;
		case ' ':
			outfile<<' ';
			break;
         
		}
		i++;
	  }
	  outfile<<'\n';
	  count++;
	}
    myfile.close();
	outfile.close();
	
  }

  else cout << "Unable to open file"; 
  return 0;
}