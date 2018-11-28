#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

#define pb push_back

using namespace std;

int solve(int le, int ri) {
    int ans = 0;
    for(int i = le; i <= ri; i ++) {

        int num = i;
        vector<int> tmp;
        while(num) {
            tmp.pb(num % 10);
            num /= 10;
        }
        reverse(tmp.begin(), tmp.end());

        set<int> st;
        for(int j = 0; j < tmp.size(); j ++) {
            num = 0;
            for(int k = 0; k < tmp.size(); k ++)
                num = num * 10 + tmp[(j + k) % tmp.size()];

            if(i < num && num <= ri) st.insert(num);
        }

        ans += st.size();
    }
    return ans;
}

int main()
{
    int t, a, b;
    scanf("%d", &t);
    for(int i = 1; i <= t; i ++) {
        scanf("%d %d", &a, &b);
        printf("Case #%d: %d\n", i, solve(a, b));
    }

    return 0;
}
