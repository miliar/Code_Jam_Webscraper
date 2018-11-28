#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

int prison [200]; // 0 = there, 1 = released
int released [200]; // permutation array
int main ()
{

    int N;

    // input output streams
    freopen ("C-small-attempt0.in", "r", stdin);
    //freopen ("input2.txt", "r", stdin);
    freopen ("output.txt", "w", stdout);

    // number of cases
    scanf ("%d", &N);
    if (N < 1)
        printf ("Error: input file not found\n");

    // for each case
    for (int caseId=1; caseId<=N; caseId++)
    {
        int P, Q;
        scanf ("%d%d", &P, &Q);
        for (int i=0; i<Q; i++)
        {
            int rel;
            scanf ("%d", &rel);
            released[i] = rel-1; // asc
        }
        int min = -1;
        do
        {
int count = 0;
            for (int i=0; i<P; i++)
            {
                prison[i] = 0;
            }
            for (int i=0; i<Q; i++)
            {
                prison[released[i]]=1;
                int left = 0;
                if(released[i]>0)
                {
                    int ptr=released[i]-1;
                    //printf ("ptr %d\n", ptr);
                    while (prison[ptr] == 0)
                    {
                        left++;
                        if (ptr==0) break;
                        ptr--;
                    }
                }
                int right = 0;
                if(released[i]<P-1)
                {
                    int ptr=released[i]+1;
                    while (prison[ptr] == 0)
                    {
                        right++;
                        if (ptr==P-1) break;
                        ptr++;
                    }
                }
                //printf ("%d %d\n", left, right);
                count+=left+right;
            }
//printf ("%d\n", count);
            if (min==-1) min = count;
            else if (count < min) min = count;
        }
        while (next_permutation(released, released + Q));



        printf ("Case #%d: %d\n", caseId, min);
    }
    return 0;
}

