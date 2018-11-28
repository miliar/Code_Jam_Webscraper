#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <fstream>

using namespace std;

int main(long long int argc, char** argv)
{
    fstream in, out;
    in.open("b.in", ios_base::in);
    out.open("b.out", ios_base::out);
    long long int T;
    in >> T;
    for (long long int t = 0; t < T; t++) {
        long long int L, time, N, C;
        in >> L >> time >> N >> C;
        vector<long long int> ldist;
        for (long long int i = 0; i < C; i++) {
            long long int c;
            in >> c;
            ldist.push_back(c);
        }

        long long int full_time = 0;
        vector<long long int> dist;
        for (long long int i = 0; i < N; i++) {
            dist.push_back(ldist[i % C]);
            full_time += 2 * ldist[i % C];
        }

        vector<long long int> profit;
        long long int curtime = 0;
        for (long long int i = 0; i < N; i++) {
            if (curtime < time) {
                if (2 * dist[i] + curtime < time) {
                    profit.push_back(0);
                    curtime += 2 * dist[i];
                } else {
                    long long int dt = time - curtime;
                    long long int dl = dt / 2;
                    profit.push_back(dist[i] - dl);
                    curtime = time + 1;
                }
            } else {
                profit.push_back(dist[i]);
            }
        }
        sort(profit.begin(), profit.end());
        for (long long int i = 0; i < L; i++) {
            full_time -= profit[profit.size() - i - 1];
        }

        out << "Case #" << t + 1 << ": " << full_time << endl;
    }
    in.close();
    out.close();
	return 0;
}

