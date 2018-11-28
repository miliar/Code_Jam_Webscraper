#include <vector>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <functional>
#include <map>
#include <math.h>
#include <iomanip>

using namespace std;
typedef unsigned long long int ui;
#define PI M_PI

char ex(char in)
{
    if (in == 'y') {
        return 'a';
    } else if (in == 'n') {
        return 'b';
    } else if (in == 'f') {
        return 'c';
    } else if (in == 'i') {
        return 'd';
    } else if (in == 'c') {
        return 'e';
    } else if (in == 'w') {
        return 'f';
    } else if (in == 'l') {
        return 'g';
    } else if (in == 'b') {
        return 'h';
    } else if (in == 'k') {
        return 'i';
    } else if (in == 'u') {
        return 'j';
    } else if (in == 'o') {
        return 'k';
    } else if (in == 'm') {
        return 'l';
    } else if (in == 'x') {
        return 'm';
    } else if (in == 's') {
        return 'n';
    } else if (in == 'e') {
        return 'o';
    } else if (in == 'v') {
        return 'p';
    } else if (in == 'z') {
        return 'q';
    } else if (in == 'p') {
        return 'r';
    } else if (in == 'd') {
        return 's';
    } else if (in == 'r') {
        return 't';
    } else if (in == 'j') {
        return 'u';
    } else if (in == 'g') {
        return 'v';
    } else if (in == 't') {
        return 'w';
    } else if (in == 'h') {
        return 'x';
    } else if (in == 'a') {
        return 'y';
    } else if (in == 'q') {
        return 'z';
    }
    
    return ' ';
}

int main()
{
	ifstream ifp("./A-small-attempt0.in");
	//ifstream ifp("./test.txt");
	ofstream ofp("./output.txt");
	
    int T;
    
	ifp >> T;
	cout << "testcase : " << T << endl;
	for (int i = 0; i < T; i++)
	{
        char buf[2048];
        char _buf[2048];
        int j = 0;
        
        do {
           ifp.getline(buf, 2048); 
        } while (strlen(buf) == 0);
        
        while (buf[j] != '\0')
        {
            _buf[j] = ex(buf[j]);
            
            j++;
        }
        _buf[j] = '\0';
        
        
        
		ofp << "Case #" << i+1 << ": " << _buf << endl;
        
		cout << "Case #" << i+1 << ": " << _buf << endl;
	}
}


