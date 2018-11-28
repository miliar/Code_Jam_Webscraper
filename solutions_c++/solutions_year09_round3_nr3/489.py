#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <list>
#include <set>
#include <ios>
#include <map>
#include <algorithm>
#include <iomanip>
#include <limits>

using namespace std;

int calc(vector<bool>& p, int P, vector<int>& q, int Q)
{
    int result = 0;

    for (int i = 0; i < Q; ++i) {
        int ind = q[i];
        if (!p[ind]) continue;

        p[ind] = false;

        int res = 0;
        int j = ind - 1;
        while (j >= 0 && p[j]) ++res, --j;
        j = ind + 1;
        while (j < P && p[j]) ++res, ++j;

        res += calc(p, P, q, Q);

        if (!result || res < result) result = res;

        p[ind] = true;
    }

    return result;
}

int main(int argc, char* argv[])
{
	int N;
	cin >> N;

    for (int i = 1; i <= N; ++i) {
        int P, Q;
        cin >> P >> Q;

        vector<bool> p(P);
        for (int j = 0; j < P; ++j) p[j] = true;

        vector<int> q(Q);
        for (int j = 0; j < Q; ++j) {
            cin >> q[j];
            --q[j];
        }

        int result = calc(p, P, q, Q);

        cout << "Case #" << i << ": " << result << endl;
    }

	return 0;
}
