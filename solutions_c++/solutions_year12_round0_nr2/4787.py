#include<cstdio>
using namespace std;
#define TUPLE 3

int T; 

int test_number(int t, int p, int *S, int count)
{
    int x = t / TUPLE;
    int y = t % TUPLE;

    // edge case 
    if (t < TUPLE)
    {
        if (p <= t)
        {
            if (t == 2 && p == 2)
            {
                if (*S <= 0)
                    return count;
                (*S)--;
            }
            return ++count;
        }
        // p > t
        return count;
    }

    // always will work
    if (x >= p)
        return ++count;
    // test if it will work
    else
    {
        if (p - x == 2) 
        {
            if (y == 2 && *S > 0)
            {
                (*S)--;
                return ++count;
            }
        }
        if (p - x == 1)
        { 
            if (y == 1 || y == 2)
                return ++count;

            if (y == 0 && *S > 0)
            {
                (*S)--;
                return ++count;
            }
        } 
        // p - x > 2, S <= 0, p-x==2 && y==[0|1]
        return count;
    }
    return count;
}

int main()
{
    freopen("B-large.in", "r", stdin);
    //freopen("B.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    scanf("%d", &T);

    for (int i = 0; i < T; i++)
    {
        int N, S, p;
        scanf("%d %d %d", &N, &S, &p);
        
        int num_people = 0;
        for (int j = 0; j < N; j++)
        {
            int t;
            scanf("%d", &t);

            //printf("S: %d\n", S);
            
            num_people = test_number(t, p, &S, num_people);
        }

        printf("Case #%d: %d\n", (i+1), num_people);
        
    }

    return 0;
}

