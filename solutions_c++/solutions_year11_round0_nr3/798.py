#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <cmath>
#include <sstream>
#include <map>
#include <set>
#include <numeric>
#include <memory.h>
#include <cstdio>

using namespace std;

struct Problem
{
    int N;
    vector<int> C;

    Problem()
    {
        cin >> N;
        C.resize(N,0);
        for(int i = 0; i < N; ++i) cin >> C[i];
    }

    int solve()
    {
        int xor_res = 0;

        for(int i = 0; i < N; ++i) xor_res ^= C[i];

        if(xor_res) return -1;

        return accumulate(C.begin(),C.end(),0) - (*min_element(C.begin(), C.end()));
    }
};

int main()
{
	#ifndef ONLINE_JUDGE
        freopen("C-large.in","r",stdin);
        freopen("output.txt","w",stdout);
	#endif

    int T;
    cin >> T;

    for(int cs = 1; cs <= T; ++cs)
    {
        int ans = Problem().solve();

        cout << "Case #" << cs <<": ";

        if(ans == -1)
            cout << "NO";
        else
            cout << ans;
        cout << endl;
    }

	return 0;
}
