#include <fstream>
#include <iostream>
#include <string>
#include "terrain.h"

using std::string;
using std::cout;
using std::endl;
using std::ifstream;
using std::ofstream;

int main(int argc, char **argv)
{
	/*
	int ter[] = {1, 2, 3,
		     4, 5, 6,
		     7, 8, 1};

	terrain t(3, 3, ter);

	t.prune();
	t.print_heights();
	t.print_drains();

	*/

	ifstream infile(argv[1]);
	//ofstream outfile(argv[2]);

	int t;
	string s;

	infile >> t;

	for (int i = 0; i < t; i++)
	{
		cout << "Case #" << i + 1 << ":" << endl;
		int w, h;

		infile >> h;
		infile >> w;

		int *ter = new int[w*h];

		for (int j = 0; j < w*h; j++)
		{
			infile >> ter[j];
		}

		terrain t(w, h, ter);
		t.prune();
		//t.print_heights();
		t.print_drains();

		delete ter;
	}
}
