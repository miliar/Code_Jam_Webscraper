#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
#define tiao system("pause")

int r;
int k;
int n;
int t;
int hash[1111];
long long money[1111];
int start[1111];
int g[1111];
int pos;

void calc(int start, long long& money, int& next)
{
    long long cnt = 0;
    int cb = 0;
    int i;
    for (i=start; ; i=(i+1)%n)
    {
        if (cnt + g[i] > k) break;
        cb++;
        if (cb > n) break;
        
        cnt += g[i];
    }
    
    money = cnt;
    next = i;
}

int main(void)
{
    int i,j,ci,cici,cicici;
    
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    
    cin >> t;
    for (cicici=1; cicici<=t; cicici++)
    {
        memset(hash, 0, sizeof(hash));
        memset(money, 0, sizeof(money));
        memset(start, 0, sizeof(start));
        
        cin >> r >> k >> n;
        for (i=0; i<n; i++) cin >> g[i];
        
        int Start = 0;
        pos = 0;
        while(1)
        {
            int Next;
            long long Money;
            calc(Start, Money, Next);
            
            pos++;
            money[pos] = Money;
            start[pos] = Start;
            hash[Start] = true;
            
            if (hash[Next]) // 重复的这一位存一下~ 
            {
                pos++;
                start[pos] = Next;
                break;
            }
            Start = Next;
        }
    
        int pre;
        for (pre=1; pre<pos; pre++)
            if (start[pre] == start[pos]) break;

//cout << pre << ' ' << pos << endl;
    
        long long ans = 0;
        if (r <= pre)
        {
            for (i=1; i<=r; i++) ans += money[i];
        }
        else
        {
            for (i=1; i<pre; i++) ans += money[i];
            long long wb = 0;
            for (i=pre; i<pos; i++) wb += money[i];
            r -= pre - 1;
            ans += (long long)(r / (pos - pre)) * wb;
            for (i=pre; i<pre+(r % (pos - pre)); i++) ans += money[i];
        }
        
        cout << "Case #" << cicici << ": " << ans << endl;
    }
//    tiao;
    return 0;
}
