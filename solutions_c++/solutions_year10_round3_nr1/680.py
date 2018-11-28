#include <iostream>
#include <algorithm>
using namespace std;

struct Line {
    int a, b;
} line[1010];

bool cmp(Line a, Line b)
{
    return a.a < b.a;
}

int main()
{
    freopen("A-large.in", "r", stdin);
	freopen("al.out.txt", "w", stdout);

    int T, N;
    int count, t, i, j;

    scanf("%d", &T);
    for (t = 1; t <= T; ++t)
    {
        scanf("%d", &N);
        for (i=0; i<N; i++) {
            scanf("%d %d", &line[i].a, &line[i].b);
        }

        sort(line, line+N, cmp);

        count = 0;
        for (i=1; i<N; i++) {
            for (j=i-1; j>=0; j--) {
                if (line[i].b < line[j].b) count ++;
            }
        }

        printf("Case #%d: %d\n", t, count);
    }

    fclose(stdin);
	fclose(stdout);

    return 0;
}
