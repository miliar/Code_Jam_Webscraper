#include <algorithm>
#include <cmath>
#include <complex>
#include <cstdio>
#include <deque>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <vector>
#include <string>
#include <cstring>
using namespace std;
#define sz(x) (int)x.size()
char s[1024];
vector<int> ans;
bool vis[100000];
string toString(int n)  {
    stringstream ss;
    ss << n;
    string ans;
    ss >> ans;
    return ans;
}
void tran()  {
    ans.clear();
    for(int i = 0; s[i]; i++)  {
        if(isdigit(s[i]))  {
            int k = 0;
            int j = i;
            while(isdigit(s[j]))  {
                k = k * 10 + s[j] - '0';
                j++;
            }
            ans.push_back(k);
            if(s[j] == 0)  return;
            i = j;
        }
        
    }
}
int toInt(string s)  {
    int sum = 0;
    for(int i = 0; i < sz(s); i++)  sum = sum * 10 + s[i] - '0';
    return sum;
}
int toInt2(string s)  {
    int sum = 0;
    for(int i = 0; i < sz(s); i++)  sum += (s[i] - '0') * (s[i] - '0');
    return sum;
}
string tok(int n, int k)  {
    string str;
    while(n)  {
        char c = n % k + '0';
        str = c + str;
        n /= k;
    }
    return str;
}
bool well(int n, int k)  {
    if(n == 1)  return true;
    if(vis[n])  return false;
    //cout << n << ' ' << k << endl;
    vis[n] = 1;
    int tmp = toInt2(tok(n, k));
    string str = tok(tmp, k);
    int sum = toInt2(str);
    return well(sum, k);
}
bool ok(int n)  {
    //cout << n << endl;
    for(int i = 0; i < sz(ans); i++)  {
        memset(vis, 0, sizeof(vis));
        if(!well(n, ans[i]))  return false;
    }
    return true;
}
int main() {
    freopen("Asmall.out", "w", stdout);
	int t;
    scanf("%d\n", &t);
    int Case = 1;
    while(t--)  {
        
        gets(s);
        //cout << s << endl;
        tran();
        //for(int i = 0; i < sz(ans); i++)  cout << ans[i] << endl;
        int i;
        
        for(i = 2; ; i++)  if(ok(i))  break;

        printf("Case #%d: %d\n", Case++, i);
    }
    return 0;
}
