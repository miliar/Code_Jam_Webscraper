#include <iostream>
#include <cstring>
#include <vector>

using namespace std;

const size_t MAX_GRP = 1024;

typedef unsigned long long ULL;

ULL R, k, N;
ULL gv[MAX_GRP];
int next[MAX_GRP];
size_t at[MAX_GRP];

pair<ULL, size_t> f(size_t i)
{
    ULL se = 0;
    size_t c;
    for (c = 0; c < N; c++)
    {
	if (se + gv[i] > k)
	    return make_pair(se, i);
	se += gv[i];
	i = (i + 1) % N;
    }
    
    return make_pair(se, 0);
}

int main()
{
    unsigned T;
    while (cin >> T)
    {
	for (size_t t = 1; t <= T; ++t)
	{
	    memset(next, 0xff, sizeof(next));
	    memset(at, 0, sizeof(at));

	    cin >> R >> k >> N;
	    for (size_t i = 0; i < N; ++i)
		cin >> gv[i];

	    vector<ULL> ev;
	    size_t p = 0;
	    while (next[p] == -1)
	    {
		pair<ULL, size_t> change = f(p);
		// cout << "change: " 
		//      << change.first << " " 
		//      << change.second << endl;
		ev.push_back(change.first);
		next[p] = change.second;
		at[p] = ev.size() - 1;
		p = next[p];
	    }
	    // cout << "p = " << p << endl;

	    ULL res = 0;
	    
	    size_t i;
	    for (i = 0; i < at[p] && i < R; ++i)
		res += ev[i];
	    // cout << "res = " << res;

	    size_t l = ev.size() - at[p];
	    size_t s = 0, j = i;
	    for (j = i; j < ev.size() && j < R; ++j)
		s += ev[j];
	    res += s * ((R - i) / l);
	    ULL Rp = (R - i) % l;

	    for (j = i; j < i + Rp; ++j)
		res += ev[j];

	    // cout << ", s = " << s 
	    // 	 << ", l = " << l 
	    // 	 << ", Rp = " << Rp << endl;
	    cout << "Case #" << t << ": " << res << endl;
	}
    }

    return 0;
}
