#include <stdio.h>
#include <string.h>

#define MS 109

int att[MS][MS];

int set[MS*MS];
int idx[MS*MS];

int dir[5][2] = { {0, 0}, {-1, 0}, {0, -1}, {0, 1}, {1, 0} };

int find(int th)
{
//    printf("find(%d), set[th] = %d\n", th, set[th]);
    if(set[th] == th) return th;
    return set[th] = find(set[th]);
}

void setUnion(int a, int b)
{
//    printf("union : %d %d\n", a, b);
    set[find(a)] = set[find(b)];
}

int getPtr(int i, int j) { return i*MS + j; }

int main()
{
    freopen("B-large.in", "rt", stdin);
    freopen("B-large.txt", "wt", stdout);

    int t;
//    for(int i = 0; i <= 4; i++)
//        printf("dir[%d %d]\n", dir[i][0], dir[i][1]);

    scanf("%d", &t);
    
    for(int tt = 1; tt <= t; tt++)
    {
        for(int i = 0; i < MS*MS; i++)
            set[i] = i;
        
        int h, w;

        scanf("%d %d", &h, &w);
//        printf("[%d %d]\n", h, w);
        
        for(int i = 1; i <= h; i++)
            for(int j = 1; j <= w; j++)
                scanf("%d", &att[i][j]);

        for(int i = 0; i < MS; i++)
            att[0][i] = att[h+1][i] = att[i][0] = att[i][w+1] = 1000000;
        
        for(int i = 1; i <= h; i++)
        {
            for(int j = 1; j <= w; j++)
            {
                int minDir = 0;

                for(int k = 1; k <= 4; k++)
                {
//                    printf("%d %d %d : %d < %d ?\n", i, j, k, att[i+dir[k][0]][j+dir[k][1]], att[i+dir[ptr[i][j]][0]][j+dir[ptr[i][j]][1]]);
                    if(att[i+dir[k][0]][j+dir[k][1]] < att[i+dir[minDir][0]][j+dir[minDir][1]])
                        minDir = k;
                        
                }
                setUnion(getPtr(i, j), getPtr(i+dir[minDir][0], j+dir[minDir][1]));
//                printf("%d ", minDir);
            }
//            printf("\n");
        }
        
        for(int i = 0; i < MS*MS; i++) idx[i] = 0;
        
        char c = 'a';
        printf("Case #%d:\n", tt);
        for(int i = 1; i <= h; i++)
        {
            for(int j = 1; j <= w; j++)
            {
                if(!idx[find(getPtr(i, j))])
                    idx[find(getPtr(i, j))] = (c++);

                printf("%c ", idx[find(getPtr(i, j))]);
            }
            printf("\n");
        }
    }

    return 0;
}
