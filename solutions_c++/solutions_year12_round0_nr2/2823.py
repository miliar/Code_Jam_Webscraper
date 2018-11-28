#include <cstdio>
#include <vector>
#include <deque>
#include <queue>
#include <map>
#include <algorithm>
#include <functional>
#include <iostream>
#include <string>
#include <cmath>

using namespace std;


int getMaxWithSurprise(int total){
    if (total <= 1 || total >= 29){
        return -1;
    }
    return (total + 4) / 3;
}

int getMaxWithNoSurprise(int total){
    return (total + 2) / 3;
}

int getMaxNumber(int N, int S, int p, vector<int> &totals){
    if (totals.size() <= 6){
        vector<int> comb(S, 1);
        for(int i = 0; i < (N-S); ++i){
            comb.push_back(0);
        }
        sort(comb.begin(), comb.end());

        int ret = 0;
        do{
            int cand = 0;
            bool hasError = false;
            for(int i = 0; i < (int)totals.size(); ++i){
                int maxScore = (comb[i])
                    ? getMaxWithSurprise(totals[i])
                    : getMaxWithNoSurprise(totals[i]);

                if (maxScore == -1){
                    hasError = true;
                    break;
                }
                if (maxScore >= p){
                    ++cand;
                }
            }

            if (cand > ret && !hasError){
                ret = cand;
            }
        }while(next_permutation(comb.begin(), comb.end()));

        return ret;
    }
    else{
        int ret = 0;

        vector<int> formerTotals(N/2);
        vector<int> latterTotals(N - (N/2));
        copy(&totals[0], &totals[N/2], formerTotals.begin());
        copy(&totals[N/2], &totals[N], latterTotals.begin());

        for(int former = 0; former <= S; ++former){
            int latter = S - former;

            if (former <= (int)formerTotals.size() && latter <= (int)latterTotals.size()){
                int cand = getMaxNumber( formerTotals.size(), former, p, formerTotals )
                         + getMaxNumber( latterTotals.size(), latter, p, latterTotals );
                if (cand > ret){
                    ret = cand;
                }
            }
        }
        return ret;
    }
}

int main(void)
{
    int T;
    cin >> T;

    for(int t = 0; t < T; ++t){
        int N, S, p;
        cin >> N >> S >> p;

        vector<int>totals;
        for(int n = 0; n < N; ++n){
            int tmp;
            cin >> tmp;
            totals.push_back(tmp);
        }

        int ret = getMaxNumber(N, S, p, totals);

        cout << "Case #" << (t+1) << ": " << ret << endl;
    }

    return 0;
}
