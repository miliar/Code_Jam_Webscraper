#include <cstdio>
#include <vector>
#include <set>

using namespace std;

int f(int i, int b) {
    int r = 0;
    while (i) {
        int d = i % b;
        i /= b;
        r += d * d;
    }
    return r;
}

bool test(int i, int b) {
    set<int> v;
    v.insert(i);
    while(i != 1) {
        int t = f(i, b);
        if (v.find(t) != v.end())
            return false;
        i = t;
        v.insert(i);
    }
    return true;
}

int main()
{
    int nCase;
    scanf("%d\n", &nCase);
    for (int iCase = 1; iCase <= nCase; ++iCase)
    {
        char line[1024];
        gets(line);

        vector<int> vi;
        int t, n;
        char *p = line;
        while (sscanf(p, "%d%n", &t, &n) == 1)
        {
            p += n;
            vi.push_back(t);
        }

        for (int i = 2; i < 1000000; ++i)
        {
            bool all = true;
            for (unsigned j = 0; j < vi.size(); ++j)
            {
                if (!test(i, vi[j]))
                {
//                    printf("%d fails at %d\n", i, vi[j]);
                    all = false;
                    break;
                }
//                printf("%d pass\n", vi[j]);
            }
            if (all) {
                printf("Case #%d: %d\n", iCase, i);
                break;
            }
        }
    }

    return 0;
}
