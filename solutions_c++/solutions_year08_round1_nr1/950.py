#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

string	upperCase( string str )
{
	string	s = "";
	int	i;
	for( i=0; i<(int)str.length(); i++ )
		s += toupper(str[i]);
	return s;
}


int	main()
{
	int	n;			// number of test cases
	int	i, j, k;
	

	// open input file
	ifstream iFile("input.txt");
	// create output file
	ofstream oFile("output.txt");
	// number of test cases
	iFile >> n;
	//cout << n << endl;

	int	v1, val;
	vector<int> V1;
	vector<int> V2;

	k = 1;		/* case number */
	while( n > 0 )
	{
		V1.clear();
		V2.clear();
		iFile >> v1;	//
		for( i=0; i<v1; i++ )
		{
			iFile >> val;
			V1.push_back(val);
		}
		for( i=0; i<v1; i++ )
		{
			iFile >> val;
			V2.push_back(val);
		}

		sort(V1.begin(), V1.end());
		sort(V2.begin(), V2.end());
		int	result = 0;
		for( i=0; i<v1; i++ )
		{
			result += V1[i] * V2[v1-1-i];
		}
		//getline( iFile, str );	// next line
		oFile << "Case #" << k << ": " << result << endl;

		k++;			// next test case
		n--;
	}
	return 0;
}