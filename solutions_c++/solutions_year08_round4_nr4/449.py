#include <iostream>
#include <string>

using namespace std;

int k;
string st;
int perm[16];
bool used[16];
int minn;
const char *s;
unsigned int len;

void solve(int x)
{
    if (x == k)
    {
        int count = 0;
        char last = ';';
        int index = 0;
        int index2 = 0;
        for (unsigned int i = 0; i < len; i++)
        {
            char next = s[index2 + perm[index]];
            if (next != last)
            {
                count++;
                last = next;
            }
            index++;
            if (index == k)
            {
                index = 0;
                index2 += k;
            }
        }
        if (count < minn)
            minn = count;
    }
    else
    {
        for (int i = 0; i < k; i++)
            if (!used[i])
            {
                used[i] = true;
                perm[x] = i;
                solve(x + 1);
                used[i] = false;
            }
    }
}

int main()
{
    int n;
    cin >> n;
    for (int c = 1; c <= n; c++)
    {
        cin >> k >> st;
        s = st.c_str();
        len = st.length();
        minn = len + 1;
        for (int x = 0; x < k; x++)
            used[x] = false;
        solve(0);
        cout << "Case #" << c << ": " << minn << endl;
    }
    return 0;
}
