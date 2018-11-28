#include <iostream>
#include <cstdio>
#include <cstring>
#include <string.h>
#include <sstream>

using namespace std;

FILE* out = fopen("output.txt", "w");

string to_str(int x)
{
    stringstream ss;
    ss << x;
    return ss.str();
}

void solve(int x)
{
    int a, b;
    scanf("%d %d", &a, &b);

    string num1, num2;
    int c = a;
    int l=0;
    while(c)
    {
        c /= 10;
        ++l;
    }
    int ans=0;

    for(int m = a; m <= b; ++m)
    {
        num1 = to_str(m);
        for(int n = m+1; n <= b; ++n)
        {
            bool fin = false;
            num2 = to_str(n);

            for(int i = 1; i < l; ++i)
            {
                bool temp = true;
                int cur=0;
                int start = l-i;
                for(int j = start; j < l; ++j)
                {
                    if(num1[j] != num2[cur])
                    {
                        temp = false;
                        break;
                    }
                    ++cur;
                }

                if(temp)
                {
                    for(int j = 0; j < start; ++j)
                    {
                        if(num1[j] != num2[cur])
                        {
                            temp = false;
                            break;
                        }
                        ++cur;
                    }
                }

                fin = temp;
                if(fin)
                    break;
            }

            if(fin)
                ++ans;
        }
    }

    fprintf(out, "Case #%d: %d\n", x, ans);
}

int main()
{
    int t;
    cin >> t;
    for(int i = 1; i <= t; ++i)
        solve(i);

    return 0;
}
