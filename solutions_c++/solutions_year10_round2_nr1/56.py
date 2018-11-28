#include <iostream>
#include <vector>
#include <string>
#include <deque>
#include <algorithm>
#include <map>
#include <set>
#include <list>

struct Path;
typedef std::map<std::string, Path*> Dirs;

struct Path
{
    Dirs dirs;

    ~Path()
    {
        for (Dirs::iterator d = dirs.begin() ; d != dirs.end() ; ++d)
            delete d->second;
    }

    int count()
    {
        int res = 1;
        for (Dirs::iterator d = dirs.begin() ; d != dirs.end() ; ++d)
            res += d->second->count();

        return res;
    }

    void addDir(const char *dir)
    {
        if (!*dir)
            return;
        std::string name;
        for (++dir ; *dir && *dir != '/' ; ++dir)
            name += *dir;
        if (!dirs[name])
            dirs[name] = new Path;
        dirs[name]->addDir(dir);
    }
};

int main()
{
    int T;
    std::cin >> T;
    for (int t = 1 ; t <= T ; ++t)
    {
        Path root;
        std::cout << "Case #" << t << ": ";
        int n, m;
        std::cin >> n >> m;
        std::string dir;
        for (int i = 0 ; i < n ; ++i)
        {
            std::cin >> dir;
            root.addDir(dir.c_str());
        }
        int count = -root.count();
        for (int i = 0 ; i < m ; ++i)
        {
            std::cin >> dir;
            root.addDir(dir.c_str());
        }
        count += root.count();
        std::cout << count << "\n";
    }
    return 0;
}
