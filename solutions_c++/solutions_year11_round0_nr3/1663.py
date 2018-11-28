
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

ifstream inFile;
ofstream outFile;

vector<int> pieces;

int largest_value;
int total_value;
int xor_value;

void
find_partition(int piece, int psum, int ssum, int p_xor, int s_xor)
{
	if (piece >= pieces.size())
		return;
	if (psum > ssum)
		return;
	if (ssum < largest_value)
		return;
	int temp1 = pieces[piece] ^ p_xor;
	int temp2 = pieces[piece] ^ s_xor;
	if (temp1 == temp2)
	{
		if (largest_value < ssum - pieces[piece])
			largest_value = ssum - pieces[piece];
		
		find_partition(piece + 1, psum, ssum, p_xor, s_xor);
	} else {
		find_partition(piece + 1, psum + pieces[piece], ssum - pieces[piece], temp1, temp2);
		find_partition(piece + 1, psum, ssum, p_xor, s_xor);
	}
}

int
main()
{
	inFile.open("input.txt");
	outFile.open("output.txt");

	int num_cases;
	inFile >> num_cases;
	
	int num_pieces;
	int value;
	for (int curr_case = 0 ; curr_case < num_cases ; curr_case++)
	{
		pieces.clear();
		total_value = 0;
		xor_value = 0;
		inFile >> num_pieces;
		for (int curr_piece = 0 ; curr_piece < num_pieces ; curr_piece++)
		{
			inFile >> value;
			pieces.push_back(value);
			total_value += value;
			xor_value ^= value;
		}
		largest_value = 0;
		if (xor_value == 0)
		{
			find_partition(0, 0, total_value, 0, xor_value);
			outFile << "Case #" << curr_case + 1 << ": " << largest_value << endl;
		} else
			outFile << "Case #" << curr_case + 1 << ": NO" << endl;
	}

	return 0;
}


