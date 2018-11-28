// vim:ts=4:sw=4:cindent:
#include "base.hh"

#define check(where, y, x) { \
	debug("Looking %s of %d, %d\n", where, x, y); \
	if (elevation[(y) * W + (x)] < lowest) { \
		debug("The elevation %s of here is %d, lower than %d\n", where, elevation[(y) * W + (x)], lowest); \
		low_y = y; \
		low_x = x; \
		lowest = elevation[(y) * W + (x)]; \
		ret = true; \
	} \
}

bool find_lowest(int H, int W, int *elevation, int& locy, int& locx)
{
	int lowest = elevation[locy * W + locx];
	int low_y = locy;
	int low_x = locx;
	bool ret = false;

	// Check north.
	if (locy > 0) check("north", locy - 1, locx);

	// Check west.
	if (locx > 0) check("west", locy, locx - 1);

	// Check east.
	if (locx < W - 1) check("east", locy, locx + 1);

	// Check south.
	if (locy < H - 1) check("south", locy + 1, locx);

	locy = low_y;
	locx = low_x;
	return ret;
}

void evaluate_map(const int H, const int W, int *elevation, char *sink)
{
	for (int y = 0; y < H; y++) {
		for (int x = 0; x < W; x++) {
			sink[y * W + x] = 0;
		}
	}

	char next = 'a';

	vector<char *> related;

	for (int y = 0; y < H; y++) {
		for (int x = 0; x < W; x++) {
			related.clear();
			related.push_back(sink + (y * W + x));
			debug("\nSelf address %d, %d\n", x, y);

			int move_y = y, move_x = x;
			while (find_lowest(H, W, elevation, move_y, move_x)) {
				related.push_back(sink + (move_y * W + move_x));
				debug("Related address %d, %d\n", move_x, move_y);
			}

			char use = 0;

			for (size_t k = 0; k < related.size(); k++) {
				if (*(related[k]) != 0) {
					if (use != 0 && use != *(related[k])) {
						fprintf(stderr, "ERROR: Conflict between %c and %c!\n", use, *(related[k]));
						exit(1);
					}
					use = *(related[k]);
				}
			}

			if (use == 0) {
				use = next;
				next++;
			}

			for (size_t k = 0; k < related.size(); k++) {
				*(related[k]) = use;
			}
		}
	}
}

void do_problem()
{
	int T;
	read_int(T);

	for (int i = 0; i < T; i++) {
		int H, W;
		read_int(H);
		read_int(W);

		int elevation[H * W];

		for (int y = 0; y < H; y++) {
			for (int x = 0; x < W; x++) {
				read_int(elevation[y * W + x]);
			}
		}

		char sink[H * W];

		evaluate_map(H, W, elevation, sink);

		output_case("\n");
		for (int y = 0; y < H; y++) {
			for (int x = 0; x < W; x++) {
				printf("%c ", sink[y * W + x]);
			}
			printf("\n");
		}
	}
}

