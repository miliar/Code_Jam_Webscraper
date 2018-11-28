#include <vector>
#include <list>
#include <queue>
#include <map>
#include <set>
#include <string>
#include <iostream>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <cstdio>
#include <cstdlib>

using namespace std;

int
main(void)
{
    int N;
    int k, M;
    int i, j, a, ans, tmp;
    string s;

    cin >> N;

    for(i=1;i<=N;i++) {
        cin >> k;
        cin >> s;

        vector<int> perm(k);

        ans = 100000;
        
        M = 1;
        for(j=0;j<k;j++) {
            perm[j] = j;
            M *= (j+1);
        }
        for(j=0;j<M;j++) {
            string s_new = s;

            for(a=0;a<s_new.size();a++) {
                s_new[a] = s[(a/k)*k+perm[a % k]];
            }
            tmp = 1;
            for(a=1;a<s_new.size();a++) {
                if (s_new[a] != s_new[a-1])
                    tmp++;
            }
            ans = min(ans, tmp);
            
            next_permutation(perm.begin(), perm.end());
        }
        cout << "Case #" << i << ": " << ans << endl;
    }
    
    return 0;
}
