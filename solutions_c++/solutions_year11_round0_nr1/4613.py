#include <utility>
#include <vector>
#include <fstream>


//static const char* file = "A-small-attempt9.in";
static const char* file = "A-large.in";



int main(void)
{
	std::ifstream ifs(file);
	std::ofstream ofs("out.txt");

	if (ifs.bad() || ofs.bad()) {
		printf("Error: can't open the file\n");
		return -1;
	}

	int T;
	ifs >> T;
	for (int i = 0 ; i < T ; ++i) {
		int N;
		ifs >> N;
		std::vector<std::pair<char, int> > table(N);
		for (int j = 0 ; j < N ; ++j)
			ifs >> table[j].first >> table[j].second;

		char pr = table[0].first;
		int ot = 0, bt = 0;
		int od = 1, bd = 1; // distance
		for (int j = 0 ; j < N ; ++j) {
			const char R = table[j].first;
			const int P = table[j].second;

			const int old = (R == 'O' ? od : bd);
			const int tmp = abs(P - old) + 1;
			if (R == 'O') {
				ot += tmp;
				od = P;
			} else {
				bt += tmp;
				bd = P;
			}

			if (R != pr) {
				if (R == 'O' && (bt >= ot))
					ot = bt + 1;
				else if (R == 'B' && (ot >= bt))
					bt = ot + 1;
			}

			pr = R;
		}
		
		ofs << "Case #" << i+1 << ": " << std::max(ot,bt) << std::endl;
	}

	return 0;
}