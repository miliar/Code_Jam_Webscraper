
#include <iostream>
#include <cstdio>
using namespace std;


#define DIR_X	0
#define DIR_N	1
#define DIR_E	2
#define DIR_S	3
#define DIR_W	4




unsigned long worldw;
unsigned long worldh;


typedef struct
{
	unsigned char label;
	unsigned long altitude;
	bool sink;

} cell;

cell world[100][100];
char labels[30];



bool is_nothing(unsigned long w, unsigned long h, unsigned long dir);



inline unsigned long get_altitude(unsigned long w, unsigned long h, unsigned long dir)
{
	if (is_nothing(w,h,dir)) {
		return 0xFFFFFFFF;
	}


	switch (dir) {
		case DIR_N: h -= 1; break;
		case DIR_E: w += 1; break;
		case DIR_S: h += 1; break;
		case DIR_W: w -= 1; break;
	}

	return world[w][h].altitude;
}


inline bool get_sink(unsigned long w, unsigned long h, unsigned long dir)
{
	switch (dir) {
		case DIR_N: h -= 1; break;
		case DIR_E: w += 1; break;
		case DIR_S: h += 1; break;
		case DIR_W: w -= 1; break;
	}

	return world[w][h].sink;
}


inline char get_label(unsigned long w, unsigned long h, unsigned long dir)
{
	switch (dir) {
		case DIR_N: h -= 1; break;
		case DIR_E: w += 1; break;
		case DIR_S: h += 1; break;
		case DIR_W: w -= 1; break;
	}

	return world[w][h].label;
}


inline bool is_nothing(unsigned long w, unsigned long h, unsigned long dir)
{
	switch (dir) {
		case DIR_N: h -= 1; break;
		case DIR_E: w += 1; break;
		case DIR_S: h += 1; break;
		case DIR_W: w -= 1; break;
	}

	return !((w < worldw) && (h < worldh));
}


inline bool is_sink(unsigned long w, unsigned long h, unsigned long dir = DIR_X)
{

	if (!is_nothing(w, h, DIR_N) && (get_altitude(w, h, DIR_N) < get_altitude(w,h, DIR_X))) {
		return false;
	}
	if (!is_nothing(w, h, DIR_E) && (get_altitude(w, h, DIR_E) < get_altitude(w,h, DIR_X))) {
		return false;
	}
	if (!is_nothing(w, h, DIR_S) && (get_altitude(w, h, DIR_S) < get_altitude(w,h, DIR_X))) {
		return false;
	}
	if (!is_nothing(w, h, DIR_W) && (get_altitude(w, h, DIR_W) < get_altitude(w,h, DIR_X))) {
		return false;
	}

	return true;
}



char find_nearest_sink(unsigned long w, unsigned long h)
{

	/*
	// Next to
	if (!is_nothing(w,h,DIR_N) && get_sink(w,h,DIR_N)) {
		return get_label(w,h,DIR_N);
	}
	if (!is_nothing(w,h,DIR_E) && get_sink(w,h,DIR_E)) {
		return get_label(w,h,DIR_E);
	}
	if (!is_nothing(w,h,DIR_S) && get_sink(w,h,DIR_S)) {
		return get_label(w,h,DIR_S);
	}
	if (!is_nothing(w,h,DIR_W) && get_sink(w,h,DIR_W)) {
		return get_label(w,h,DIR_W);
	}

	*/


	if (world[w][h].sink) {
		return world[w][h].label;
	}


	// Try north
	if (!is_nothing(w,h, DIR_N)) {
		if (
		 (get_altitude(w,h,DIR_N) <= get_altitude(w,h,DIR_E)) &&
		 (get_altitude(w,h,DIR_N) <= get_altitude(w,h,DIR_S)) &&
		 (get_altitude(w,h,DIR_N) <= get_altitude(w,h,DIR_W))) {
			 return find_nearest_sink(w,h-1);
		}
	}



	// Try west
	if (!is_nothing(w,h,DIR_W)) {
		if (
		 (get_altitude(w,h,DIR_W) <= get_altitude(w,h,DIR_N)) &&
		 (get_altitude(w,h,DIR_W) <= get_altitude(w,h,DIR_E)) &&
		 (get_altitude(w,h,DIR_W) <= get_altitude(w,h,DIR_S))) {
			 return find_nearest_sink(w-1,h);
		}
	}

	// Try east
	if (!is_nothing(w,h,DIR_E)) {
		if (
		 (get_altitude(w,h,DIR_E) <= get_altitude(w,h,DIR_N)) &&
		 (get_altitude(w,h,DIR_E) <= get_altitude(w,h,DIR_S)) &&
		 (get_altitude(w,h,DIR_E) <= get_altitude(w,h,DIR_W))) {
			 return find_nearest_sink(w+1,h);
		}
	}

	// Try south
	if (!is_nothing(w,h,DIR_S)) {
		if (
		 (get_altitude(w,h,DIR_S) <= get_altitude(w,h,DIR_N)) &&
		 (get_altitude(w,h,DIR_S) <= get_altitude(w,h,DIR_E)) &&
		 (get_altitude(w,h,DIR_S) <= get_altitude(w,h,DIR_W))) {
			 return find_nearest_sink(w,h+1);
		}
	}




	// Whot?
	return -1;
}






int main(int argc, char* argv[])
{
	unsigned long cases = 0;
	cin >> cases;

	for (unsigned long i = 0; i < cases; i++) {

		cin >> worldh;
		cin >> worldw;

		for (int j=0; j < 30; j++) {
			labels[j] = 0;
		}


		if (i == 12) {
			int x = 0;
		}
		for (unsigned long h=0; h < worldh; h++) {
			for (unsigned long w=0; w < worldw; w++) {
				cin >> world[w][h].altitude;
				world[w][h].label = 0;
				world[w][h].sink = false;
			}
		}


		// Mark and label all the sinks
		char label = 0;
		for (unsigned long w=0; w < worldw; w++) {
			for (unsigned long h=0; h < worldh; h++) {

				if (is_sink(w,h)) {
					world[w][h].sink = true;
					world[w][h].label = label;
					label++;
				}
			}
		}


		// Label, and print
		for (unsigned long h=0; h < worldh; h++) {
			for (unsigned long w=0; w < worldw; w++) {
				if (!is_sink(w,h)) {
					world[w][h].label = find_nearest_sink(w,h);
				}
			}
		}



		// Label, and print
		char l = 'a';
		cout << "Case #" << (i+1) << ":" << endl;
		for (unsigned long h=0; h < worldh; h++) {
			for (unsigned long w=0; w < worldw; w++) {
				if (labels[world[w][h].label] == 0) {
					labels[world[w][h].label] = l;
					l++;
				}

				if (w > 0) {
					cout << ' ';
				}

				cout << labels[world[w][h].label];

			}
			cout << endl;
		}

	}	

	return 0;
}
