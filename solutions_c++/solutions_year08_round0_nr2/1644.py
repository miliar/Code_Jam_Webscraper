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
using std::list;

#define LARGE 1000000

/////////////////////////
// Function declaration
/////////////////////////

struct Time {
    int depHr;
    int depMin;
    int arrHr;
    int arrMin;
};

int diff(Time first, Time second)
{
//cout << first.depHr <<" "<< first.depMin <<" "<< second.depHr<< " "<< second.depMin << endl;
	return (first.depHr - second.arrHr) * 60 + first.depMin - second.arrMin;
}

bool sortByDeparture (Time first, Time second)
{
	if (first.depHr < second.depHr)
		return true;
	if (first.depHr == second.depHr && first.depMin < second.depMin)
		return true;
	return false;
}

template <typename T>
bool fromString(const std::string &s, T &result)
{
std::istringstream stream(s);
return (stream >> result);
}

int numTrainsRequired(int, int, Time *, Time *, int);

int main(int argc, char *argv[])
{
	if (argc != 2)
	{
		cerr << "Usage: input file" << endl;
		exit (1);
	}

	////////////////////////
	// Variables definition
	////////////////////////

	int _N; // the number of test cases
	int * _turnAroundTime;
	int * _NA;
	int * _NB;
	Time ** _tA;
	Time ** _tB;
	int ** _nTrains;

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

	_turnAroundTime = new int[_N];
	_NA = new int[_N];
	_NB = new int[_N];
 	_tA = new Time * [_N];
	_tB = new Time * [_N];
	_nTrains = new int * [_N];

	for (int i = 0; i < _N; i++)
	{
		_inFile >> _turnAroundTime[i] >> _NA[i] >> _NB[i];
//		cout << _turnAroundTime[i] << "\t" << _NA[i] << "\t" << _NB[i] << endl;

		_inFile.ignore(256,'\n');

		_tA[i] = new Time [_NA[i]];
		_tB[i] = new Time [_NB[i]];

		for (int a = 0; a < _NA[i]; a++)
		{
			string _s;
			getline(_inFile, _s);
			if (!fromString(_s.substr(0,2), _tA[i][a].depHr))
				cerr << "Error in the conversion from string to int!!" << endl;
			if (!fromString(_s.substr(3,2), _tA[i][a].depMin))
				cerr << "Error in the conversion from string to int!!" << endl;
			if (!fromString(_s.substr(6,2), _tA[i][a].arrHr))
				cerr << "Error in the conversion from string to int!!" << endl;
			if (!fromString(_s.substr(9,2), _tA[i][a].arrMin))
				cerr << "Error in the conversion from string to int!!" << endl;
//cout << _tA[i][a].depHr << ":" << _tA[i][a].depMin << "\t" << _tA[i][a].arrHr << ":" << _tA[i][a].arrMin << endl;
		}

		for (int b = 0; b < _NB[i]; b++)
		{
			string _s;
			getline(_inFile, _s);
			if (!fromString(_s.substr(0,2), _tB[i][b].depHr))
				cerr << "Error in the conversion from string to int!!" << endl;
			if (!fromString(_s.substr(3,2), _tB[i][b].depMin))
				cerr << "Error in the conversion from string to int!!" << endl;
			if (!fromString(_s.substr(6,2), _tB[i][b].arrHr))
				cerr << "Error in the conversion from string to int!!" << endl;
			if (!fromString(_s.substr(9,2), _tB[i][b].arrMin))
				cerr << "Error in the conversion from string to int!!" << endl;
//cout << _tB[i][b].depHr << ":" << _tB[i][b].depMin << "\t" << _tB[i][b].arrHr << ":" << _tB[i][b].arrMin << endl;
		}
	}

	_inFile.close();

			

	//////////////////////
	// Main calculation
	//////////////////////

	for (int i = 0; i < _N; i++)
	{
		_nTrains[i] = new int[2];

		_nTrains[i][0] = numTrainsRequired(_NA[i], _NB[i], _tA[i], _tB[i], _turnAroundTime[i]);

		_nTrains[i][1] = numTrainsRequired(_NB[i], _NA[i], _tB[i], _tA[i], _turnAroundTime[i]);
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
		outFile << "Case #" << i+1 << ": " << _nTrains[i][0] << " " << _nTrains[i][1] <<endl;
	}
        outFile.close();




	///////////////////
	// Clean up memory
	///////////////////
	
	delete _turnAroundTime; _turnAroundTime = 0;
	delete _NA; _NA = 0;
	delete _NB; _NB = 0 ;

	for (int i = 0; i < _N; i++)
	{
		delete _tA[i]; _tA[i] = 0;
		delete _tB[i]; _tB[i] = 0;
		delete _nTrains[i]; _nTrains[i] = 0;
	}
	delete _tA; _tA = 0;
	delete _tB; _tB = 0;
	delete _nTrains; _nTrains = 0;

	return 0;
}


int numTrainsRequired(int _NA, int _NB, Time * _tA, Time * _tB, int _turnAroundTime)
{
	list<Time> _myListA;

	for (int a = 0; a < _NA; a++)
		_myListA.push_back(_tA[a]);
	
	_myListA.sort(sortByDeparture);

 	list<Time>::iterator it;
// 	for (it=_myListA.begin(); it!=_myListA.end(); ++it)
// 		cout << it->depHr << ":" << it->depMin << endl;
// 	cout << endl;

	for (int b = 0; b < _NB; b++)
	{
		for (it=_myListA.begin(); it!=_myListA.end(); ++it)
		{
			if (diff(*it, _tB[b]) >= _turnAroundTime)
			{
				_myListA.erase(it);
				break;
			}
		}
// 		list<Time>::iterator it;
// 		for (it=_myListA.begin(); it!=_myListA.end(); ++it)
// 			cout << it->depHr << ":" << it->depMin << endl;
// 		cout << endl;
	}

	return _myListA.size();
}
