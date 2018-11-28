#include<cstdio>
#include<cstdlib>
#include<vector>
#include<string>
#include<sstream>
#include<iostream>
#include<algorithm>

using namespace std;

int cards[11000];
int n;
int queue[1100];
int pos;
int size;

int main()
{
    int teste, t;
    scanf("%d", &teste);
    for (t=0; t<teste; t++)
    {
        scanf("%d", &n);

        if (n == 0)
        {
            printf("Case #%d: 0\n", t+1);
        }
        else
        {
            int i;
            int start = 10001;
            int end = -1;
            for (i = 0; i <= 10000; i++)
            {
                cards[i] = 0;
            }
            for (i = 0; i < n; i++)
            {
                int a;
                scanf("%d", &a);
                cards[a]++;
                if (start > a)
                    start = a;
                if (end < a)
                    end = a;
            }

            int worst = 11000;
            pos = 0;
            size = 0;
            end++;
            for (i = start; i <= end; i++)
            {
                if (size - pos < cards[i])
                {
                    while(size - pos < cards[i])
                    {
                        queue[size++] = i;
                    }
                }
                else if (size - pos > cards[i])
                {
                    while(size - pos > cards[i])
                    {
                        int s = i - queue[pos++];
                        if (worst > s)
                            worst = s;
                    }
                }
            }

            printf("Case #%d: %d\n", t+1, worst);
        }
    }
    return 0;
}
