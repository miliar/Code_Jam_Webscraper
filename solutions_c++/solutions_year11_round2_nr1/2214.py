#include <iomanip>
#include <fstream>
#include <iostream>
using namespace std;

int main()
{
	ifstream fin("A.in");
	ofstream fout("A.out");

	int test_cases, dimension, rows, columns, i, j, d;
	fin >> test_cases;
	char matrix[100][100];
	long double OWP, OOWP, counterOnes, counterAll;
	long double WPs[100], OWPs[100], Ds[100];
	for (int current_case = 1; current_case <= test_cases; current_case++)
	{
		fout << "Case #" << current_case << ":" << endl;
		fin >> dimension;
		for (rows = 0; rows < dimension; rows++)
			for (columns = 0; columns < dimension; columns++)
				fin >> matrix[rows][columns];

		//for (rows = 0; rows < dimension; rows++) {
		//	for (columns = 0; columns < dimension; columns++)
		//		cout << matrix[rows][columns];
		//	cout << endl;
		//}

		for (rows = 0; rows < dimension; rows++)
		{
			// Calculate WP.
			counterOnes = counterAll = 0;
			for (columns = 0, d = dimension; columns < dimension; columns++)
			{
				if (matrix[rows][columns] == '0')
				{
					counterAll++;
				}

				if (matrix[rows][columns] == '1')
				{
					counterOnes++;
					counterAll++;
				}

				if (matrix[rows][columns] == '.')
					d--;
			}
			WPs[rows] = (counterOnes / counterAll);
			Ds[rows] = d;

			// Calculate OWP.
			for (i = 0, OWP = 0; i < dimension; i++) 
			{
				if (i != rows && matrix[rows][i] != '.') // Skip our row and the blank ones.
				{
					counterOnes = counterAll = 0;
					for (j = 0; j < dimension; j++)
					{
						if (j != rows && matrix[i][j] != '.') // Skip our column and the blank ones.
						{
							if (matrix[i][j] == '0')
							{
								counterAll++;
							}

							if (matrix[i][j] == '1')
							{
								counterOnes++;
								counterAll++;
							}
						}
					}
					OWP += (counterOnes / counterAll);
				}
			}

			OWP /= d;
			OWPs[rows] = OWP;
		}

		// Calculate OOWP.
		for (rows = 0; rows < dimension; rows++)
		{
			for (OOWP = 0, columns = 0; columns < dimension; columns++)
				if (matrix[rows][columns] != '.')
					OOWP += OWPs[columns];

			OOWP /= Ds[rows];
			fout << setprecision (12) << (0.25 * WPs[rows] + 0.50 * OWPs[rows] + 0.25 * OOWP) << endl;
		}
	}

	return 0;
}