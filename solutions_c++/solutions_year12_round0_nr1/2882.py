#include <iostream>
#include <string>
#include <map>

using namespace std;

map<char, char> mapper;

void cal(string a, string b)
{
    for (size_t i = 0; i < a.size(); i++)
    {
        mapper[a[i]] = b[i];
    }
}

char find(string a)
{
    int mk[26] = {0};
    for (size_t i = 0; i < a.size(); i++)
    {
        mk[a[i] - 'a'] = 1;
    }
    
    for (int i = 0; i < 26; i++)
    {
        if (mk[i] == 0)
        {
            return i + 'a';
        }
    }
}

void init()
{
    string b1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
    string e1 = "our language is impossible to understand";
    string b2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
    string e2 = "there are twenty six factorial possibilities";
    string b3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
    string e3 = "so it is okay if you want to just give up";
    
    string aa = b1 + b2 + b3 + "z";
    string bb = e1 + e2 + e3 + "q";
    
    mapper.clear();
    
    mapper['z'] = 'q';
    cal(b1, e1), cal(b2, e2), cal(b3, e3);
    mapper[find(aa)] = find(bb);
}

string change(string a)
{
    string b;
    for (size_t i = 0; i < a.size(); i++)
    {
        b += mapper[a[i]];
    }
    return b;
}

void run()
{
    string line;
    getline(cin, line);
    cout << change(line) << endl;
}

int main()
{
    freopen("A-small-attempt2.in", "r", stdin);
    freopen("a.out", "w", stdout);
    
    init();
    int N = 0;
    scanf("%d", &N);
    getchar();
    for (int k = 1; k <= N; k++)
    {
        printf("Case #%d: ", k);
        run();
    }
    return 0;
}
