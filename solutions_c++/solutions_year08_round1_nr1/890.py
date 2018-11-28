#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <list>

using namespace std;

void getInput(ifstream& source, int& number)
{
	string inp;
	getline(source, inp);
	istringstream ist(inp);
	ist >> number;
}

void getInput(ifstream& source, int n, list<long>& v)
{
	string inp;
	getline(source, inp);
	istringstream ist(inp);
	long value;
	
	for(int i = 0; i < n; i++)
	{
		ist >> value;
		list<long>::iterator it;
		for(it = v.begin(); it != v.end(); it++)
		{
			if( *it >= value)
			{
				v.insert(it, value);
				break;
			}
		}
		if( it == v.end() ) v.push_back( value );
	}
}

int main(int argc, char* argv[])
{
	if( argc != 2 ) return -1;

	std::ifstream source(argv[1]);

	if( !source ) return -1;

	int number;
	getInput(source, number);

	for(int cases = 0; cases < number; cases++)
	{
		cout << "Case #" << cases + 1 << ": ";
		int n;
		getInput(source, n);
		list<long> mylist1;
		list<long> mylist2;
		getInput(source, n, mylist1);
		
		//for(list<long>::iterator it = mylist1.begin(); it != mylist1.end(); it++)
		//	cout << *it << endl;
			
		getInput(source, n, mylist2);
		
		long long result = 0;
		list<long>::iterator it1 = mylist1.begin();
		list<long>::reverse_iterator it2 = mylist2.rbegin();
		for(int i = 0; i < n; i++)
		{
			result += (*it1) * (*it2);
			it1++; it2++;
		}
		cout << result << endl;
		
		mylist1.clear();
		mylist2.clear();
	}
	return 0;
}
