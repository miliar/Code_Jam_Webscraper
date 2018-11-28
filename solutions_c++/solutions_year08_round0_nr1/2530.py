#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <algorithm>
#include <string>
#include <conio.h>
using namespace std;

class engine
{
public:
	string name; // name of the engine
	int sp; // selection priority of the engine
	engine( const string &n ): name(n), sp(0) {}
	~engine( void ) {}
};

// overloads and sort function
bool operator==( const engine &e1, const engine &e2 ) { return e1.name == e2.name; }
bool operator!=( const engine &e1, const engine &e2 ) { return e1.name != e2.name; }
bool sortengineBiggerToSmall( const engine &e1, const engine &e2 ) { return e1.sp>e2.sp; }


void selectenginesmartly( vector<engine> &engines, vector<string> inputs, vector<engine>::iterator &selectedengine )
{
	vector<engine> selectionlist;
	vector<string>::iterator itinput;
	vector<engine>::iterator itengine;
	int count;

	// find engine which consumes most of our inputs
	itengine = engines.begin();
	while( itengine != engines.end() )
	{
		count = 0;
		itinput = inputs.begin();
		while( itinput != inputs.end() )
		{
			if( *itinput == itengine->name )
				break;
			itinput++;
			count++;
		}
		itengine->sp = count;
		itengine++;
	}

	//
	sort( engines.begin(), engines.end(), sortengineBiggerToSmall );
	selectedengine = engines.begin();
}

int savetheuniverse( vector<engine> engines, vector<string> inputs )
{
	vector<engine>::iterator itengine;
	vector<engine>::iterator itengine1;
	vector<string>::iterator itinput;
	int result;

	result = 0;
	selectenginesmartly( engines, inputs, itengine );

	// calculate results
	itinput = inputs.begin();
	cout<<itengine->name<<endl;
	while( itinput != inputs.end() )
	{
		// switch engine
		if( *itinput == (*itengine).name )
		{
			string preveng = itengine->name; // to prevent deadlock
			selectenginesmartly( engines, inputs, itengine );
			if( itengine->name == preveng )
				itengine++;
			if( itengine == engines.end() )
				itengine = engines.begin();
			cout<<itengine->name<<endl;
			result++;
		}
		else
		{
			inputs.erase( itinput );
			itinput = inputs.begin();
		}
	}

	return result;
}

int main( void )
{
	vector<engine> engines;
	vector<string> inputs;
	int n;
	int s;
	int q;
	ifstream input;
	ofstream out;
	string line;

	input.open("A-large.in", ios::in);
	//input.open("savingtheuniverse.in", ios::in);
	out.open("A-large.out", ios::out);
	//out.open("savingtheuniverse.out", ios::out);
	if( input.fail() || out.fail() )
	{
		cerr << "file io failed" << endl;
		return -1;
	}

	input >> n;
	// test cases
	for( int i=0; i<n; i++ )
	{
		input >> s;
		input.ignore();
		
		// read engines
		while( s-->0 )
		{
			getline( input, line );
			engines.push_back( line );
		}

		// read inputs
		input >> q;
		input.ignore();
		while( q-->0 )
		{
			getline( input, line );
			inputs.push_back( line );
		}

		int res = savetheuniverse( engines, inputs );
		cout << "Case #" << i+1 << ": " << res << endl;
		out << "Case #" << i+1 << ": " << res << endl;
		
		engines.clear();
		inputs.clear();
	}

	input.close();
	out.close();
	getch();
}