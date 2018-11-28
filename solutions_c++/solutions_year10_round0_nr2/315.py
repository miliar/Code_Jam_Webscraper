#include <iostream>
#include <vector>
#include <fstream>
#include <string>

using namespace std;

int C, N;

const int MAX = 60;

struct bigint
{
    int len;
    int d[MAX];
};

vector<bigint> T;

bool smaller(bigint a, bigint b)
{
    if (a.len != b.len) return (a.len < b.len);
    int k = a.len-1;
    while (k >= 0 && a.d[k] == b.d[k]) k--;
    return (k >= 0 && a.d[k] < b.d[k]);
}

bigint subtract(bigint a, bigint b)
{   
    bigint c;
    c.len = a.len;
    for (int i = 0; i < MAX; i++) c.d[i] = 0;
    int s = 0;
    for (int i = 0; i < c.len; i++)
        if (a.d[i]-s < b.d[i])
        {
            c.d[i] = 10+a.d[i]-b.d[i]-s;
            s = 1;
        }
        else
        {
            c.d[i] = a.d[i]-b.d[i]-s;
            s = 0;
        }
    while (c.len > 0 && c.d[c.len-1] == 0) c.len--;
    return c;
}

bigint findmod(bigint a, bigint b)
{
    if (a.len < b.len) return a;
    int k = a.len-b.len;
    bigint rest;
    rest.len = b.len-1;
    for (int i = 0; i < rest.len; i++) rest.d[i] = a.d[i+k+1];
    for (int i = rest.len; i < MAX; i++) rest.d[i] = 0;
    while (k >= 0)
    {
        while (!smaller(rest, b)) rest = subtract(rest, b);
        bigint restnew;
        restnew.len = rest.len+1;
        for (int i = 1; i < restnew.len; i++) restnew.d[i] = rest.d[i-1];
        for (int i = restnew.len; i < MAX; i++) restnew.d[i] = 0;
        restnew.d[0] = a.d[k];
        while (restnew.len > 0 && restnew.d[restnew.len-1] == 0) restnew.len--;
        rest = restnew;
        k--;
    }
    while (!smaller(rest, b)) rest = subtract(rest, b);
    return rest;
}

bigint findgcd(bigint a, bigint b)
{
    if (a.len == 0) return b;
    if (smaller(b, a)) return findgcd(b, a);
    return findgcd(a, findmod(b, a));
}

string printnum(bigint a)
{
    if (a.len == 0) 
        return "0";
    else
    {
        string s = "";
        for (int i = a.len-1; i>=0; i--) s += char('0'+a.d[i]);
        return s;
    }
}

int main()
{
    ifstream input("B-large.in");
    ofstream output("B-large.out");
    input >> C;
    
    for (int cc = 0; cc < C; cc++)
    {
        input >> N;
        T.resize(N);
        for (int i = 0; i < N; i++)
        {
            string s;
            input >> s;
            bigint cur;
            cur.len = s.length();
            for (int j = 0; j < MAX; j++) cur.d[j] = 0;
            for (int j = 0; j < cur.len; j++) cur.d[j] = s[cur.len-1-j]-'0';
            T[i] = cur;
        }
    
        bigint gcd;
        gcd.len = 0;
        for (int j = 0; j < MAX; j++) gcd.d[j] = 0;
        for (int i = 1; i < N; i++)
        {
            if (smaller(T[i-1], T[i]))
                gcd = findgcd(gcd, subtract(T[i], T[i-1]));
            else
                gcd = findgcd(gcd, subtract(T[i-1], T[i]));
        }
        
        bigint ans = findmod(T[0], gcd);
        if (ans.len > 0) ans = subtract(gcd, ans);
        output << "Case #" << cc+1 << ": " << printnum(ans) << endl;
    }
    input.close();
    output.close();
    return 0;
}
