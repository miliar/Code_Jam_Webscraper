
#include <iostream>
#include <fstream>
#include <string>
#include <math.h>

using namespace std;

void dec2bin(long decimal, char *binary);

int main()
{	
	
	ifstream input("large.in");
	ofstream output("large.out");
	string line;

	int numInputs;

	input >> numInputs;

	for (int i=0; i<numInputs; i++)
	{
		long in1, in2;
		line = "";
		while (line == "")
			getline(input,line);
		sscanf(line.c_str(),"%ld %ld",&in1,&in2);
		output << "Case #" << i+1 << ": ";

		//It's like counting in binary with (in1) digits,
		// (in2) times: (need to check if the RIGHT (in1) digs
		// of the bin number are all 1.
		int out1 = in2 % (long)pow(2,(double)in1);
		char *bin = new char[in1];
		long outCheck = (long)pow(2,(double)in1)-1;
		char *binCheck = new char[in1];
		dec2bin(out1,bin);
		dec2bin(outCheck,binCheck);
		
		if (strcmp(bin,binCheck)==0)//process(in1,in2))
			output << "ON" << endl;
		else
			output << "OFF" << endl;
	}

	input.close();
	output.close();

	cout << "done";

	int a;
	cin >> a;


	return 0;
}


void dec2bin(long decimal, char *binary)
{
  int  k = 0, n = 0;
  int  neg_flag = 0;
  int  remain;
  char temp[80];

  do 
  {
    remain    = decimal % 2;
    decimal   = decimal / 2;
    temp[k++] = remain + '0';
  } while (decimal > 0);
 
  while (k >= 0)
    binary[n++] = temp[--k];
 
  binary[n-1] = 0;   
}
