#include<cstdio>
#include<utility>
#include<algorithm>

#define N 1010

int t;
int n;
std::pair<int,int> cables[N];

int calc()
{
    int i,j;
    scanf("%d", &n);
    for(i=0; i<n; i++)
    {
        scanf("%d%d", &cables[i].first, &cables[i].second);
    }

    int res=0;
    for(i=0; i<n; i++)
    {
        for(j=i+1; j<n; j++)
        {
            if((cables[i].first<cables[j].first && cables[i].second>cables[j].second) || (cables[i].first>cables[j].first && cables[i].second<cables[j].second))
            {
                //printf("%d/%d with %d/%d\n", cables[i].first, cables[i].second, cables[j].first, cables[j].second);
                ++res;
            }
        }
    }

    return res;
}

int main()
{
    int i,j;

    scanf("%d", &t);

    for(i=0; i<t; i++)
    {
        printf("Case #%d: %d\n", i+1, calc());
    }

    return 0;
}
