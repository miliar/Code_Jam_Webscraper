#include <iostream>

using namespace std;


char r_tab[128];
int p_tab[128];
int t, n;
int wyn;
static int INF = 1024;

int next(int current, char c) {

	int index = INF;

	for (int j=current+1; j<n; ++j) {

		if (r_tab[j] == c) {

			index = j;

			break;
		}
	}

	return index;	
}

int
main()
{
	cin >> t;

	for (int i=0; i<t; ++i) {

		cin >> n;

		for (int j=0; j<n; ++j) {

			cin >> r_tab[j] >> p_tab[j];
		}

		int i_orange = -1;
		int i_blue = -1;
		int gdzie_orange = 1;
		int gdzie_blue = 1;
		bool czy_orange = true;
		bool czy_blue = true;
		wyn = 0;

		while (true) {

			if (czy_orange) {
	
				i_orange = next(i_orange, 'O');
				czy_orange = false;
			}
			if (czy_blue) {
	
				i_blue = next(i_blue, 'B');
				czy_blue = false;
			}

			if (i_orange == INF && i_blue == INF) {

				break;
			}

			if (i_orange < i_blue) {

				if (p_tab[i_orange] == gdzie_orange) {

					czy_orange = true;

				} else if (p_tab[i_orange] > gdzie_orange) {

					++gdzie_orange;

				} else if (p_tab[i_orange] < gdzie_orange) {

					--gdzie_orange;
				}

				if (i_blue != INF && p_tab[i_blue] > gdzie_blue) {

					++gdzie_blue;

				} else if (i_blue != INF && p_tab[i_blue] < gdzie_blue) {

					--gdzie_blue;
				}

			} else {
				
				if (p_tab[i_blue] == gdzie_blue) {

					czy_blue = true;

				} else if (p_tab[i_blue] > gdzie_blue) {

					++gdzie_blue;

				} else if (p_tab[i_blue] < gdzie_blue) {

					--gdzie_blue;
				}

				if (i_orange != INF && p_tab[i_orange] > gdzie_orange) {

					++gdzie_orange;

				} else if (i_orange != INF && p_tab[i_orange] < gdzie_orange) {

					--gdzie_orange;
				}
			}

			++wyn;
		}
	
		cout << "Case #" << i+1 << ": " << wyn << endl;
	}


	return 0;	
}
