#include <iostream>
#include <vector>
#include <algorithm>
#define pb push_back
using namespace std;

void solve_case(int case_id)
{
    cout << "Case #" << case_id << ": ";
    int i, j, C, D, N;
    char res[32][32], p, q, r;
    bool op[32][32];
    vector<char> ans;

    for(i = 0; i < 26; ++i)
        for(j = 0; j < 26; ++j)
        {
            res[i][j] = '-';
            op[i][j] = false;
        }

    cin >> C;
    for(i = 0; i < C; ++i)
    {
        cin >> p >> q >> r;
        res[p - 'A'][q - 'A'] = r;
        res[q - 'A'][p - 'A'] = r;
    }
    cin >> D;
    for(i = 0; i < D; ++i)
    {
        cin >> p >> q;
        op[p - 'A'][q - 'A'] = true;
        op[q - 'A'][p - 'A'] = true;
    }
    cin >> N;
    for(i = 0; i < N; ++i)
    {
        cin >> p;
        if(ans.size() > 0 && res[ans[ans.size() - 1] - 'A'][p - 'A'] != '-')
        {
            q = res[ans[ans.size() - 1] - 'A'][p - 'A'];
            ans.pop_back();
            ans.pb(q);
            continue;
        }
        if(ans.size() > 0)
        {
            for(j = 0; j < ans.size(); ++j)
                if(op[ans[j] - 'A'][p - 'A'])
                {
                    ans.clear();
                    goto next;
                }
        }
        ans.pb(p);
        next:;
    }
    cout << "[";
    for(i = 0; i < (int)ans.size() - 1; ++i) cout << ans[i] << ", ";
    if(ans.size() > 0) cout << ans[ans.size() - 1] << "]\n";
    else cout << "]\n";
}
int main()
{
    int i, t;
    cin >> t;
    for(i = 1; i <= t; ++i) solve_case(i);
    return 0;
}
