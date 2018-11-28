#include <set>
#include <map>
#include <cmath>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <utility>
#include <iostream>
#include <algorithm>
#include <functional>

using namespace std;

string input = "B-small-attempt0.in", output = input + "___.out";
ifstream ifs(input.c_str());
ofstream ofs(output.c_str());

int main(void)
{
	int re;
	bool flag;
	int n, m, a, xmin, xmax, ymin, ymax;

	ifs >> re;
	for (int ri = 1; ri <= re; ri++) {
		ifs >> n >> m >> a;
		flag = false;		
		ofs << "Case #" << ri << ": ";
		cerr << ri << endl;
		for (int x1 = -n; x1 <= n; x1++) {
			for (int y1 = -m; y1 <= m; y1++) {
				for (int x2 = -n; x2 <= n; x2++) {
					for (int y2 = -m; y2 <= m; y2++) {
						if (abs(x1 * y2 - x2 * y1) == a) {
							xmin = min(0, min(x1, x2));
							xmax = max(0, max(x1, x2));
							ymin = min(0, min(y1, y2));
							ymax = max(0, max(y1, y2));
							if (xmax - xmin <= n && ymax - ymin <= m) {
								flag = true;
								ofs << -xmin << " " << -ymin << " " << x1 - xmin << " " << y1 - ymin << " " << x2 - xmin << " " << y2 - ymin << endl;
								goto BREAK;
							}
						}
					}
				}
			}
		}
		// output
BREAK:
		if (!flag) {
			ofs << "IMPOSSIBLE" << endl;
		}
	}

	return 0;
}
