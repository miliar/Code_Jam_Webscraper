#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
using namespace std;

int main ()
{
    string data[32]; // creates data to hold names
    short loop=0; //short for loop for input
	
    string line; //this will contain the data read from the file
    ifstream inputFile ("input.txt"); //opening the file.
	ofstream outputFile ("output.txt");
	if (inputFile.is_open() && outputFile.is_open()) //if the file is open
    {
        while (! inputFile.eof() ) //while the end of file is NOT reached
        {
			getline (inputFile,line); //get one line from the file
			std::string s = line;
			std::replace( s.begin(), s.end(), 'y', '_');
			std::replace( s.begin(), s.end(), 'w', '-');
			std::replace( s.begin(), s.end(), 't', 'w');
			std::replace( s.begin(), s.end(), 'r', 't');
			std::replace( s.begin(), s.end(), 'p', 'r');
			std::replace( s.begin(), s.end(), 'v', 'p');
			std::replace( s.begin(), s.end(), 'g', 'v');
			std::replace( s.begin(), s.end(), 'l', 'g');
			std::replace( s.begin(), s.end(), 'm', 'l');
			std::replace( s.begin(), s.end(), 'x', 'm');
			std::replace( s.begin(), s.end(), 'h', 'x');
			std::replace( s.begin(), s.end(), 'b', 'h');
			std::replace( s.begin(), s.end(), 'i', '#');
			std::replace( s.begin(), s.end(), 'k', 'i');
			std::replace( s.begin(), s.end(), 'o', 'k');
			std::replace( s.begin(), s.end(), 'e', 'o');
			std::replace( s.begin(), s.end(), 'c', 'e');
			std::replace( s.begin(), s.end(), 'd', '@');
			std::replace( s.begin(), s.end(), 'j', '!');
			std::replace( s.begin(), s.end(), 'n', 'b');
			std::replace( s.begin(), s.end(), 'q', '?');
			std::replace( s.begin(), s.end(), 's', 'n');
			std::replace( s.begin(), s.end(), 'u', 'j');
			std::replace( s.begin(), s.end(), 'f', 'c');
			std::replace( s.begin(), s.end(), 'a', 'y');
			std::replace( s.begin(), s.end(), 'z', 'q');
			std::replace( s.begin(), s.end(), '_', 'a');
			std::replace( s.begin(), s.end(), '-', 'f');
			std::replace( s.begin(), s.end(), '!', 'u');
			std::replace( s.begin(), s.end(), '?', 'z');
			std::replace( s.begin(), s.end(), '@', 's');
			std::replace( s.begin(), s.end(), '#', 'd');
			data[loop]=s;
            loop++;
        }
		int i=1;
		while (i<loop) {
			outputFile<<"Case #"<<i<<": "<<data[i]<<endl; //and output it
			i=i+1;
		}
        inputFile.close(); //closing the file
		outputFile.close();
    }
    else cout << "Unable to open file"; //if the file is not open output
    return 0;
}