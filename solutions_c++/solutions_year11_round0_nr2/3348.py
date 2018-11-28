#include <stdio.h>
#include <set>
#include <cstring>
#include <vector>

template <class InputIterator1, class InputIterator2>
bool has_intersection(InputIterator1 first1, InputIterator1 last1, InputIterator2 first2, InputIterator2 last2)
{
    while (first1 != last1 && first2 != last2) {
        if (*first1 < *first2)
            ++first1;
        else if (*first2 < *first1)
            ++first2;
        else
            return true;
    }
    return false;
}

int main()
{
    int t;
    scanf("%d", &t);
    
    for (int k = 1; k <= t; ++k) {
        int c;
        scanf("%d", &c);
        
        char combinations[127][127];
        std::set<char> opposed[127];
        memset(combinations, 0, 128 * 128);
        for (int i = 0; i < c; ++i) {
            char combination[4];
            scanf("%s", combination);
            
            char b1 = combination[0];
            char b2 = combination[1];
            char nb = combination[2];
            combinations[b1][b2] = combinations[b2][b1] = nb;
        }
        
        int d;
        scanf("%d", &d);
        for (int i = 0; i < d; ++i) {
            char opposition[3];
            scanf("%s", opposition);
            
            char o1 = opposition[0];
            char o2 = opposition[1];
            opposed[o1].insert(o2);
            opposed[o2].insert(o1);
        }
        
        int n;
        char string[101];
        scanf("%d %s", &n, string);
        
        std::vector<char> result;
        std::multiset<char> charset;
        for (int i = 0; i < n; ++i) {
            char c = string[i];
            char c2 = result.empty() ? '\0' : result.back();

            if (combinations[c][c2] == '\0') {
                charset.insert(c);
                result.push_back(c);
                
                if (has_intersection(opposed[c].begin(), opposed[c].end(), charset.begin(), charset.end())) {
                    charset.clear();
                    result.clear();
                }
            } else {
                result.pop_back();
                charset.erase(charset.find(c2));
                result.push_back(combinations[c][c2]);
            }
        }
        
        printf("Case #%d: [", k);
        for (int i = 0; i < result.size(); ++i) {
            printf("%c", result[i]);
            if (i < result.size() - 1)
                printf(", "); 
        }
        printf("]\n");
    }
}

