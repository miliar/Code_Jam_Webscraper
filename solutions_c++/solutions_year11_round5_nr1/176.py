#include<cstdio>
#include<cstdlib>
#include<vector>
#include<string>
#include<sstream>
#include<iostream>
#include<algorithm>

using namespace std;

double upper[1100];
double bottom[1100];
double diff[1100];
double size[1100];
int segsx[110];
int segsy[110];
int w;

int main()
{
    int teste, t;
    scanf("%d", &teste);
    for (t=0; t<teste; t++)
    {
        int n, m, g;
        scanf("%d %d %d %d", &w, &n, &m, &g);

        int i;
        int last;
        last = 1;
        scanf("%d %d", &segsx[0], &segsy[0]);
        bottom[0] = segsy[0];
        for (i = 1; i < n; i++)
        {
            scanf("%d %d", &segsx[i], &segsy[i]);
            for (; last <= segsx[i]; last++)
            {
                bottom[last] = segsy[i-1] + (double)((last - segsx[i-1]) * (segsy[i] - segsy[i - 1]))/(segsx[i] - segsx[i-1]);
            }
        }

        last = 1;
        scanf("%d %d", &segsx[0], &segsy[0]);
        upper[0] = segsy[0];
        for (i = 1; i < m; i++)
        {
            scanf("%d %d", &segsx[i], &segsy[i]);
            for (; last <= segsx[i]; last++)
            {
                upper[last] = segsy[i-1] + (double)((last - segsx[i-1]) * (segsy[i] - segsy[i - 1]))/(segsx[i] - segsx[i-1]);
            }
        }

        for (i = 0; i <= w; i++)
        {
            diff[i] = upper[i] - bottom[i];
        }

        size[0] = 0;
        for (i = 1; i <= w; i++)
        {
            size[i] = size[i-1] + (diff[i] + diff[i-1])/2;
        }

        printf("Case #%d:\n", t+1);
        for (i = 1; i < g; i++)
        {
            double target = size[w]/g*i;
            double a = 0;
            double b = w;
            double c;
            for (int j = 0; j < 1000; j++)
            {
                c = (a + b) / 2;
                int part = (int)c;
                double diffc = diff[part] + (c - part) * (diff[part + 1] - diff[part]);
                double calc = size[part] + (c - part) / 2 * (diff[part] + diffc);
                if (calc > target)
                {
                    b = c;
                }
                else
                {
                    a = c;
                }
            }
            printf("%lf\n", c);
        }
    }
    return 0;
}
