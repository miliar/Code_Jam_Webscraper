#include <cstdio>

int count_recycled_numbers(int A, int B);

int main()
{
    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; i++)
    {
        int A, B;
        scanf("%d %d", &A, &B);
        printf("Case #%d: ", i);
        int answer = count_recycled_numbers(A, B);
        printf("%d\n", answer);
    }
    return 0;
}

int count_recycled_numbers(int A, int B)
{
    int cnt = 0;
    int X = 10;
    for (; X <= A; X *= 10);
    int pair_number[7];
    int pair_size;
    for (int i = A; i <= B; i++)
    {
        pair_size = 0;
        for (int base = 10; base < i; base *= 10)
            if (i % base / (base / 10) != 0)
            {
                int back = i % base;
                int front = i / base;
                int temp = back * X / base + front;
                
                //printf("X = %d, base = %d\n", X, base);
                //printf("(%d, %d) %d, %d\n", i, temp, back, front);
                
                bool flag = false;
                for (int j = 0; j < pair_size; j++)
                    if (pair_number[j] == temp)
                    {
                        flag = true;
                        break;
                    }
                if (flag) continue;
                
                if (i < temp && temp <= B)
                {
                    //printf("(%d, %d)\n", i, temp);
                    pair_number[pair_size++] = temp;
                    cnt++;
                }
            }
    }
    return cnt;
}