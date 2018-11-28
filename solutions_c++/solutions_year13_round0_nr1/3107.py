// Code Jam 2013 qualifier
// Problem A
// Author: intrepid
//
// The Boost library was used. You can get it at www.boost.org.
// Boost source: http://sourceforge.net/projects/boost/files/boost/1.46.1

#include <iostream>
#include <utility>
#include <array>
#include <algorithm>
#include <iterator>
using namespace std;

class Line
{
public:
	typedef array<char,4> data_t;
	Line(data_t data) : data_(data) {}
	Line(char data[4]) { copy(data, data+4, data_.begin()); };
	Line(char a, char b, char c, char d)
	{
		data_[0] = a; data_[1] = b; data_[2] = c; data_[3] = d;
	}
	
	char winner() {
		char curChar = data_[0];
		for (int i=1; i < 4; ++i) {
			char testChar = data_[i];
			if ( curChar == 'T' ) curChar = testChar;
			if ( testChar != 'T' && testChar != curChar || curChar == '.' ) {
				curChar = 0;
				break;
			}
		}

		return curChar;
	}
private:
	data_t data_;
};

class Board
{
public:
	typedef array<char,16> data_t;
	Board(data_t data) : data_(data) {}
	
	Line getRow(size_t index)
	{
		size_t offset = index * 4;
		return Line(&data_[offset]);
	}
	
	Line getCol(size_t index)
	{
		return Line(data_[index], data_[index+4], data_[index+8], data_[index+12]);
	}
	
	Line getDiag(bool upperRight)
	{
		if ( upperRight ) return Line(data_[12], data_[9], data_[6], data_[3]);
		else return Line(data_[0], data_[5], data_[10], data_[15]);
	}
	
	bool isFull()
	{
		return ( find(data_.begin(), data_.end(), '.') == data_.end() );
	}

private:
	data_t data_;
};

// Returns (Row, Col)
pair<size_t, size_t> getRowCol(size_t pos)
{
	size_t row = pos / 4;
	size_t col = pos % 4;
	return make_pair(row,col);
}


int main()
{
	int numTests = 0;
	cin >> numTests;
	cerr << "Running " << numTests << " tests.\n";
	
	for (int i=0; i < numTests; ++i) {
		Board::data_t data;
		for_each(data.begin(), data.end(), [] (char& d) { cin >> d; });
		//copy(data.begin(), data.end(), ostream_iterator<char>(cerr, ""));
		if ( !cin ) {
			cerr << "Unexpected end of stream\n";
			return 1;
		}
		
		cout << "Case #" << i + 1 << ": ";
		Board board(data);
		char winner = '\0';
		for (int row=0; row < 4; ++row) {
			if ( winner = board.getRow(row).winner() ) {
				break;
			}
		}
		if ( !winner ) {
			for (int col=0; col < 4; ++col) {
				if ( winner = board.getCol(col).winner() ) {
					break;
				}
			}
		}
		if ( !winner ) winner = board.getDiag(false).winner();
		if ( !winner ) winner = board.getDiag(true).winner();
		
		if ( winner ) {
			cout << winner << " won\n";
		}
		else if ( board.isFull() ) {
			cout << "Draw\n";
		}
		else {
			cout << "Game has not completed\n";
		}
	}

	cerr << "Done.\n";
	
	return 0;
}
