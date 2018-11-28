#include <Windows.h>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <math.h>

using namespace std;

int main(int argc, char *argv[], char *envp[])
{
	int iCounter = 0;
	int T = 0;
	int K = -1;
	int N = -1;
	ifstream file_in;
	ofstream file_out;

	file_in.open("input.txt", ios::in);
	file_out.open("output.txt", ios::out);

	file_in >> T;

	if (T > 0)
	{
		//cout << "T: " << T << endl;
		
		for (iCounter = 1; iCounter <= T; iCounter++)
		{
			file_in >> N;
			file_in >> K;

			if (N != -1)
			{
				if (K != -1)
				{
					file_out << "Case #" << iCounter << ": ";
					if (((K + 1) % (int)pow((double)2, (int)N)) == 0)
					{
						file_out << "ON";
					}
					else
					{
						file_out << "OFF";
					}
					file_out << endl;
				}
				else
				{
					cout << "Invalid K on line " << iCounter << endl;
				}
			}
			else
			{
				cout << "Invalid N on line " << iCounter << endl;
			}

			N = -1;
			K = -1;
		}
	}
	else
	{
		cout << "Error: Invalid T" << endl;
	}

	file_in.close();
	file_out.close();

	cin >> T;

	return 0;
}