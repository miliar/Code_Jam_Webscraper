#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <set>
using namespace std;

int main()
{
	ifstream inFile("A-large.in");
	string T_str, N_str, A_wire_str, B_wire_str;
	int T, N, A_wire, B_wire, test_case = 0, num_intersect, B_value;
	set<int> B_set;

	typedef map<int, int> mapType;
	mapType wireMap;


	if (inFile.is_open())
	{
		getline(inFile, T_str);
		T = atoi(T_str.c_str());

		ofstream outFile("A_out.txt");
		while (test_case < T)
		{
			getline(inFile, N_str);
			N = atoi(N_str.c_str());
			for (int iter = 0; iter < N; iter++)
			{
				getline(inFile, A_wire_str, ' ');
				A_wire = atoi(A_wire_str.c_str());
				getline(inFile, B_wire_str);
				B_wire = atoi(B_wire_str.c_str());

				wireMap.insert(pair<int, int>(A_wire, B_wire));
				B_set.insert(B_wire);
			}

			set<int>::iterator B_iter, iz;
			num_intersect = 0;
			for (mapType::iterator A_iter = wireMap.begin(); A_iter != wireMap.end(); A_iter++)
			{
				B_value = A_iter->second;
				B_iter = B_set.find(B_value);
				if (B_iter != B_set.end())
				{
					for (iz = B_set.begin(); iz != B_iter; iz++)
					{
						++num_intersect;
					}

					B_set.erase(B_iter);
				}
			}
			wireMap.clear();
			outFile << "Case #" << ++test_case << ": " << num_intersect << endl;
		}
	}
	else
		cout << "Unable to open file." << endl;

	return 0;
}