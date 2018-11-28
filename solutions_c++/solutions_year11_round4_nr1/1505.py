#define _CRT_SECURE_NO_DEPRECATE

#include <algorithm>
#include <map>
#include <set>
#include <cstdio>
#include <cstring>
#include <vector>
#include <string>
#include <sstream>
#include <queue>

		using namespace std;
#define all(a) (a).begin(),(a).end()

		struct Walk {
			Walk(){}
			Walk(int _beg, int _end, int _speed) :
			beg(_beg), end(_end), speed(_speed) {}

			int beg, end, speed;

			bool operator<(const Walk& w) const {
				return this->beg < w.beg;
			}
		};

		struct Period {
			Period(){ used = false;}
			Period(double d, double s) {distance = d; speed = s; used = false;}
			double distance;
			double speed;
			bool used;

			bool operator < (const Period& p) const {
				//double time1 = distance / speed;
				//double time2 = p.distance / p.speed;

				//return time1 < time2;

				return this->speed > p.speed;
			}

		};



		int main() {
			FILE* in = fopen("input.txt", "rt");
			FILE* out = fopen("output.txt", "wt");
			int T;
			fscanf(in, "%d", &T);

			for (int k = 0; k < T; ++k) {
				int X, s, r, N;
				double t;
				fscanf(in, "%d%d%d%lf%d", &X, &s, &r, &t, &N);
				vector<Walk> v;

				for (int i = 0; i < N; ++i) {
					int b, e, w;
					fscanf(in, "%d%d%d", &b, &e, &w);
					v.push_back(Walk(b, e, w));
				}
				sort(all(v));

				double result = 0;
				int last = 0;
				vector<Period> q;

				for (int i = 0 ; i < N; ++i) {
					if (last < v[i].beg) {
						q.push_back(Period(v[i].beg - last, s));
						result += q.back().distance / q.back().speed;
					}
					last = v[i].end;
					q.push_back(Period(v[i].end - v[i].beg, s + v[i].speed));
					result += q.back().distance / q.back().speed;	
				}

				if (last != X) {
					q.push_back(Period(X - last, s));
					result += q.back().distance / q.back().speed;
				}

				while (t > 0.000001) {
					double best_speed_up = 0.0;
					int ind = -1;
					double next_t = t;
					double dist_run = 0.0;

					double t_back = t;

					for (int i = 0; i < q.size(); ++i) {
						Period curr_p = q[i];	
						if (curr_p.distance < 0.000001) {
							continue;
						}
						
						double time = curr_p.distance / (curr_p.speed - s + r);
						if (t > time) {
							t = time;
						}
					}

					for (int i = 0; i < q.size(); ++i) {
						Period curr_p = q[i];	
						if (curr_p.distance < 0.000001) {
							continue;
						}

						double base_time = curr_p.distance / curr_p.speed;
						double su_time = 0.0;
						double tt = t;

						double dist = curr_p.distance;
						double speed = curr_p.speed - s + r;
						double time = dist / speed;

						double d3 = dist;

						if (time > t) {
							double d2 = t * speed;
							d3 = d2;
							su_time += t;
							tt = t;
							speed = speed - r + s;
							dist -= d2;
							time = dist / speed;
						}
						else {
							tt = time;
						}

						su_time += time;
						
						double curr_speedup = base_time - su_time;
						if (curr_speedup > best_speed_up) {
							best_speed_up = curr_speedup;
							next_t = tt;
							ind = i;
							dist_run = d3;
						}
					}

					if (ind == -1) {
						break;
					}
					q[ind].distance -= dist_run;
					t = t_back - next_t;
					result -= best_speed_up;
				}
				fprintf(out, "Case #%d: %lf\n", k + 1, result);
			}

			return 0;
		}
