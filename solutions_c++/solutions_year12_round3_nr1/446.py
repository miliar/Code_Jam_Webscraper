
//#define _SECURE_SCL 0
//#define _HAS_ITERATOR_DEBUGGING 0

#include <iostream>
#include <fstream>
#include <strstream>
#include <sstream>
#include <list>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <iomanip>
#include <memory.h>

using namespace std;

inline istream& eatwhite(istream& is)
{
	char c;
	while(!is.eof() && is.get(c))
	{
//		if (!isspace(c))
		if (c != ' ' && c != 0xA && c != 0xD && c != '\t')
		{
			is.putback(c);
			break;
		}
	}
	return is;
}

#define assert(v)  if(!(v)) {int*a=0;*a=1;}

#define mymin(a,b)  ((a)<(b)?(a):(b))
#define mymax(a,b)  ((a)>(b)?(a):(b))

ifstream my_fin;
ofstream my_fout;
bool my_fin_initialized = false;
bool my_fout_initialized = false;

inline void set_fio(const char* file_in, const char* file_out)
{
	//extern ifstream my_fin;
	//extern ofstream my_fout;

	my_fin.open(file_in);
	my_fout.open(file_out);
	my_fin_initialized = true;
	my_fout_initialized = true;
}

inline void set_fio(const char* file_in)
{
	//extern ifstream my_fin;
	//extern ofstream my_fout;

	my_fin.open(file_in);
	my_fin_initialized = true;
}

inline basic_istream<char, char_traits<char> >& get_myfin()
{
	if (my_fin_initialized)
		return my_fin;
	else
		return cin;
}

inline basic_ostream<char, char_traits<char> >& get_myfout()
{
	if (my_fout_initialized)
		return my_fout;
	else
		return cout;
}

#define fin get_myfin()
#define fout get_myfout()
