#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int	main()
{
	int		i, j, k;
	int		n;		// test cases
	int		turnaroundTime;
	int		aTotal;
	int		bTotal;	// number of trains leaving a to b ( and vice versa )

	vector<int> aStart;
	vector<int> aReady;
	vector<int> bStart;
	vector<int> bReady;

	// open input file
	ifstream iFile("input.txt");
	// create output file
	ofstream oFile("output.txt");
	// number of test cases 
	iFile >> n;
	
	k = 1;		// case
	while( n > 0 )
	{
		aReady.clear();
		bReady.clear();
		aStart.clear();
		bStart.clear();

		iFile >> turnaroundTime;
		iFile >> aTotal;
		iFile >> bTotal;

		int	hours, minutes;
		char	c;
		for( i=0; i<aTotal; i++ )
		{
			iFile >> hours;
			//cout << hours;
			iFile >> c;
			//cout << c;
			iFile >> minutes;
			//cout << minutes << endl;
			aStart.push_back(hours*60 + minutes);
			iFile >> hours;
			//cout << hours;
			iFile >> c;
			//cout << c;
			iFile >> minutes;
			//cout << minutes << endl;
			bReady.push_back(hours*60 + minutes + turnaroundTime);
		}
		for( i=0; i<bTotal; i++ )
		{
			iFile >> hours;
			//cout << hours;
			iFile >> c;
			//cout << c;
			iFile >> minutes;
			//cout << minutes << endl;
			bStart.push_back(hours*60 + minutes);
			iFile >> hours;
			//cout << hours;
			iFile >> c;
			//cout << c;
			iFile >> minutes;
			//cout << minutes << endl;
			aReady.push_back(hours*60 + minutes + turnaroundTime);
		}
		sort( aReady.begin(), aReady.end() );
		sort( bReady.begin(), bReady.end() );
		sort( aStart.begin(), aStart.end() );
		sort( bStart.begin(), bStart.end() );

		for( i=0; i<(int)bReady.size(); i++ )
		{
			for( j=0; j<(int)bStart.size(); j++ )
			{
				if( bReady[i] <= bStart[j] )
				{	
					bStart.erase(bStart.begin()+j);
					break;
				}
			}
		}
		for( i=0; i<(int)aReady.size(); i++ )
		{
			for( j=0; j<(int)aStart.size(); j++ )
			{
				if( aReady[i] <= aStart[j] )
				{	
					aStart.erase(aStart.begin()+j);
					break;
				}
			}
		}
		oFile << "Case #" << k << ": " << aStart.size() << " " << bStart.size() << endl;
		k++;
		n--;
	}
	return 0;
}