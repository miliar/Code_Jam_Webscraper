#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int n; scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        int j; scanf("%d", &j);
        vector<int> elems;
        vector<int> left_xor(j, 0);
        vector<int> right_xor(j, 0);
        for (int k = 0; k < j; k++) {
            int temp; scanf("%d", &temp);
            elems.push_back(temp);
        }
        sort(elems.begin(), elems.end());
        reverse(elems.begin(), elems.end());
        left_xor[0] = elems[0];
        for (int k = 1; k < j; k++) {
            left_xor[k] = elems[k] ^ left_xor[k - 1];
            
        }
        right_xor[j - 1] = elems[j - 1];
        for (int k = j - 2; k >= 0; k--) {
            right_xor[k] = elems[k] ^ right_xor[k + 1];
        }
        int k;
        for (k = j - 1; k > 0; k--) {
            if (right_xor[k] == left_xor[k - 1]) {
                break;
            }
        }

        if (k == 0) {
            printf("Case #%d: NO\n", (i + 1));
        } else {
            int sum = 0;
            for (int a = 0; a < k; a++)
                sum += elems[a];

            printf("Case #%d: %d\n", (i + 1), sum);
        }
    } 
    return 0;
}
