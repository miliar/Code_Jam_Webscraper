#include <cstdio>
#include <iostream>
#include <cmath>
#include <string>
#include <algorithm>
using namespace std;

double p[20];
double p1[2000];

void test1(int n)
{
    int a[10];
    for (int i = 0; i < n; i++)
    {
        a[i] = i + 1;
    }
    int all = 0;
    int y = 0;
    do
    {
        all++;
        for(int i = 0; i < n; i++)
        {
            if (a[i] == i + 1)
            {
                y++;
                break;
            }
        }
        
    }while(next_permutation(a,a + n));
    
    //printf("%d %d %.6lf\n", all, y, (double)all / y);
    p[n] = p[n-1] + (double)all / y;
    
    for(int i = 1; i <= n; i++)
    {
        printf("%d: %.6lf  ", i, p[i]);
    }
    printf("\n");
}

void test2(int n)
{
    int all = 0;
    
    int a[10];
    for (int i = 0; i < n; i++)a[i] = i + 1;
    do
    {
        all++;
    }while(next_permutation(a,a + n));
    
    for (int i = 0; i < n; i++)a[i] = i + 1;
    bool mk[11];
    
    int xall = 0;
    double ans = 0.0;
    do
    {
        memset(mk, false, sizeof mk);
        bool flag = false;
        for (int i = 0; i < n; i++)
        {
            if (!mk[i])
            {
                int k = a[i] - 1;
                int count = 1;
                mk[i] = true;
                while(!mk[k])
                {
                    mk[k] = true;
                    count++;
                    k = a[k] - 1;
                }
                if (count < n)
                {
                    flag = true;
                    ans = ans + p1[count];
                }
            }
        }
       
        if (flag)xall++;
        
    }while(next_permutation(a,a + n));
    p1[n] = (double)ans / xall + (double)all / xall;
    
    /*
    for(int i = 1; i <= n; i++)
    {
        printf("%d: %.6lf  ", i, p1[i]);
    }
    printf("\n");
    printf("\n");
    */
}

void solve()
{
    int n;
    cin >> n;
    int a[1010];
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
        //cout << a[i] << ' ';
    }
    //cout << endl;
    int all = 0;
    double ans = 0.0;
    bool mk[1010];
    memset(mk, false, sizeof mk);
    for (int i = 0; i < n; i++)
    {
        if (!mk[i])
        {
            int k = a[i] - 1;
            int count = 1;
            mk[i] = true;
            while(!mk[k])
            {
                mk[k] = true;
                count++;
                k = a[k] - 1;
            }
            ans = ans + p1[count];
        }
    }
    printf("%.6lf\n", ans);
    //cout << endl;
}

int main() {
    
    freopen("D-large.in", "r", stdin);
    freopen("D.out", "w", stdout);
    
    p[1] = 0.0;
    p[2] = 2.0;
    p1[2] = 2.0;
    p1[1] = 0.0;
    for (int i = 3; i <= 1000; i++)
    {
       // test1(i);
        p1[i] = (double)i;
    }
    //return 0;
    
    int T;
    scanf("%d", &T);
    
    for (int i = 1; i <= T; i++)
    {
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}
