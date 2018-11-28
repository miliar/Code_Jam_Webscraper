#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main()
{
	ifstream infile("a-in.txt");
	ofstream outfile("a-out.txt");

	int t;
	int n;

	infile >> t;

	for (int icase = 0; icase < t; ++icase)
	{
		infile >> n;

		int oPos = 1;
		int bPos = 1;
		int oTime = 0;
		int bTime = 0;
		for (int i = 0; i < n; ++i)
		{
			string r;
			int k;

			infile >> r >> k;

			cout << "Robot: " << r << endl;
			cout << "Button: " << k << endl;

			int &pos = (r == "O" ? oPos : bPos);
			int &time = (r == "O" ? oTime : bTime);
			int &oppTime = (r != "O" ? oTime : bTime);

			int t = abs(k - pos);
			
			time = max(time + t + 1, oppTime + 1);
			pos = k;

			cout << "oPos = " << oPos <<  ", oTime = " << oTime << ", bPos = " << bPos << ", bTime = " << bTime << endl;
		}

		outfile << "Case #" << (icase + 1) << ": " << max(oTime, bTime) << endl;
	}

	return 0;
}
