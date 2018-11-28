//#include <boost/thread/thread.hpp>
#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <string>
#include <assert.h>

using namespace std;

struct Field
{
	static const int SIZE_X = 4;
	static const int SIZE_Y = 4;

	vector<char> data;

	Field() : data(SIZE_X*SIZE_Y){}

	char& get(int x, int y)
	{
		if (x < 0 || y< 0 || x>=SIZE_X || y>=SIZE_Y)
		{
			cout << "bad []" << x << " " << y << endl;
			throw exception();
		}

		return data[y*SIZE_X + x];
	};

	struct Detector
	{
		int t_count, player_count;
		char player;
		vector<char> v;
		Detector(char player) : player(player), t_count(0), player_count(0), v(Field::SIZE_X){}
		void put(char ch)
		{
			if ( ch == 'T')
				t_count++;
			else
				if (ch == player)
					player_count++;
		}

		bool match() const
		{
			return player_count == SIZE_X || (player_count == SIZE_X -1 && t_count == 1);
		}
	};

	bool won(char ch) 
	{
		for (int i=0; i<SIZE_Y; i++)
		{
			Detector d1(ch), d2(ch);
			for (int j=0; j<SIZE_X; j++)
			{
				d1.put(get(i, j));
				d2.put(get(j, i));
			}
			if (d1.match() || d2.match())
				return true;
		}

		Detector diag1(ch), diag2(ch);
		for (int i=0; i<SIZE_X; i++)
		{
			diag1.put(get(i, i));
			diag2.put(get(SIZE_X - i -1, i));
		}

		return diag1.match() || diag2.match();
	}

	bool draw() const
	{
		for (size_t i=0; i<data.size(); i++)
			if (data[i] == '.')
				return false;
		return true;
	}

} field;

void main()
{
	ifstream f;
	f.open("in.txt");
	if (f.fail())
	{
		cout << "cannot open file" << endl;
		return;
	}

	int cases = 0;
	f >> cases;
	for (int _case=1; _case<=cases; _case++)
	{
		string s;
		getline(f, s);
		for (int y =0; y<Field::SIZE_Y; y++)
		{
			getline(f, s);
			if (s.length() < Field::SIZE_X)
			{
				cout << "bad data" << endl;
				throw exception();
			}
			for (int i=0; i<Field::SIZE_X; i++)
				field.get(i, y) = s[i];
		}

		cout << "Case #" << _case << ": ";
		if (field.won('X'))
			cout << "X won";
		else
			if (field.won('O'))
				cout << "O won";
			else
				if (field.draw())
					cout << "Draw";
				else
					cout << "Game has not completed";

		cout << endl;
	}
}
