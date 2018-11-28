#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

bool recycle(int n, int m);
void cycle(string &s);

int main()
{
    int T, A, B, count;

    cin >> T;

    for (int Ti = 1; Ti <= T; Ti++)
    {
        cin >> A >> B;
        count = 0;
        for (int n = A; n < B; n++)
        {
            for (int m = n+1; m <= B; m++)
            {
                if (recycle(n,m))
                    count++;
            }
        }

        cout << "Case #" << Ti << ": " << count << endl;
    }

    return 0;
}

void cycle(string &s)
{
    char c = s[0];
    for (int i = 0; i + 1 < s.length(); i++)
    {
        s[i] = s[i+1];
    }
    s[s.length() - 1] = c;
}

bool recycle(int n, int m)
{
    char s1[5];
    char s2[5];
    sprintf(s1,"%d",n);
    sprintf(s2,"%d",m);
    
    string s(s1);
    string t(s2);
    for (int i = 1; i < s.length(); i++)
    {
        cycle(s);
        if (s == t)
            return true;
    }
    return false;
}
