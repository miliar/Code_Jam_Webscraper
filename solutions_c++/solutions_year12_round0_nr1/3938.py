#include<iostream>
#include<cstdio>
#include<fstream>
#include<cstdlib>
#include<vector>
#include<map>
#include<algorithm>

#define forn(i,n) 	 for(int i=0; i<n; i++)
#define fornd(i,n) 	 for(int i=n-1; i>=0; i--)
#define fornx(i,x,n) for(int i=x; i<n; i++)

using namespace std;

int main(int argc, char** argv)
{
	/* Define the mapping. .*/
    
    map<char, char> conversion;
    
    conversion['a'] = 'y';
    conversion['b'] = 'h';
    conversion['c'] = 'e';
    conversion['d'] = 's';
    conversion['e'] = 'o';
    conversion['f'] = 'c';
    conversion['g'] = 'v';
    conversion['h'] = 'x';    
    conversion['i'] = 'd';
    conversion['j'] = 'u';
    conversion['k'] = 'i';
    conversion['l'] = 'g';    
    conversion['m'] = 'l';
    conversion['n'] = 'b';
    conversion['o'] = 'k';    
    conversion['p'] = 'r';
    conversion['q'] = 'z';    
    conversion['r'] = 't';
    conversion['s'] = 'n';
    conversion['t'] = 'w';
    conversion['u'] = 'j';    
    conversion['v'] = 'p';
    conversion['w'] = 'f';
    conversion['x'] = 'm';    
    conversion['y'] = 'a';
    conversion['z'] = 'q';
    // Faltan: q z Los pongo como que quedan igual
    
    ifstream entrada("A-small-1.in");
	ofstream salida("A-small-1.out");
	
	int casos;
	entrada >> casos;
	
    string s;
    
    std::getline(entrada, s);
	forn(caso, casos)
	{        
        std::getline(entrada, s);        
        string res (s.length(), ' ');
        
        forn(i, s.length())
        {
            if (s[i] != ' ') 
                res[i] = conversion[s[i]];
        }
            
        salida << "Case #" << caso + 1 << ": " << res << endl;
	}
	
	return 0;	
}
