#include <cstdlib>
#include <iostream>
#include <iostream>
#include <fstream>
#include <vector>
#include <cstdlib>
#include <algorithm>

using namespace std;

int my_count;

/*
pseudocode
find character(sin,welcome)
if welcome[0] found in sin
{
   if welcome.size() != 1
    find(sin(where_welcome_found, end),welcome(1,end)) 
   else
     count++
     find (sin(where_welcome_found,end),welcome(0))
}
*/


void find_pattern(string sin, string pattern)
{
     size_t found;
     found = sin.find(pattern[0]);
     if (found != string::npos)
     {
        if (pattern.size() == 1)
        {
            if (my_count == 9999) my_count = 0;
            else my_count++;
        }           
        find_pattern(sin.substr(found+1),pattern);
        find_pattern(sin.substr(found+1),pattern.substr(1));
     }
}

int main(int argc, char *argv[])
{
	ifstream infile;
    int N;
    string line;
    string welcome("welcome to code jam");

	infile.open(argv[1]);
	if (!infile)
	{
	   cout << "Invalid file name" << endl;
	   exit(1);
	}
    infile >> N;
    infile.get(); // '\n'
	for (int i=0; i < N; i++)
	{
        my_count = 0;
        getline(infile, line);
        find_pattern(line,welcome);
		cout << "Case #" << i+1 << ": ";
        cout.width(4);
        cout.fill('0');
        cout << my_count << endl;
    }

    return EXIT_SUCCESS;
}
