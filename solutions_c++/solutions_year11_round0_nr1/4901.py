#include <fstream>
#include <string>
using namespace std;

int main()
{
	int T;
	int N;
	ifstream infile("X.txt");
	infile >> T;
	for (int t = 1; t <= T; ++t)
	{
		float y = 0;
		float yO = 0;
		float yB = 0;
		float yOr = 0;
		float yBr = 0;
		string R; 
		int O;
		int B;
		int PO = 1;
		int PB = 1;
		infile >> N;
		for (int n = 1; n <= N; ++n)
		{
			infile >> R;
			if (R == "O")
			{
				infile >> O;
				if (PO > O)
				{yO = (PO - O + 1);}
				else
				{yO = (O - PO + 1);}
				if (yOr + yO > yBr)
				{yOr = yOr + yO;}
				else
				{yOr = yBr + 1;}
				PO = O;
			}
			else
			{
				infile >> B;
				if (PB > B)
				{yB = (PB - B + 1);}
				else
				{yB = (B - PB + 1);}
				if (yBr + yB > yOr)
				{yBr = yBr + yB;}
				else
				{yBr = yOr + 1;}
				PB = B;
			}
		}
		if (yBr > yOr)
		{y = yBr;}
		else
		{y = yOr;}
		ofstream outfile("A.txt", ios_base::app);
		outfile << "Case#";
		outfile << '\0';
		outfile << t;
		outfile << ":";
		outfile << '\0';
		outfile << y;
		outfile << endl;
	}
	return 0;
}