#include <iostream>
#include <string>
#include <algorithm>
#include <map>
using namespace std;
#define tiao system("pause")


int t;
int n;
int a1, a2;
int b1, b2;
int f[1111111];

inline bool isOK(int i, int j)
{
    int cnt = 0;
    while(i != j)
    {
        j -= i;
        
        if (i > j) swap(i,j);
        
        if (2*i <= j) break;
        cnt++;
    }
    
    return cnt % 2 == 1;
}

int main(void)
{
    int i,j,k,ci,cici,cicici;
    
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);

    for (i=1; i<=1000000; i++)
    {
        int l = i;
        int r = 2*i; 
        int m;
        
        while(l + 1 < r)
        {
            m = (l + r) / 2;
            if (isOK(i,m)) r = m;
            else l = m;
        }
        f[i] = r;
    }

    cin >> t;
    for (cicici=1; cicici<=t; cicici++)
    {
        cin >> a1 >> a2 >> b1 >> b2;
        long long cnt = 0;
        
        for (i=a1; i<=a2; i++)
        {
            if (f[i] < b1) cnt += b2 - b1 + 1;
            else if (f[i] <= b2) cnt += b2 - f[i] + 1;
        }
        for (i=b1; i<=b2; i++)
        {
            if (f[i] < a1) cnt += a2 - a1 + 1;
            else if (f[i] <= a2) cnt += a2 - f[i] + 1;
        }
        cout << "Case #" << cicici << ": " << cnt << endl;
    }
    
//    tiao;
    return 0;
}
