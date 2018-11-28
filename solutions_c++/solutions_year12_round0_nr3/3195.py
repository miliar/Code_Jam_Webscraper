#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>
using namespace std;

int a, b;
long long ans;

string toString(int x)
{
    string str = "";
    while (x)
    {
        str = (char)(x%10 + '0') + str;
        x /= 10;
    }
    return str;
}
int toInt(const string s)
{
    int a = 0;
    for (int i = 0; i < s.length(); i++)
    {
        a *= 10;
        a += s[i] - '0';
    }
    return a;
}
inline void cycle(string &str)
{
    str += str[0];
    str.erase(0, 1);
}
int work(int num)
{
    string str = toString(num);
    int temp;
    for (int i = 1; i < str.size(); i++)
    {
        cycle(str);
        if (str[0] == '0') continue;
        temp = toInt(str);
        if (temp > num && temp <= b)
        {
            ans++;
        }
    }
}
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("codejamout.txt","w",stdout);
    int t;
    cin >> t;
    for (int tcase = 1; tcase <= t; tcase++)
    {
        scanf("%d%d", &a, &b);
        ans = 0;
        for (int i = a; i <= b; i++)
        {
            work(i);
        }
        printf("Case #%d: %d\n", tcase, ans);
    }
    fclose(stdout);
    return 0;
}
