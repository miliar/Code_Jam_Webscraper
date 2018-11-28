// gcc version 4.6.1 (tdm-1)
// g++ -I tr1 femidav.cpp -O2 -Wall -std=c++0x -o femidav.exe
// femidav < small-attempt0.in > small-attempt0.out
// femidav < large.in > large.out

#include <cstdio>
#include <iostream>
#include <string>

#define FOR(I, N) for( int I = 0, end_ = (N); I < end_; ++I )
int rin() { int r; scanf( "%d\n", &r ); return r; }
std::string const rline() { std::string r; getline(std::cin, r); return r; }

int main()
{
	char const * const T = "yhesocvxduiglbkrztnwjpfmaq";
    FOR(i, rin())
    {
		std::string line = rline();
		FOR(j, line.length())
			if (line[j] != ' ')
				line[j] = T[line[j] - 'a'];

        printf("Case #%d: %s\n", i + 1, line.c_str());
    }
}