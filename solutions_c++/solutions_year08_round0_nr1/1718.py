#include <iostream>
#include <fstream>
#include <vector>
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
	int	s;			// number of search engines
	int	q;			// number of queries
	int	i;
	string	str;
	vector<string>	engineList;
	vector<int>		engineCount;
	vector<string>	queryList;

	// open input file
	ifstream iFile("input.txt");
	// create output file
	ofstream oFile("output.txt");
	iFile >> n;

	int	k = 1;		/* case number */
	while( n > 0 )
	{
		iFile >> s;
		getline( iFile, str );	// next line
		//cout << s << endl;
		// clear vectors
		engineList.clear();
		engineCount.clear();
		queryList.clear();
		/* get search engines */
		for( i=0; i<s; i++ )
		{
			getline( iFile, str);
			str = upperCase(str);
			engineList.push_back(str);
			engineCount.push_back(0);
		}
		iFile >> q;
		getline( iFile, str );
		/* get list of queries */
		for( i=0; i<q; i++ )
		{
			getline( iFile, str);
			str = upperCase(str);
			queryList.push_back(str);
		}

		int	switchCount = 0;
		int	querySpot = 0;
		int	qS = 0;
		int	qSMax = -1;
		while( querySpot < q )
		{
			for( i=0; i<s; i++ )
			{
				qS = querySpot;	// reset the index to current spot
				while( queryList[qS] != engineList[i] )
				{
					qS++;
					if( qS == q )
						break;		// in case we hit the end...
				}
				if( qS > qSMax )
					qSMax = qS;
			}
			if( qSMax < q )
				switchCount++;
			querySpot = qSMax;
		}
		oFile << "Case #" << k << ": " << switchCount << endl;

		k++;			// next test case
		n--;

	}





	return 0;
}