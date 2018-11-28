#include <iostream>
#include <string>
#include <sstream>
#include <list>
#include <vector> 
#include <algorithm> 

using namespace std;

#define CASE(x) "Case #" << x << ": " 
#define TIME_PARSE(str) ((int)(str[0]-'0')*10+(int)(str[1]-'0'))*60+(int)(str[3]-'0')*10+(int)(str[4]-'0'))

string linebuf; 
#define cinline getline(cin, linebuf);\
		stringstream(linebuf)

void process_case()
{
    int S, Q;
    int Switch = 0; 
    string Name; 
    list<string> Engines, SearchList;  
    cinline >> S; 
    for (int j = 0; j<S; j++)
    {
	getline(cin, Name); 
	Engines.push_back(Name); 
    }
    cinline >> Q; 
    SearchList.assign(Engines.begin(), Engines.end()); 
    for (int k = 0; k<Q; k++)
    {
	getline(cin, Name); 
	SearchList.remove(Name); 
	if (SearchList.empty()) {
	    Switch++; 
	    SearchList.assign(Engines.begin(), Engines.end()); 
	    SearchList.remove(Name); 
	}

    }
    cout << Switch; 
}

int main(int argc, char* argv[])
{
    int cases; 
    cinline >> cases;  
    for (int i = 1; i <= cases; i++) {
	cout << CASE(i); 
	process_case();
	cout << endl; 
    }
}
