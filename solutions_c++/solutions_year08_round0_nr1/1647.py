#include<iostream>
#include <sstream>
#include<fstream>
#include <math.h>
#include <iomanip>
#include <time.h>
#include <list>

//using namespace std;

using std::istringstream;
using std::string;
using std::cout;
using std::cerr;
using std::endl;
using std::ifstream;
using std::ofstream;
using std::ios;
using std::getline;

#define LARGE 1000000

/////////////////////////
// Function declaration
/////////////////////////


int main(int argc, char *argv[])
{
	if (argc != 2)
	{
		cerr << "Usage: triangle file" << endl;
		exit (1);
	}

	////////////////////////
	// Variables definition
	////////////////////////

	int _N; // the number of test cases
	int * _NSearchEngine; // the number of search engines
	int * _NQueries; //the number of incoming queries
	string ** _searchEngines;
	string ** _queries;
	int * _min;
	bool ** _matchBox;
	int ** _minSwitches;



	////////////////////
	// Read Input File
	////////////////////

        ifstream _inFile(argv[1], ios::in);
        if (!_inFile.is_open())
        {
                cerr << "Error opening input file" << endl;
                exit (1);
        }

	if (! _inFile.eof() )
		_inFile >> _N;

	_NSearchEngine = new int[_N];
	_NQueries = new int[_N];
	_searchEngines = new string * [_N];
	_queries = new string * [_N];
	_min = new int[_N];

	for (int i = 0; i < _N; i++)
	{
		_inFile >> _NSearchEngine[i];
		_inFile.ignore(256,'\n');

//		cout << "_NSearchEngine=" << _NSearchEngine << endl;

		_searchEngines[i] = new string [_NSearchEngine[i]];

		for (int s = 0; s < _NSearchEngine[i]; s++)
			getline(_inFile, _searchEngines[i][s]);

// 		for (int j = 0; j < _NSearchEngine; j++)
// 			cout << _searchEngines[i][j] << "---" <<endl;


		_inFile >> _NQueries[i];
		_inFile.ignore(256,'\n');
		
//  		cout << "_NQueries=" << _NQueries[i] << endl;

		if (_NQueries[i] > 0)
		{
			_queries[i] = new string [_NQueries[i]];
	
			for (int q = 0; q < _NQueries[i]; q++)
				getline(_inFile, _queries[i][q]);

// 			for (int q = 0; q < _NQueries[i]; q++)
// 				cout << _queries[i][q] << "---" << endl;
		}
		_min[i] = 0;
	}

	_inFile.close();

			

	//////////////////////
	// Main calculation
	//////////////////////

	for (int i = 0; i < _N; i++)
	{
		if (_NQueries[i] > 0)
		{

			_matchBox = new bool * [_NSearchEngine[i]];
			_minSwitches = new int * [_NSearchEngine[i]];
			for (int s = 0; s < _NSearchEngine[i]; s++)
			{
				_matchBox[s] = new bool [_NQueries[i]];
				_minSwitches[s] = new int [_NQueries[i]];
			}
	
			for (int s = 0; s < _NSearchEngine[i]; s++)
				for (int q = 0; q < _NQueries[i]; q++)
					_matchBox[s][q] = (_searchEngines[i][s] == _queries[i][q]);
	
// 			for (int s = 0; s < _NSearchEngine[i]; s++)
// 			{
// 				for (int q = 0; q < _NQueries[i]; q++)
// 					cout << _matchBox[s][q] << " ";
// 				cout << endl;
// 			}
// 			cout << endl;
	
			for (int s = 0; s < _NSearchEngine[i]; s++)
			{
				_minSwitches[s][_NQueries[i]-1] = (_matchBox[s][_NQueries[i]-1] ? 1 : 0 );
			}

			for (int q = _NQueries[i]-2; q >= 0; q--)
			{
				int _m = LARGE, _unmatched = LARGE;
				for (int s = 0; s < _NSearchEngine[i]; s++)
				{
					if (!_matchBox[s][q])
					{
						_minSwitches[s][q] = _minSwitches[s][q+1];
						if (_m > _minSwitches[s][q])
							_m = _minSwitches[s][q];
					} else
						_unmatched = s;
				}
				if (_unmatched < LARGE) _minSwitches[_unmatched][q] = 1 + _m;
			}
	
// 			for (int s = 0; s < _NSearchEngine[i]; s++)
// 			{
// 				for (int q = 0; q < _NQueries[i]; q++)
// 					cout << _minSwitches[s][q] << " ";
// 				cout << endl;
// 			}
// 			cout << endl;
// 			cout << endl;
			
			_min[i] = LARGE;
			for (int s = 0; s < _NSearchEngine[i]; s++)
			{
				if (_min[i] > _minSwitches[s][0])
					_min[i] = _minSwitches[s][0];
			}
	
			for (int s = 0; s < _NSearchEngine[i]; s++)
			{
				delete _matchBox[s]; _matchBox[s] = 0;
				delete _minSwitches[s]; _minSwitches[s] = 0;
			}
			delete _matchBox; _matchBox = 0;
			delete _minSwitches; _minSwitches = 0;
		}
	}



	//////////////
	// Output
	//////////////

        ofstream outFile("results.out", ios::out);
        if (!outFile.is_open())
        {
                cout << "Error opening output file" << endl;
                exit (1);
        }

	for (int i = 0; i < _N; i++)
	{
		outFile << "Case #" << i+1 << ": " << _min[i] << endl;
	}
        outFile.close();




	///////////////////
	// Clean up memory
	///////////////////
	

	for (int i = 0; i < _N; i++)
	{
		delete [] _searchEngines[i]; _searchEngines[i] = 0;
		delete [] _queries[i]; _queries[i] = 0;
	}
	delete _NSearchEngine; _NSearchEngine = 0;
	delete _NQueries; _NQueries = 0;
	delete [] _searchEngines; _searchEngines = 0;
	delete [] _queries; _queries = 0;
	delete _min; _min = 0;

	return 0;
}

