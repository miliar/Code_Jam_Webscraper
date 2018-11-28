#include <iostream>
#include <algorithm>
#include <string>
#include <cstdio>

using namespace std;

int sum(int n)
{
    int ans = 0;
    for(int i = 1; i < n; i++)
        ans += i;
}

bool ok(string a, string b)
{
    string t;
    if(a.length() != b.length()) return 0;
    int len = b.length();
    b += b;
    for(int i = 0; i < len; i++)
    {
        t= "";
        for(int j = i; j < i+len; j++)
            t += b[j];
        if(t == a) return 1;
    }
    return 0;
}

int main()
{
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    int t;
    int a,b,n,m,ans = 0;
    cin>>t;
    for(int i = 0; i < t; i++)
    {
        ans = 0;
        string s1,s2;
        cin>>a>>b;
        for(int j = a; j < b; j++)
        {

            s1 ="";
            s2 ="";
            int temp = j;
            while(temp)
                s1 += temp%10+48,
                temp/=10;
            reverse(s1.begin(),s1.end());
            for(int k = j+1; k <= b; k++)
            {
                s2 = "";
                temp = k;
                while(temp)
                    s2 += temp%10+48,
                    temp /= 10;
                reverse(s2.begin(),s2.end());
                if(ok(s1,s2)) ans++;
            }
        }
        cout<<"Case #"<<i+1<<": "<<ans<<endl;
    }

return 0;
}
