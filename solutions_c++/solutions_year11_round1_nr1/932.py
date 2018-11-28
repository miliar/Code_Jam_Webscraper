// BEGIN CUT HERE
// PROBLEM STATEMENT
// Taro and Brus are playing a new game called Square Series. The game involves 
// placing a non-empty sequence of black and white squares following a couple of 
// rules:
// 
// The first square has side length 1.
// For i > 1, if the color of square i (1-indexed) is different than the color of 
// square i-1, its side length will be equal to the side length of the previous 
// square plus 1. If the colors are the same, then the side length will be equal 
// to the previous side length minus 1. Note that  a side length of 0 would make 
// the shape not a square, so it is not legal to repeat the color after a length 
// 1 square.
// 
// 
// Taro wants to prepare new challenges for Brus and would like you to make a 
// program that will generate valid square series such that it matches  string 
// pattern and the length of the last square is equal to lastLength. The pattern 
// contains 'W' and 'B' representing white and black squares respectively and 
// exactly one '?' character. To generate a sequence of strings that matches the 
// pattern, replace the '?' character with a (possibly empty) sequence of white 
// and black squares.
// 
// Given the pattern and lastLength, if there is no valid sequence of squares 
// that follows the aforementioned rules, matches the pattern and finishes with a 
// square of side length equal to lastLength, then return "..." (quotes for 
// clarity). Otherwise, return the shortest possible sequence that matches the 
// pattern and finishes with a square of  the appropriate side length. In case 
// there is more than one sequence with a length equal to the shortest possible, 
// return the lexicographically first of them.
// 
// DEFINITION
// Class:SquareSeries
// Method:completeIt
// Parameters:string, int
// Returns:string
// Method signature:string completeIt(string pattern, int lastLength)
// 
// 
// NOTES
// -The lexicographically earlier of two strings of the same length is the one 
// that has the earlier character (using ASCII ordering) at the first position at 
// which they differ.
// 
// 
// CONSTRAINTS
// -lastLength will be between 1 and 100, inclusive.
// -pattern will contain between 1 and 50 characters, inclusive.
// -Each character in pattern will be 'W', 'B' or '?'.
// -pattern will contain exactly one '?' character.
// 
// 
// EXAMPLES
// 
// 0)
// "W?B"
// 2
// 
// Returns: "WB"
// 
// It is possible to replace the '?' character with an empty sequence. The 
// sequence "WB" is the shortest one that matches the pattern and ends with a 
// square of length 2.
// 
// 1)
// "?"
// 5
// 
// Returns: "BWBWB"
// 
// Any sequence can match the "?" pattern. "BWBWB" and "WBWBW" are the shortest 
// sequences possible that end with a square of size 5. "BWBWB" is the 
// lexicographically earlier of the two.
// 
// 
// 2)
// "BWBBBBW?WB"
// 10
// 
// Returns: "..."
// 
// Every sequence that begins with BWBBBB is invalid because it will require an 
// invalid square of size 0 at position 6 (1-based).
// 
// 3)
// "BWBWBW?WBWBWBW"
// 15
// 
// Returns: "BWBWBWBBWBWBWBWBW"
// 
// 
// 
// 4)
// "WBWBWBWBWBWWBB?W"
// 1
// 
// Returns: "WBWBWBWBWBWWBBBBBBBBBBBWW"
// 
// 
// 
// 5)
// "?WBWBWBBB"
// 3
// 
// Returns: "..."
// 
// 
// 
// END CUT HERE
#include <algorithm>
#include <functional>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
#include <cmath>
#include <queue>
#include <map>
#include <set>

using namespace std;

#define VT vector
typedef VT<int> VI;
typedef VT<VI> VVI;
typedef VT<string> VS;
typedef VT<double> VD;
#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define ALL(c) c.begin(),c.end()
#define PB push_back
#define MP make_pair
#define FS first
#define SC second
#define SZ size() 


bool calc(long long N, long long PD, long long PG)
{
	if (PD == 0)
	{
		return PG < 100;
	}

	if (PD == 100)
	{
		return PG > 0;
	}

	if (PG == 100)
	{
		return PD == 100;
	}

	if (PG == 0)
	{
		return PD == 0;
	}

	if (N >= 100)
		return true;

	for(int d = 1; d <= N; ++d)
	{
		if (d*PD %100 == 0)
		{
			return true;
		}
	}

	return false;
}
	

int main(int argc, char* argv[])
{

	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T;
	cin >> T;
	REP(t, T)
	{
		long long N, PG, PD;
		cin >> N >> PD >> PG;

		if (calc(N, PD, PG))
		{
			cout << "Case #" << (t+1) << ": Possible\n";
		}
		else
		{
			cout << "Case #" << (t+1) << ": Broken\n";
		}


	}


	int Int;
	std::cin >> Int;
}