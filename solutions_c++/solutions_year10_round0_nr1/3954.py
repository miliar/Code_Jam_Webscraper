#include <iostream>
#include <limits.h>
#include <fstream>
#include <string>
#include <cmath>

#define TRUE 1
#define FALSE 0

using namespace std;


int main(int argc, char* argv[])
{
 unsigned long int index = 0;
 unsigned long int testcases;
 unsigned long int n;
 unsigned long int t;
 
 string res_str("");
 
 string buff;
 char* endptr =  new char[100];

 string in_filename = argv[1];
 string out_filename = "output.txt";

 ifstream inp_file;
 ofstream out_file;

 inp_file.open(in_filename.c_str());
 out_file.open(out_filename.c_str());

 getline(inp_file, buff);
 testcases = strtoul(buff.c_str(), NULL, 10);

while( !inp_file.eof() ) // To get you all the lines.
{


	getline(inp_file,buff); // Saves the line in STRING.

	if(buff.empty())
		break;

	res_str = "OFF";
	
	n = strtoul(buff.c_str(), &endptr, 10);
	t = strtoul(endptr, NULL, 10);
	//  cout << "n = " << n << " t = " << t << endl;
	
	unsigned long int power = pow((double) 2, (double) n);
	unsigned int long rem = t % power;
	
	//unsigned int long rem = 0;
	
	if(rem == (power - 1))
		res_str = "ON";
	
	index++;
	
	out_file << "Case #" << index << ": " << res_str << endl;

}
	
 inp_file.close();
 out_file.close();


 return 0;
}

