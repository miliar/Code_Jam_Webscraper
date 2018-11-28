#include <iostream>
#include <fstream>
#include <vector>

using namespace std;


std::vector <char> 
	make_map () 
{
	ifstream in_map = ifstream ("in_map.txt");
	ifstream out_map = ifstream ("out_map.txt");

	char i;
	char o;
	int lines;
	
	// ascii begin
	int shift = 97;
	
	// letter count
	int letter_count = 26;

	// unknown mapping
	char unknown = '-';

	// result map
	std::vector <char> map_vector;
	map_vector.resize (letter_count, '-');

	// already know these
	map_vector ['a' - shift] = 'y';
	map_vector ['o' - shift] = 'e';
	map_vector ['z' - shift] = 'q';

	while (in_map.good () && out_map.good ())
	{
		in_map >> i;
		out_map >> o;

		if (in_map.good () && out_map.good ())
		{
			int index = ((int)(i) - shift);
			map_vector [index] = o;
		}
	}

	in_map.close ();
	out_map.close ();

	/*	
	// unknown mapping
	for (int i = 0; i < map_vector.size (); i++) 
	{
		if (map_vector [i] == unknown)
			cout << "unknown " << (char)(i + shift) << endl;
	}

	// unused mapping
	std::vector <bool> used_vector;
	used_vector.resize (letter_count, 0);
	for (int i = 0; i < map_vector.size (); i++) 
	{
		if (map_vector [i] != unknown)
			used_vector [map_vector [i] - shift] = 1;
	}
	for (int i = 0; i < map_vector.size (); i++) 
	{
		if (used_vector [i] == 0)
			cout << "unused " << (char)(i + shift) << endl;
	}*/

	// this was unknown and unused after first run
	map_vector ['q' - shift] = 'z';	

	// print
	for (int i = 0; i < map_vector.size (); i++) 
	{
		cout << (char)(i + shift) << " -> " << map_vector [i] << endl;
	}

	return map_vector;
}


#define LINE_SIZE 111

void
	translate (const std::vector <char> map)
{
	ifstream in = ifstream ("in.txt");
	ofstream out = ofstream ("out.txt");

	int line_count; 
	in >> line_count;

	int letter_begin = 97;
	int letter_end = 122;

	// skip line with case count
	char line [LINE_SIZE];
	in.getline (line, LINE_SIZE);

	for (int i = 1; i <= line_count; i++)
	{
		in.getline (line, LINE_SIZE);
		int j = 0;

		while (line [j] != '\0')
		{
			if (line [j] >= letter_begin && line [j] <= letter_end)
			{
				line [j] = map [line [j] - letter_begin]; 
			}
			j++;
		}

		cout << "Case #" << i << ": " << line << endl;
		out << "Case #" << i << ": " << line << endl;
	}

	in.close ();
	out.close ();
}


int 
	main () 
{
	std::vector <char> map = make_map ();
	
	translate (map);

	system ("pause");
}
