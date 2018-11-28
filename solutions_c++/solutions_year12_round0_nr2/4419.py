#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

int main()
{
    int n;
    scanf("%d", &n);
    for(int k = 1; k <= n; k++) {
        int t, s, p;
        scanf("%d %d %d", &t, &s, &p);
        vector<int> scores;
        for(int i = 0; i < t; i++) {
            int temp;
            scanf("%d", &temp);
            scores.push_back(temp);
        }
        int miniWithout = 3*p - 2;
        int miniWith = 3*p - 4;
        int countWithout = 0;
        int countWith = 0;
        int res;
        if(p != 0){
            for(int i = 0; i < scores.size(); i++) {
                if(scores[i] >= miniWithout)
                    countWithout++;
                else if (scores[i] >= miniWith && scores[i] > 0)
                    countWith++;
            }
            res = countWithout + min(countWith, s);
        } else res = scores.size();

        printf("Case #%d: %d\n", k, res);
    }
    return 0;
}
