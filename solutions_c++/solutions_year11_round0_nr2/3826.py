#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;

//////////////////////////////////////////////////////////////////////////

struct ONE_CASE
{
	int C;
	int D;
	int N;

	char combine[36][4];
	char oppose[28][3];
	char invoke[101];
};

int T;

ONE_CASE allCases[100];
char results[100][101];

int LoadData(char * filename)
{
	int i, j, k, C, D, N;
	char ch;
	fstream f(filename);
	if (!f.is_open()) {
		return 0;
	}

	f >> T;

	for (i = 0; i < T; ++i) {
		f >> C;
		allCases[i].C = C;
		k = 0;

		for (j = 0; j < C; ++j) {
			for (k = 0; k < 3; ++k) {
				f >> ch;
				allCases[i].combine[j][k] = ch;
			}
		}

		f >> D;
		allCases[i].D = D;
		for (j = 0; j < D; ++j) {
			for (k = 0; k < 2; ++k) {
				f >> ch;
				allCases[i].oppose[j][k] = ch;
			}
		}

		f >> N;
		allCases[i].N = N;

		for (j = 0; j < N; ++j) {
			f >> ch;
			allCases[i].invoke[j] = ch;
		}
	}

	return 1;
}

void Process()
{
	int no;
	for (no = 0; no < T; ++no) {
		ONE_CASE * p = allCases + no;
		char *invoke = results[no];
		int i, j, k, N = p->N, C = p->C, D = p->D;
		char chNow, chLast;
		invoke[0] = p->invoke[0];
		int idx, combine, oppose;

		idx = 1;
		for (i = 1; i < N; ++i)
		{
			chNow = invoke[idx] = p->invoke[i];

			if (idx == 0) {
				++idx;
				continue;
			}

			chLast = invoke[idx - 1];

			combine = 0;
			oppose = 0;
			for (j = 0; j < C; ++j) {
				if (chNow == p->combine[j][0] && chLast == p->combine[j][1]) {
					combine = 1;
					break;
				}

				if (chNow == p->combine[j][1] && chLast == p->combine[j][0]) {
					combine = 1;
					break;
				}
			}

			if (combine) {
				invoke[idx - 1] = p->combine[j][2];
				invoke[idx] = 0;
			} else {
				for (j = 0; j < idx; ++j) {
					for (k = 0; k < D; ++k) {
						if (chNow == p->oppose[k][0] && invoke[j] == p->oppose[k][1]) {
							oppose = 1;
							break;
						}

						if (chNow == p->oppose[k][1] && invoke[j] == p->oppose[k][0]) {
							oppose = 1;
							break;
						}
					}

					if (oppose) {
						break;
					}
				}

				if (oppose) {
					memset(invoke, 0, 11);
					idx = 0;
				} else {
					invoke[idx++] = p->invoke[i];
				}
			}
		}
	}
}

void Output()
{
	stringstream ss;
	fstream f("output.txt", ios::out | ios::trunc);
	char *invoke;
	int len;
	for (int i = 0; i < T; ++i) {
		invoke = results[i];
		ss << "Case #" << i + 1 <<": " <<'[';
		len = strlen(invoke);
		if (len > 0) {
			ss << invoke[0];
			for (int j = 1; j < len; ++j) {
				ss << ", " << invoke[j];
			}
		}
		ss <<"]\r\n";

		f << ss.str();

		ss.str("");
	}

	f.close();
}

int main(int argc, char * argv[])
{
	if (!LoadData("B-small-attempt0.in")){
		return -1;
	}
	
	Process();

	Output();

	return 0;
}