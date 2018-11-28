#include <stdio.h>
#include <list>
#include <map>

using namespace std;

/*

score    surprising     high score
-----   ------------   -------------
0           N             0         [0, 0, 0]
1           N             1         [0, 0, 1]
2           Y             2         [0, 1, 1] *[0, 0, 2]
3           Y             2         [1, 1, 1] *[0, 1, 2]
4           Y             2         [1, 1, 2] *[0, 2, 2]
5           Y             3         *[1, 1, 3] [1, 2, 2]
6           Y             3         *[1, 2, 3] [2, 2, 2]
7           Y             3         *[1, 3, 3] [2, 2, 3]
8           Y             4         *[2, 2, 4] [2, 3, 3]
9           Y             4         *[2, 3, 4] [3, 3, 3]

10          Y             4         *[2, 4, 4] [3, 3, 4]
11          Y             5         *[3, 3, 5] [3, 4, 4]
12          Y             5         *[3, 4, 5] [4, 4, 4]
13          Y             5         *[3, 5, 5] [4, 4, 5]
14          Y             6         *[4, 4, 6] [4, 5, 5]

15          Y             6         *[4, 5, 6] [5, 5, 5]
16          Y             6         *[4, 6, 6] [5, 5, 6]
17          Y             7         *[5, 5, 7] [5, 6, 6]
18          Y             7         *[5, 6, 7] [6, 6, 6]
19          Y             7         *[5, 7, 7] [6, 6, 7]

20          Y             8         *[6, 6, 8] [6, 7, 7]
21          Y             8         *[6, 7, 8] [7, 7, 7]
22          Y             8         *[6, 8, 8] [7, 7, 8]
23          Y             9         *[7, 7, 9] [7, 8, 8]
24          Y             9         *[7, 8, 9] [8, 8, 8]

25          Y             9         *[7, 9, 9] [8, 8, 9]
26          Y             10        *[8, 8, 10] [8, 9, 9]
27          Y             10        *[8, 9, 10] [9, 9, 9]
28          Y             10        *[8, 10, 10] [9, 9, 10]
29          N             10        [9, 10, 10]
30          N             10        [10, 10, 10]
*/

#define MIN(x, y) ((x) < (y) ? x : y)

int lscore_map[] = {
    0, 1, 1, 1, 2,
    2, 2, 3, 3, 3, 4,
    4, 4, 5, 5, 5, 6, 
    6, 6, 7, 7, 7, 8,
    8, 8, 9, 9, 9, 10, 10, 10
};

int hscore_map[] = {
    0, 1, 2, 2, 2,
    3, 3, 3, 4, 4, 4,
    5, 5, 5, 6, 6, 6, 
    7, 7, 7, 8, 8, 8,
    9, 9, 9, 10, 10, 10, 10, 10
};



int main()
{
    FILE *ifile = freopen("input.in", "r", stdin);
    FILE *ofile = freopen("output.txt", "w", stdout);

    int num_inputs = 0;
    scanf("%d", &num_inputs);

    int num_gler;
    int num_sp;
    int threshold;
    for (int i = 0 ; i < num_inputs ; ++i)
    {
        scanf("%d %d %d", &num_gler, &num_sp, &threshold);

        int ns_accept = 0;
        int s_accept = 0;
        int score;
        for (int j = 0 ; j < num_gler ; ++j)
        {
            scanf("%d", &score);
            if (lscore_map[score] >= threshold)
            {
                ++ns_accept;
            }
            else
            {
                if (hscore_map[score] >= threshold)
                {
                    if (score < 2 || score > 28)
                    {
                        // ns_group
                        ++ns_accept;
                    }
                    else
                    {
                        // s_group
                        ++s_accept;
                    }
                }
            }
        }

        printf("Case #%d: %d\n", (i+1), ns_accept + MIN(num_sp, s_accept));
    }


    fclose(ifile);
    fclose(ofile);
    return 0;
}