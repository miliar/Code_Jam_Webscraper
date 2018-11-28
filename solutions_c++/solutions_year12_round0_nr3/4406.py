#include <iostream>
#include <cstring>
#include <map>
using namespace std;

string tos(int value)
{
    string res = "";
    while (value)
    {
        res += '0' + value % 10;
        value /= 10;
    }
    reverse(res.begin(), res.end());
    return res;
}

bool isRecycle(const string a, const string b)
{
    for (int i=0; i < a.length(); ++i)
    {
        bool isOk = true;
        for (int j=0; j < a.length(); ++j)
        {
            int p = (j+i) % a.length();
            if (a[j] != b[p])
            {
                isOk = false;
                break;
            }
        }
        if (isOk) return true;
    }
    return false;
}

int main()
{    
    int Q;
    cin >> Q;
    for (int ct=0; ct < Q; ++ct)
    {
        int a, b;
        cin >> a >> b;

        int ans = 0;
        for (int i=a; i <= b; ++i)
        {
            for (int j=i+1; j <=b; ++j)
            {
                ans += isRecycle(tos(i), tos(j));
            }
        }
        
        cout << "Case #" << ct+1 << ": " << ans << endl;
    }
    
    return 0;
}
