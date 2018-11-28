#include <iostream>
#include <map>
#include <string>
#include <algorithm>
using namespace std;

int t, tt, k;
string s, s2;

void input()
{
    cin >> k >> s;
    //cout << k << s << endl;
} 

void solve()
{
    int a[16];
    for (int i = 0; i < k; i++) a[i] = i;
    int ans = 100000;
    do 
    {
        s2 = s;
        int len = s.length();
        for (int i = 0; i < len / k; i++)
        {
            for (int j = i * k; j < i * k + k; j++)
            {
                s2[j] = s[i * k + a[j - i * k]];
            }    
        }   
        int xx = 1;
        char pre = s2[0];
        for (int i = 1; i < len; i++)
        {
            if (s2[i] != pre) pre = s2[i], xx++;
        }  
        if (xx < ans) ans = xx;   
    }while (next_permutation(a, a + k));  
    printf("Case #%d: %d\n", t, ans); 
}  

int main()
{
    freopen("D-small-attempt0.in", "r", stdin);
    //freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &tt);
    for (t = 1; t <= tt; t++)
    {
        input();
        solve();
    } 
}    
