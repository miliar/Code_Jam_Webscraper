#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

vector <int> v;
char s[22];

int main()
{
    int t,Case = 1;
    freopen ("B-large.in", "r", stdin);
    freopen ("out.txt", "w", stdout);
    
    scanf ("%d", &t);
    while (t--) {
        scanf ("%s", s);
        v.clear();
        for (int i = 0; s[i]; ++i)
            v.push_back(s[i] - '0');
        printf ("Case #%d: ", Case++);
        if (next_permutation(v.begin(), v.end())) {
            for (int i = 0; i < v.size(); ++i)
                printf ("%d", v[i]);
            printf ("\n");
        }
        else {
            sort(v.begin(), v.end());
            int i = 0;
            while (v[i] == 0 && i < v.size())
                ++i;
            if (i != 0) {
                v[0] = v[i];
                v[i] = 0;
            }
            for (int i = 0; i < v.size(); ++i) {
                if (i == 1)
                    printf ("0");
                printf ("%d", v[i]);
            }
            if (v.size() == 1)
                printf ("0");
            printf ("\n");
        }
    }
    
    return 0;
}
