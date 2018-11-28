#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

int T;

struct Cell
{
	int Alt, X, Y;
	char Label;
};

bool cellCompare(Cell *c1, Cell *c2)
{
	if (c1->Alt == c2->Alt)
	{
		if (c1->Y == c2->Y)
			return c1->X < c2->X;
		else
			return c1->Y < c2->Y;
	}
	else
		return c1->Alt > c2->Alt;
}

void unify(Cell *field, int H, int W, Cell *cell, char c)
{
	char oldColor = cell->Label;
	cell->Label = c;
	if ((cell->Y - 1) >= 0 && field[(cell->Y - 1) * W + cell->X].Label == oldColor)
		unify(field, H, W, &field[(cell->Y - 1) * W + cell->X], c);
	if ((cell->X - 1) >= 0 && field[cell->Y * W + cell->X - 1].Label == oldColor)
		unify(field, H, W, &field[cell->Y * W + cell->X - 1], c);
	if ((cell->X + 1) < W && field[cell->Y * W + cell->X + 1].Label == oldColor)
		unify(field, H, W, &field[cell->Y * W + cell->X + 1], c);
	if ((cell->Y + 1) < H && field[(cell->Y + 1) * W + cell->X].Label == oldColor)
		unify(field, H, W, &field[(cell->Y + 1) * W + cell->X], c);
}

void paint(Cell *field, int H, int W, Cell *cell, char &c)
{
	cell->Label = c;
	int dx = 0, dy = 0, minAlt = cell->Alt;

	// North
	if ((cell->Y - 1) >= 0 && field[(cell->Y - 1) * W + cell->X].Alt < minAlt)
		{ dx = 0; dy = -1; minAlt = field[(cell->Y - 1) * W + cell->X].Alt; }

	// West
	if ((cell->X - 1) >= 0 && field[cell->Y * W + cell->X - 1].Alt < minAlt)
		{ dx = -1; dy = 0; minAlt = field[cell->Y * W + cell->X - 1].Alt; }

	// East
	if ((cell->X + 1) < W && field[cell->Y * W + cell->X + 1].Alt < minAlt)
		{ dx = +1; dy = 0; minAlt = field[cell->Y * W + cell->X + 1].Alt; }

	// South
	if ((cell->Y + 1) < H && field[(cell->Y + 1) * W + cell->X].Alt < minAlt)
		{ dx = 0; dy = +1; minAlt = field[(cell->Y + 1) * W + cell->X].Alt; }

	if (dx != 0 || dy != 0)
	{
		if (field[(cell->Y + dy) * W + cell->X + dx].Label != 0)
		{
			unify(field, H, W, cell, field[(cell->Y + dy) * W + cell->X + dx].Label);
			c--;
		}
		else
			paint(field, H, W, &field[(cell->Y + dy) * W + cell->X + dx], c);
	}
}

int main(int argc, char **argv)
{
	if (argc < 2) { cerr << "Please give input file name as parameter"; return 0; }

	ifstream input(argv[1]);
	if (input.bad()) { cerr << "Please give CORRECT input file name as parameter"; return 0; }
	ofstream output("output.out");
	if (output.bad()) { cerr << "Cannot create output file"; input.close(); return 0; }

	int H, W;
	vector<Cell *> sortedCells;

	input >> T;
	char *letters = new char[26];

	for (int i = 0; i < T; i++)
	{
		input >> H >> W;

		sortedCells.clear();

		Cell *field = new Cell[H * W];
		for (int j = 0; j < H * W; j++)
		{
			input >> field[j].Alt;
			field[j].Label = 0;
			field[j].X = j % W;
			field[j].Y = j / W;
			sortedCells.insert(sortedCells.end(), &field[j]);
		}
		sort(sortedCells.begin(), sortedCells.end(), cellCompare);

		char c = 1;
		for (int j = 0; j < H * W; j++)
		{
			if (sortedCells[j]->Label == 0)
			{
				paint(field, H, W, sortedCells[j], c);
				c++;
			}
		}

		for (int j = 0; j < 26; j++)
			letters[j] = 0;

		char currentLetter = 'a';

		// Write result
		cout << "Case " << (i + 1) << " of " << T << endl;
		output << "Case #" << (i + 1) << ":" << endl;
		for (int j = 0; j < H; j++)
		{
			for (int k = 0; k < W; k++)
			{
				if (letters[field[j * W + k].Label - 1] == 0)
				{
					letters[field[j * W + k].Label - 1] = currentLetter;
					currentLetter++;
				}
				output << letters[field[j * W + k].Label - 1];
				if (k < (W - 1))
					output << " ";
				else
					output << endl;
			}
		}

		delete [] field;
	}
	delete [] letters;

	input.close();
	output.close();
	cin.get();
	return 0;
}