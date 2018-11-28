#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int T;

int main() {
    scanf("%d", &T);

    for (int casenum = 1; casenum <= T; ++casenum) {
        char temp[50];
        scanf("%s", temp);
        vector<int> nums;
        vector<int> numsnozero;
        int zeroes = 0;
        char* p = temp;
        while (*p) {
            int t = (int)(*p - '0');
            nums.push_back(t);
            if (t == 0) {
                zeroes += 1;
            } else {
                numsnozero.push_back(t);
            }
    
            p++;
        }        
        /*for (int i = 0; i < nums.size(); ++i)
            printf("%d ", nums[i]);
        printf("\n");*/

        vector<int> cur = nums;
        if (!next_permutation(cur.begin(), cur.end())) {
            cur = numsnozero;
            sort(cur.begin(), cur.end());
            zeroes += 1;
            for (int i = 0; i < zeroes; ++i)
                cur.insert(cur.begin()+1, 0);
        }
        printf("Case #%d: ", casenum);
        for (int i = 0; i < cur.size(); ++i)
            printf("%d", cur[i]);
        printf("\n");
        
    }
    return 0;
}
