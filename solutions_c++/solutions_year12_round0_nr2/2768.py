
#include <fstream>
#include <set>
#include <vector>

const int MAX_DIM = 100;
int t[MAX_DIM] = {};

#define max(a, b) ((a) > (b)? (a):(b))
#define min(a, b) ((a) < (b)? (a):(b))

int N = 0, S = 0, p = 0;

struct googler {
	int a, b, c;
	std::vector<int> vt;
};

std::vector<std::pair<googler, googler> > g;

void processChoice(int& R, const std::vector<googler>& vt) {
	int surprised = 0, r = 0;

	for (int i = 0; i < (int)vt.size(); ++i) {
		if (vt[i].a < 0) {
			return;
		}
		if (vt[i].c - vt[i].a == 2) ++surprised;
		if (vt[i].c >= p) ++r;
	}

	if (surprised == S && R < r) R = r;
}

int main() {
	int T = 0;
	std::ifstream fin("GCJ2012_B_IN.txt");
	std::ofstream fout("GCJ2012_B_OUT.txt");
	fin >> T;	
	for (int test = 0; test < T; ++test)	{
		N = 0, S = 0, p = 0;
		memset(t, 0, sizeof(int) * MAX_DIM);
		fin >> N >> S >> p;
		
		for (int i = 0; i < N; ++i) {
			fin >> t[i];
		}
		g = std::vector<std::pair<googler, googler> >(N);

		for (int i = 0; i < N; ++i) {
			int a = t[i] / 3;
			std::pair<googler, googler> gp;
			gp.first.a = gp.second.a = -1;

			if (t[i] % 3 == 0) {
				if (a >= 0) {
					gp.first.a = gp.first.b = gp.first.c = a;
					
					if (a >= 1) {
						gp.second.a = a - 1;
						gp.second.b = a;
						gp.second.c = a + 1;
					}
				}
			} else if (t[i] % 3 == 1) {
				if (a >= 0) {
					gp.first.a = gp.first.b = a;
					gp.first.c = a + 1;
					
					if (a >= 1) {
						gp.second.a = a - 1;
						gp.second.b = gp.second.c = a + 1;
					}
				}
			} else {
				gp.first.a = gp.first.b = a;
				gp.first.c = a + 2;
				gp.second.a = a;
				gp.second.b = gp.second.c = a + 1;
			}

			if (gp.first.c > 10) {
				gp.first.a = -1;
			}

			if (gp.second.c > 10) {
				gp.second.a = -1;
			}
			g[i] = gp;

			if (gp.first.a > -1) {
				g[i].first.vt = std::vector<int>(N + 1);
				g[i].first.vt[0] = (gp.first.c - gp.first.a < 2 && gp.first.c >= p)? 1 : 0;
				g[i].first.vt[1] = (gp.first.c - gp.first.a == 2 && gp.first.c >= p)? 1 : 0;
			}

			if (gp.second.a > -1) {
				g[i].second.vt = std::vector<int>(N + 1);
				g[i].second.vt[0] = (gp.second.c - gp.second.a < 2 && gp.first.c >= p)? 1 : 0;
				g[i].second.vt[1] = (gp.second.c - gp.second.a == 2 && gp.first.c >= p)? 1 : 0;
			}

			if (i > 0) {
				if (g[i].first.a > -1) {
					int v0 = g[i].first.vt[0];
					int v1 = g[i].first.vt[1];
					
					if (g[i - 1].first.a > -1) {
						for (int j = 0; j <= S; j++) {
							int vx = g[i - 1].first.vt[j];

							if (vx != 0/* && j > 0*/) {
								g[i].first.vt[j] = max(g[i].first.vt[j], vx + v0);
							}

							if (g[i].first.c - g[i].first.a == 2 && (vx != 0 || j == 0)) {
								g[i].first.vt[j + 1] = max(g[i].first.vt[j + 1], vx + ((g[i].first.c >= p)? 1 : 0));
							}
						}
					}

					if (g[i - 1].second.a > -1) {
						for (int j = 0; j <= S; j++) {
							int vx = g[i - 1].second.vt[j];

							if (vx != 0/* && j > 0*/) {
								g[i].first.vt[j] = max(g[i].first.vt[j], vx + v0);
							}

							if (g[i].first.c - g[i].first.a == 2 && (vx != 0 || j == 0)) {
								g[i].first.vt[j + 1] = max(g[i].first.vt[j + 1], vx + ((g[i].first.c >= p)? 1 : 0));
							}
						}
					}
					g[i].first.vt[0] = v0 + max((g[i - 1].first.a > -1)? g[i - 1].first.vt[0] : 0, (g[i - 1].second.a > -1)? g[i - 1].second.vt[0] : 0);
				}

				if (g[i].second.a > -1) {
					int v0 = g[i].second.vt[0];
					int v1 = g[i].second.vt[1];
					
					if (g[i - 1].first.a > -1) {
						for (int j = 0; j <= S; j++) {
							int vx = g[i - 1].first.vt[j];
							
							if (vx != 0/* && j > 0*/) {
								g[i].second.vt[j] = max(g[i].second.vt[j], vx + v0);
							}

							if (g[i].second.c - g[i].second.a == 2 && (vx != 0 || j == 0)) {
								g[i].second.vt[j + 1] = max(g[i].second.vt[j + 1], vx + ((g[i].second.c >= p)? 1 : 0));
							}
						}
					}

					if (g[i - 1].second.a > -1) {
						for (int j = 0; j <= S; j++) {
							int vx = g[i - 1].second.vt[j];
							
							if (vx != 0/* && j > 0*/) {
								g[i].second.vt[j] = max(g[i].second.vt[j], vx + v0);
							}

							if (g[i].second.c - g[i].second.a == 2 && (vx != 0 || j == 0)) {
								g[i].second.vt[j + 1] = max(g[i].second.vt[j + 1], vx + ((g[i].second.c >= p)? 1 : 0));
							}
						}
					}
					g[i].second.vt[0] = v0 + max((g[i - 1].first.a > -1)? g[i - 1].first.vt[0] : 0, (g[i - 1].second.a > -1)? g[i - 1].second.vt[0] : 0);
				}
			}
		}
		//fout << "Case #" << test + 1 << ": " << max((g[N-1].first.a > - 1)? g[N-1].first.vt[S] : 0, (g[N-1].second.a > - 1)? g[N-1].second.vt[S] : 0);
		int R = 0;
		if (N == 1) {
			std::vector<googler> vg1;
			std::vector<googler> vg2;
			vg1.push_back(g[0].first);
			vg2.push_back(g[0].second);
			processChoice(R, vg1);
			processChoice(R, vg2);
		} else if (N == 2) {
			std::vector<googler> vg1;
			std::vector<googler> vg2;
			std::vector<googler> vg3;
			std::vector<googler> vg4;
			vg1.push_back(g[0].first);
			vg1.push_back(g[1].first);
			vg2.push_back(g[0].first);
			vg2.push_back(g[1].second);
			vg3.push_back(g[0].second);
			vg3.push_back(g[1].first);
			vg4.push_back(g[0].second);
			vg4.push_back(g[1].second);
			processChoice(R, vg1);
			processChoice(R, vg2);
			processChoice(R, vg3);
			processChoice(R, vg4);
		} else if (N == 3) {
			std::vector<googler> vg1;
			std::vector<googler> vg2;
			std::vector<googler> vg3;
			std::vector<googler> vg4;
			std::vector<googler> vg5;
			std::vector<googler> vg6;
			std::vector<googler> vg7;
			std::vector<googler> vg8;

			vg1.push_back(g[0].first);
			vg1.push_back(g[1].first);
			vg1.push_back(g[2].first);

			vg2.push_back(g[0].first);
			vg2.push_back(g[1].first);
			vg2.push_back(g[2].second);

			vg3.push_back(g[0].first);
			vg3.push_back(g[1].second);
			vg3.push_back(g[2].first);

			vg4.push_back(g[0].first);
			vg4.push_back(g[1].second);
			vg4.push_back(g[2].second);

			vg5.push_back(g[0].second);
			vg5.push_back(g[1].first);
			vg5.push_back(g[2].first);

			vg6.push_back(g[0].second);
			vg6.push_back(g[1].first);
			vg6.push_back(g[2].second);

			vg7.push_back(g[0].second);
			vg7.push_back(g[1].second);
			vg7.push_back(g[2].first);

			vg8.push_back(g[0].second);
			vg8.push_back(g[1].second);
			vg8.push_back(g[2].second);

			processChoice(R, vg1);
			processChoice(R, vg2);
			processChoice(R, vg3);
			processChoice(R, vg4);
			processChoice(R, vg5);
			processChoice(R, vg6);
			processChoice(R, vg7);
			processChoice(R, vg8);
		}
		fout << "Case #" << test + 1 << ": " << R;

		if (test < T - 1) {
			fout << std::endl;
		}
		g.clear();
	}
	fin.close();
	fout.close();
	return 0;
}
