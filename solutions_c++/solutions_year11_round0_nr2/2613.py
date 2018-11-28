// gcc version 4.5.0 (tdm-1)
// g++ -I tr1 femidav.cpp -O2 -Wall -fpermissive -o femidav.exe
// femidav < A-small-attempt0.in > A-small-attempt0.out
// femidav < A-large.in > A-large.out

#include <cstdio>
#include <map>
#include <iostream>
#include <string>

#define FOR(I, N) for( int I = 0, end_ = (N); I < end_; ++I )
int ri() { int r; scanf("%d", &r); return r; }
std::string const rs() { std::string r; std::cin >> r; return r; }

struct Element
{
	Element() : self(' '), combine(' '), combined(' '), opposed(' ') {}
	Element(char s_, char c_, char d_, char o_ = ' ') : self(s_), combine(c_), combined(d_), opposed(o_) {}
	char self;
	char combine;
	char combined;
	char opposed;
};

int main()
{
	int T = ri();
	FOR(i, T)
	{
		std::map<char, Element> e;

		int C = ri();
		FOR( j, C )
		{
			std::string s = rs();
			e[ s[0] ] = Element(s[0], s[1], s[2]);
			e[ s[1] ] = Element(s[1], s[0], s[2]);
		}

		int D = ri();
		FOR( k, D)
		{
			std::string s = rs();
			if ( e.find(s[0]) != e.end() )
				e[ s[0] ].opposed = s[1];
			else
				e[ s[0] ] = Element(s[0], ' ', ' ', s[1]);

			if ( e.find(s[1]) != e.end() )
				e[ s[1] ].opposed = s[0];
			else
				e[ s[1] ] = Element(s[1], ' ', ' ', s[0]);
		}

		ri();
		std::string input = rs();
		std::string result;
		FOR( l, input.size() )
		{
			char next = input[l];
			if ( !result.size() || e.find(next) == e.end() )
				result += next;
			else if ( *result.rbegin() == e[next].combine || ( e.find(*result.rbegin()) != e.end() && next == e[*result.rbegin()].combine ) )
				result[result.size() - 1] = e[next].combined;
			else if ( result.find( e[next].opposed ) != std::string::npos )
				result = "";
			else
				result += next;
		}

		printf("Case #%d: [", i + 1);
		FOR(m, result.size())
			m == 0 ? printf("%c", result[m]) : printf(", %c", result[m]);
		printf("]\n");
	}
}

