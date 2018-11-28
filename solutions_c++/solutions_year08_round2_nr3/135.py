
#include <cstdio>
#include <algorithm>
using namespace std;

int ind [16384];
int used [16384];
int mark [16384];

int main ()
{
    int T;
    scanf ("%d", &T);
    for (int t = 0; t < T; ++t)
    {
//        printf ("HERE!\n");
        int K, n;
        scanf ("%d", &K);
        scanf ("%d", &n);
//        printf ("%d %d\n", K, n);
        for (int j = 0; j < n; ++j)
            scanf ("%d", &ind [j]);
        
        memset (mark, 0, sizeof (mark));
        memset (used, 0, sizeof (used));
        int at = -1;
        for (int i = 0; i < K; ++i)
        {
            int cnt = 0;
            while (true)
            {
                at = (at + 1) % K;
                if (!mark [at]) 
                {
                    //printf ("%d, ", at + 1);
                    ++cnt;
                }
                if (!used [cnt] && cnt > 0)
                {
                    mark [at] = cnt;
                    used [cnt] = true;
//                    printf ("mark [%d] = %d\n", at, cnt);
//                    printf ("BREAK!\n");
                    break;
                }
//                int c;
//                scanf ("%d", &c);
            }
        }
        
        printf ("Case #%d:", t + 1);
        for (int j = 0; j < n; ++j)
            printf (" %d", mark [ind [j] - 1]);
        puts ("");
        
//        for (int j = 0; j < K; ++j)
//            printf ("%d ", mark [j]);
//        puts ("");
//        printf ("PEDERAST!\n");
    }
    return 0;
}