#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>


using namespace std;


char cc[130][130];
bool dd[130][130];

int main()
{
    freopen("input.txt","r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    cin >> t;
    for(int ti = 0; ti < t; ++ti)
    {
        int c;
        cin >> c;
        memset(cc, 0, sizeof(cc));
        while(c --)
        {
            string word;
            cin >> word;
            cc[word[0]][word[1]] = cc[word[1]][word[0]] = word[2];
        }
        int d;
        cin >> d;
        memset(dd, 0, sizeof(dd));
        while(d --)
        {
            string word;
            cin >> word;
            dd[word[0]][word[1]] = dd[word[1]][word[0]] = true;
        }
        int n;
        cin >> n;
        string s;
        cin >> s;
        for(int i = 0; i < s.length(); ++i)
        {
            if(i == 0)
                continue;
            if(cc[s[i]][s[i - 1]])
            {
                s[i] = cc[s[i]][s[i - 1]];
                s.erase(i - 1, 1);
                i --;
            }
            for(int j = 0; j < i; ++j)
            {
                if(dd[s[j]][s[i]])
                {
                    s.erase(0, i + 1);
                    i = -1;
                    break;
                }
            }
        }
        cout << "Case #" << ti + 1 << ": [";
        for(int i = 0; i < s.length(); ++i)
        {
            if(i)
                cout << ", ";
            cout << s[i];
        }
        cout << "]" << endl;
    }

    return 0;
}
