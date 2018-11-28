#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
using namespace std;

int main () {
  string line;
  ifstream myfile ("/home/grnag/code/A-small-attempt0.in");
  ofstream myofile ("/home/grnag/code/output");

    string str,str1;
    int C, N;

    string xxx = "yhesocvxduiglbkrztnwjpfmaq";

    getline(myfile, str);
    stringstream strstream(str);

    strstream >> C;
    N = C;

  if (myfile.is_open())
  {
    while ( myfile.good() )
    {
      getline (myfile,line);
		cout << "Case #" << (N-C--);
		myofile << "Case #" << (N-C) << ": ";
	for(int i =0; i < line.length(); i++)
	{
	if (line[i] != ' ')
		{
		int N = line[i];
		cout << xxx[N-97];
		myofile << xxx[N-97];
		}
	else
		{
		cout << " ";
		myofile << " ";
		}
	}
	cout << endl;
	myofile << endl;
    }
    myfile.close();
  }

  else cout << "Unable to open file"; 

  return 0;
}
