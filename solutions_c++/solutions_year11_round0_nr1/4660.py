#include <iostream>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

enum ROBOT { ORANGE, BLUE };

struct Data
{
	Data(ROBOT _r, int _pos, int _value) : robot(_r), pos(_pos), value(_value) { }
	ROBOT robot;
	int pos;
	int value;
};

Data findNext(const vector<string> &table, ROBOT r)
{
	for(int i = 0; i < table.size(); ++i)
	{
		if( r == ORANGE )
		{
			if( table[i][0] == 'O' )
			{
				const char *s = table[i].c_str();
				return Data(ORANGE, i, atoi(s+1));
			}
		}
		else
		{
			if( table[i][0] == 'B' )
			{
				const char *s = table[i].c_str();
				return Data(BLUE, i, atoi(s+1));
			}
		}
	}

	return Data(r, -1, -1);
}

void deleteNext(vector<string> &table, ROBOT r)
{
	for(int i = 0; i < table.size(); ++i)
	{
		if( r == ORANGE )
		{
			if( table[i][0] == 'O' )
			{
				table[i] = " ";
				break;
			}
		}
		else
		{
			if( table[i][0] == 'B' )
			{
				table[i] = " ";
				break;
			}
		}
	}
}

template <class T>
void printArray(const vector<string> &vec)
{
	for(unsigned i = 0; i < vec.size(); ++i)
		cout << table[i] << " ";
	cout << "\n";
}

void readFromFile(ifstream &in, vector<string> &vec);

int play(vector<string> &vec);

int main()
{
	vector<string> vec;
	string s;

	ifstream in("input.in");
	ofstream out("kakka.txt");
	int cases;
	in >> cases;

	for(int i = 0; i < cases; ++i)
	{
		readFromFile(in, vec);
		out << "Case #" << i + 1 << ": " << play(vec);
		if( i < cases - 1 ) out << "\n";
		vec.clear();
	}
}

int play(vector<string> &vec)
{
	int orange = 1, blue = 1;
	bool pushed = false;

	unsigned counter = 0;

	int x = 0, y = 0;

	while( x != -1 || y != -1 )
	{
		// orange
		Data d = findNext(vec, ORANGE); // find next
		Data d2 = findNext(vec, BLUE);

		x = d.pos;
		//cout << "next orange: " << d.pos << " next blue: " << d2.pos << "\n";
		if( d.pos != -1 )
		{
			if( d.value > orange )
			{
				pushed = false;
				++orange;
				//cout << "ORANGE MOVES TO THE RIGHT\n";
			}
			else if( d.value < orange )
			{
				pushed = false;
				--orange;
				//cout << "ORANGE MOVES TO THE LEFT\n";
			}
			else // value == orange
			{
				if( d.pos > d2.pos &&  d2.pos != -1 ) // wait for BLUE
				{
					;//cout << "ORANGE STAYS AT " << orange << "\n";
					pushed = false;
				}
				else
				{
					pushed = true;
					deleteNext(vec, ORANGE);
					;//cout << "ORANGE PUSHES " << d.value << "\n";
				}
			}
		}
		else
			;//cout << "ORANGE STAYS AT " << orange << "\n";

		//printArray(table,SZ);
		//cout << "orange: " << orange << "\tblue = " << blue << "\n";
		//cin.get();

		// BLUE
		d = findNext(vec, BLUE);
		d2 = findNext(vec, ORANGE);
		y = d.pos;
		if( d.pos != -1 )
		{
			if( d.value > blue )
			{
				++blue;
				//cout << "BLUE MOVES TO THE RIGHT\n";
			}
			else if( d.value < blue )
			{
				--blue;
				//cout << "BLUE MOVES TO THE LEFT\n";
			}
			else
			{
				if( pushed )
				{
					//cout << "BLUE STAYS AT " << blue << "\n";
				}
				else
				{
					if( d.pos < d2.pos || d2.pos == -1) // wait for BLUE
					{
						deleteNext(vec, BLUE);
						//cout << "BLUE PUSHES " << d.value << "\n";
					}
					else
						;//cout << "BLUE STAYS AT " << blue << "\n";
				}
			}
		}
		else
			;//cout << "BLUE STAYS AT " << blue << "\n";

		pushed = false; // reset false
		++counter;

		//printArray(table, SZ);
		//cout << "orange: " << orange << "\tblue = " << blue << "\n";
		//cout << "time: " << counter << "s\n";

		//cin.get();
	}

	//cout << "time: " << counter - 1;

	return counter - 1;
}

void readFromFile(ifstream &in, vector<string> &vec)
{
	int positions;
	in >> positions; // number of positions

	string s1, s2;

	for(int i = 0; i < positions; ++i)
	{
		in >> s1;
		in >> s2;
		s1 += s2;
		vec.push_back(s1);
	}
}