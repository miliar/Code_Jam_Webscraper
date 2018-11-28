#include <iostream>
#include <iomanip>
#include <algorithm>
#include <map>
#include <vector>

using namespace std;

struct path
{
    map<string, struct path *> son;
};

typedef struct path PT;


void createTree(PT &pt, string line)
{
    if(line.size() == 0) return;
    size_t found = line.find('/');
    if(found == string::npos)
    {
        if(pt.son.count(line) <= 0) pt.son[line] = new PT;
    }
    else
    {
        string now = line.substr(0, found);
        if(pt.son.count(now) <= 0)
        {
            PT *np = new PT;
            string rem = line.substr(found + 1);
            createTree(*np, rem);
            pt.son[now] = np;
        }
        else
        {
            createTree(*(pt.son[now]), line.substr(found + 1));
        }
    }
}

int fun(PT &pt, string line)
{
    if(line.size() == 0) return 0;
    size_t found = line.find('/');
    if(found == string::npos)
    {
        if(pt.son.count(line) > 0) return 0;
        else
        {
            pt.son[line] = new PT;
            return 1;
        }
    }
    else 
    {
        string now = line.substr(0, found);
        if(pt.son.count(now) <= 0)
        {
            PT *np = new PT;
            string rem = line.substr(found + 1);
            int re = 1 + fun(*np, rem);
            pt.son[now] = np;
            return re;
        }
        else
        {
            return fun(*(pt.son[now]), line.substr(found + 1));
        }
    }
}

int main(int argc, char *argv[])
{
    int T, N, M;
    cin >> T;
    string line;
    for(int ci = 1; ci <= T; ci++)
    {
        
        cin >> N >> M;
        getline(cin, line);
        PT pt;
        for(int i = 0; i < N; i++)
        {
            getline(cin, line);
            createTree(pt, line.substr(1));
        }
        int re = 0;
        for(int i = 0; i < M; i++)
        {
            getline(cin, line);
            re += fun(pt, line.substr(1));
        }
        cout << "Case #" << ci << ": " << re << endl;
    }
    return 0;
}
