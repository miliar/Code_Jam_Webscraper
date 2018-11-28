#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <string>
#include <cstdlib>
#include <sstream>
#include <vector>
#include <algorithm>
#include <functional>
using namespace std;

const double PI = acos(-1.0);
const int MAXINT = 0x7FFFFFFF;
typedef long long int64;
const int64 MAXINT64 = 0x7FFFFFFFFFFFFFFFLL;

#define PS(x) (cout<<#x<<": "<<endl)
#define DB(x) (cout<<#x<<": "<<x<<endl)
#define MST(t,v) memset(t,v,sizeof(t))
#define SHOW1(a,n) (PS(a),_show1(a,n))
#define SHOW2(a,r,c) (PS(a),_show2(a,r,c))

template<class T>void _show1(T a, int n){for(int i=0; i<n; ++i) cout<<a[i]<<' '; cout<<endl;}
template<class T>void _show2(T a, int r, int l){for(int i=0; i<r; ++i)_show1(a[i],l);cout<<endl;}
template<class T> inline void CMAX(T &a,T b){if(b>a) a=b;} 
template<class T> inline void CMIN(T &a,T b){if(b<a) a=b;}

// 7427466391 第一个十位数的质数
//O(n)的筛选素数方法
//a[i]数组i的最小质因子（如果i为素数，a[i]等于0）
//p数组存放MAX以内的所有素数，pN为素数总数
#define MAX 1000000
int a[MAX]; 
int p[MAX]; 
int pN; 

// O(n)的算法 
void Prime2() {
    memset(a, 0, sizeof(a));
    int i, j, t;
    pN = 0;
    for(i = 2; i < MAX; ++i) {
        if(!a[i]) p[pN++] = i;
        for(j = 0;j < pN && i * p[j] < MAX && (p[j] <= a[i] || a[i] == 0); ++j)   
            a[i*p[j]] = p[j];
    }
} 

int N;
int Min, Max;
int main()
{
    freopen("C_S0.in", "r", stdin);freopen("C_S0.out", "w", stdout);
    //freopen("A-large.in", "r", stdin);freopen("A-large.out", "w", stdout);
    Prime2();
	int i, j, k;
    int T, cs = 0;
    scanf("%d", &T);
    while(T--)
    {
       scanf("%d", &N);
       Min = Max = 0;
       for(i = 0; i < pN; ++i)
       {
            j = 1;
            k = 0;
            while(j * p[i] <= N)
            {
                j *= p[i];
                k++;
            }
            if(k > 0)
            {
                Min += 1;
                Max += k;
            }
       }
       Max += 1;
       if(Min == 0) Min = 1;
       printf("Case #%d: %d\n", ++cs, Max - Min);
    }
	return 0;
}

