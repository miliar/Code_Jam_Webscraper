#include <iostream>
#include <fstream>
#include <string>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

int main ()
{
	string arr[31];
	int loop=0;
	int tot;
	int i;
	int j;
	int sublength;
	string sub;
	string line;
	string nline;
	ifstream myFile("C:/users/bhcomp/desktop/A-small-attempt2.in");
	if (myFile.is_open())
	{
		while (!myFile.eof())
		{
			getline(myFile,line);
			arr[loop]=line;
			loop++;
		}
		myFile.close();
	}
    ofstream f("c:/users/bhcomp/desktop/outputA.txt");
	tot=atoi(arr[0].c_str());

	for(i=1; i<=tot; i++)
	{
	    if (i>1) {f << "\n";}
	    f << "Case #" << i << ": ";
		nline=arr[i];
		sublength = nline.length();
		for(j=0; j<= sublength; j++)
		{
		    //h=j+1;
			sub = nline.substr(j,1);
			if ( sub == "a") {f << "y";}
			else if(sub == "b") {f << "h";}
			else if(sub == "c") {f << "e";}
			else if(sub == "d") {f << "s";}
			else if(sub == "e") {f << "o";}
			else if(sub == "f") {f << "c";}
			else if(sub == "g") {f << "v";}
			else if(sub == "h") {f << "x";}
			else if(sub == "i") {f << "d";}
			else if(sub == "j") {f << "u";}
			else if(sub == "k") {f << "i";}
			else if(sub == "l") {f << "g";}
			else if(sub == "m") {f << "l";}
			else if(sub == "n") {f << "b";}
			else if(sub == "o") {f << "k";}
			else if(sub == "p") {f << "r";}
			else if(sub == "q") {f << "z";}
			else if(sub == "r") {f << "t";}
			else if(sub == "s") {f << "n";}
			else if(sub == "t") {f << "w";}
			else if(sub == "u") {f << "j";}
			else if(sub == "v") {f << "p";}
			else if(sub == "w") {f << "f";}
			else if(sub == "x") {f << "m";}
			else if(sub == "y") {f << "a";}
			else if(sub == "z") {f << "q";}
			else {f << " ";}
		}
	}
	return 0;
}
