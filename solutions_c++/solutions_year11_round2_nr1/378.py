#include <vector>
#include <utility>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <stack>
#include <queue>
#include <string>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <list>
#include <bitset>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> vint;
typedef vector<string> vstr;
typedef pair<int, int> pint;

#define TWO(k)  (1<<k)
#define TWOL(k) (((LL)(1)<<(k)))
#define MP make_pair
#define MIN(a,b) ( (a)<(b)?(a):(b) )
#define MAX(a,b) ( (a)>(b)?(a):(b) )
#define LS(x) 	 ((x)<<1)
#define RS(x) 	 (((x)<<1)+1)

const double PI = acos(-1.0);
const double EPS = 1e-9;
const int oo = 210000000;
const int Max = 110;

char a[Max][Max];
int n;

int main()
{
    //freopen("E:/in.txt","r",stdin);freopen("E:/out.txt","w",stdout);
    //freopen("A-large.in","r",stdin);freopen("E:/out.txt","w",stdout);
    int t, test = 0;
    scanf("%d", &t);
    while(t--)
    {
        printf("Case #%d:\n", ++test);
        scanf("%d", &n);
        for(int i = 1; i <= n; i++) scanf("%s", a[i]);
        double wp[Max], owp[Max], oowp[Max];
        double ans[Max];
        int num[Max] = {0}, win[Max] = {0};
        for(int i = 1; i <= n; i++)
        {
            for(int j = 1; j <= n; j++)
            {
                if( a[i][j-1] != '.') num[i]++;
                if( a[i][j-1] == '1') win[i]++;
            }
        }
        for(int i = 1; i <= n; i++)
        {
            wp[i] = ( 1.0 * win[i]) / num[i];
            double sum = 0;
            for(int j = 1; j <= n; j++)
            {
                if( j != i && a[i][j-1] != '.')
                {
                    int tmp1, tmp2;
                    if( a[i][j-1] != '.') 
                    {
                        tmp1 = num[j] - 1;
                        if( a[i][j-1] == '0') tmp2 = win[j] - 1;
                        else tmp2 = win[j];
                    }
                    else 
                    {
                        tmp1 = num[j];
                        tmp2 = win[j];
                    }
                    sum += ( 1.0 * tmp2) / tmp1;
                }
            }
            owp[i] = sum / ( 1.0 * num[i]);
        }
        for(int i = 1; i <= n; i++)
        {
            double sum = 0;
            for(int j = 1; j <= n; j++)
            {
                if(j != i && a[i][j-1] != '.') sum += owp[j];
            }
            oowp[i] = sum / ( 1.0 * num[i]);
        }/*
        for(int i = 1; i <= n; i++)
        { printf("%.5f ", wp[i]);
        }printf("\n");
        for(int i = 1; i <= n; i++)
        { printf("%.5f ", owp[i]);
        }printf("\n");
        for(int i = 1; i <= n; i++)
        { printf("%.5f ", oowp[i]);
        }printf("\n");*/
        for(int i = 1; i <= n; i++)
        {
            ans[i] = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i];
        }
        for(int i = 1; i <= n; i++)
        {
            printf("%.7f\n", ans[i]);
        }
    }

    return(0);
}

