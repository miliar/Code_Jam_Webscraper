#include <cstdio>
#include <string>
#include <list>
#include <vector>
#include <set>

using namespace std;

int L, D, N;

void parse(char *p, vector<set<char> >& c, int i)
{
    set<char> l;
    switch (*p)
    {
    case 0:
        return;
    case '(':
        ++p;
        while (*p != ')')
        {
            l.insert(*p);
            ++p;
        }
        ++p;
        break;
    default:
        l.insert(*p++);
    }
    c[i] = l;
    parse(p, c, i+1);
}

bool match(const string& s, const vector<set<char> >& c, int i)
{
    if (i >= L)
        return true;
    if (c[i].find(s[i]) == c[i].end())
        return false;
    return match(s, c, i + 1);
}

int main()
{
    scanf("%d%d%d\n", &L, &D, &N);

    vector<string> l;
    for (int i = 0; i < D; ++i)
    {
        char buf[1024];
        scanf("%s", buf);
        l.push_back(string(buf));
        //printf("%s\n", buf);
    }

    for (int i = 0; i < N; ++i)
    {
        vector<set<char> > c(L);
        
        char buf[1024];
        scanf("%s", buf);
        //printf("%s\n", buf);
        parse(buf, c, 0);

        int cnt = 0;
        for (int j = 0; j < D; ++j)
        {
            if (match(l[j], c, 0))
                cnt++;
        }
        printf("Case #%d: %d\n", i + 1, cnt);
    }
}
