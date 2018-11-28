#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
#include <set>

using std::set;

typedef set<unsigned int> uint_set;
uint_set *basins[100][100];

void merge_sets(unsigned int src, unsigned int dst, unsigned int width) {
	if (basins[src / width][src % width] == basins[dst / width][dst % width])
		return;
	for (uint_set::iterator k = basins[src / width][src % width]->begin(); k != basins[src / width][src % width]->end(); ++k) {
		//printf("Merging (%d, %d) with (%d, %d)\n", *k / width, *k % width, dst / width, dst % width);
		if (*k == src || *k == dst)
			continue;
		basins[dst / width][dst % width]->insert(*k);
		basins[*k / width][*k % width] = basins[dst / width][dst % width];
	}
	basins[src / width][src % width]->clear();
	delete basins[src / width][src % width];
	basins[dst / width][dst % width]->insert(src);
	basins[src / width][src % width] = basins[dst / width][dst % width];
}

int main(int argc, char *argv[]) {
	FILE *f;
	unsigned int num_maps;

	f = fopen(argv[1], "r");
	fscanf(f, "%u\n", &num_maps);

	for (unsigned int t = 0; t < num_maps; ++t) {
		unsigned int height, width;
		unsigned int alts[100][100];
		unsigned char basin_index[100][100];

		fscanf(f, "%u %u\n", &height, &width);
		//printf("Case %d: height %u width %u\n", t, height, width);

		for (unsigned int i = 0; i < height; ++i) {
			for (unsigned int j = 0; j < width; ++j) {
				fscanf(f, "%u", &(alts[i][j]));
				basins[i][j] = new uint_set();
				basins[i][j]->insert(i * width + j);
			}
		}

		for (unsigned int i = 0; i < height; ++i) {
			for (unsigned int j = 0; j < width; ++j) {
				//printf("Processing (%d, %d)\n", i, j);
				unsigned int min_alt = alts[i][j];
				unsigned int min_alt_pos = i * width + j;
				if (i > 0 && min_alt > alts[i - 1][j]) {
					min_alt = alts[i - 1][j];
					min_alt_pos = (i - 1) * width + j;
				}
				if (j > 0 && min_alt > alts[i][j - 1]) {
					min_alt = alts[i][j - 1];
					min_alt_pos = i * width + j - 1;
				}
				if (j < width - 1 && min_alt > alts[i][j + 1]) {
					min_alt = alts[i][j + 1];
					min_alt_pos = i * width + j + 1;
				}
				if (i < height - 1 && min_alt > alts[i + 1][j]) {
					min_alt = alts[i + 1][j];
					min_alt_pos = (i + 1) * width + j;
				}
				if (min_alt == alts[i][j]) {
					/*
					if (i > 0) {
						merge_sets((i - 1) * width + j, i * width + j, width);
					}
					if (i < height - 1) {
						merge_sets((i + 1) * width + j, i * width + j, width);
					}
					if (j > 0) {
						merge_sets(i * width + j - 1, i * width + j, width);
					}
					if (j < width - 1) {
						merge_sets(i * width + j + 1, i * width + j, width);
					}
					*/
				}
				else {
					merge_sets(i * width + j, min_alt_pos, width);
				}
			}
		}

		printf("Case #%d:\n", t + 1);
		unsigned int num_sinks = 0;
		for (unsigned int i = 0; i < height; ++i) {
			for (unsigned int j = 0; j < width; ++j) {
				uint_set::iterator it = basins[i][j]->lower_bound(0);
				if (*it == i * width + j) {
					++num_sinks;
					basin_index[i][j] = (char)(num_sinks + 96);
				}
				else {
					assert(*it < i * width + j);
					basin_index[i][j] = basin_index[*it / width][*it % width];
				}
				printf("%c", basin_index[i][j]);
				if (j < width - 1)
					printf(" ");

				it = basins[i][j]->upper_bound(i * width + j);
				if (*it == i * width + j) {
					basins[i][j]->clear();
					delete basins[i][j];
				}
			}
			printf("\n");
		}
	}

	fclose(f);
}
