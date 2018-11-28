#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
using namespace std;

string get_bulb_state(int, int);

int main () 
{
	int numTests, case_number = 1;
	string line_count;
	int N_int, K_int;
	string bulb_state = "OFF", N_string, K_string;

    ifstream inFile("A-large.in");
	if (inFile.is_open())
	{
		
		// Get number of lines in input file
		getline(inFile, line_count);
		numTests = atoi(line_count.c_str());
		
		// Open output file
		ofstream outFile;
		outFile.open("SnapperChain_Output.txt");
		if (!outFile.is_open())
		{
			cout << "Unable to open output file.\n";
			exit(1);
		}
		
		while (numTests > 0)
		{			
			// Get test case from input, N and K
			getline (inFile, N_string, ' ');
			getline (inFile, K_string);
			N_int = atoi(N_string.c_str());
			K_int = atoi(K_string.c_str());
			
			// Output
			outFile << "Case #" << case_number++ << ": ";
			outFile << get_bulb_state(N_int, K_int) << endl;
			
			numTests--;
		}
		outFile.close();
		inFile.close();
	}
	else
		cout << "Unable to open input file.\n";
	
	
	
    return 0;
}

string get_bulb_state(int N, int K)
{
	int max_num = pow(2, N);
	int snaps = K + 1;
	if ((snaps % max_num) == 0)
		return "ON";
	return "OFF";
}
	
	