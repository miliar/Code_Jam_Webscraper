//	!

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

#include <set>
#include <map>
#include <vector>
#include <complex>
using namespace std;

int row, col;

int price [105][30];
bool conflict [105][105];

int minChart;

vector<int> charts [105];

void doit (int nChart, int stock)
{
	if (stock == row) {

		//printf ("nChart = %d:\n", nChart);

		if (minChart < 0 || minChart > nChart)
			minChart = nChart;

		//for (int i=0; i<nChart; ++i) {
		//	for (int k=0, n=charts [i].size(); k<n; ++k)
		//		printf (" %d", charts [i].at (k));
		//	puts ("");
		//}
		//puts ("");

		return;
	}

	if (minChart > -1 && minChart <= nChart) return;

	// use existing chart
	bool safe;
	for (int i=0; i<nChart; ++i) {
		int n = charts [i].size();

		safe = true;
		for (int k=0; k<n; ++k) {
			if (conflict [charts [i][k]][stock]) {
				safe = false;
				break;
			}
		}

		if (safe) {
			charts [i].push_back (stock);
			doit (nChart, stock + 1);
			charts [i].pop_back();
		}
	}

	// use new chart
	charts [nChart].push_back (stock); // it should be empty

	doit (nChart + 1, stock + 1);

	charts [nChart].clear();

}

int main()
{
	int kase, serial=0;

	scanf ("%d", &kase);

	while (kase--)
	{
		// begin test case
		scanf ("%d %d", &row, &col);

		memset (conflict, 0, sizeof (conflict));
		for (int i=0; i<105; ++i)
			charts [i].clear();

		for (int r=0; r<row; ++r) {
			for (int c=0; c<col; ++c) {
				scanf ("%d", & (price [r][c]));
			}

			// mark conflict
			for (int i=0; i<r; ++i) {
				if (price [i][0] > price [r][0]) {
					for (int c=0; c<col; ++c) {
						if (price [i][c] <= price [r][c]) {
							conflict [r][i] = true;
							conflict [i][r] = true;
							break;
						}
					}
				} else if (price [i][0] < price [r][0]) {
					for (int c=0; c<col; ++c) {
						if (price [i][c] >= price [r][c]) {
							conflict [r][i] = true;
							conflict [i][r] = true;
							break;
						}
					}
				} else {
					conflict [r][i] = true;
					conflict [i][r] = true;
				}
			}
		}

		minChart = -1;

		doit (0, 0);

		printf ("Case #%d: %d\n", ++serial, minChart);
		// end test case
	}
	return 0;
}