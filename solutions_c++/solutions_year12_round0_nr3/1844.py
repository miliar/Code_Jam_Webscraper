#include <cstdio>
#include <cstring>
#include <bitset>

const int BIT_SET_SIZE = 2000000 +1;

int base[] = {1, 10, 100, 1000, 10000, 100000, 1000000, 10000000};

inline int
get_bits(int num)
{
    int bits = 0;
    while (num)
    {
        bits++;
        num = num / 10;
    }
	return bits;
}

inline int
next_num(int num, int bits)
{
    return num / 10 + (num % 10) * base[bits - 1];
}

int
calc(int n)
{
    if (n == 1)
        return 0;
    else
        return n * (n-1) / 2;
}

int
main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);

//    init();
//    print();

    std::bitset<BIT_SET_SIZE> my_set;

    int T;
    scanf("%d", &T);
    for (int case_i = 1; case_i <= T; case_i++)
    {
        int A, B;
        scanf("%d %d", &A, &B);
        my_set.reset();
        int result = 0;
        for (int i = A; i <= B; i++)
        {
            if (my_set.test(i))
                continue;

            int start = i;
            int cur = start;
            int cnt = 1;
			int bits = get_bits(start);
            my_set.set(start);
            while ((cur = next_num(cur, bits)) != start)
            {
                if (cur >= A && cur <= B &&
                    !my_set.test(cur))
                {
                    cnt++;
                    my_set.set(cur);
                }
            }
            result += calc(cnt);
        }
        printf("Case #%d: %d\n", case_i, result);
    }

    return 0;
}
