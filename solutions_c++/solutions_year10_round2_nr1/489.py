#include <iostream>
#include <set>
#include <string>

using namespace std;

int how_many_create(set<string>& existing, const string& dir)
{
    int pos = dir.size() - 1;
    int ret = 0;
    pos = dir.find_last_of('/', pos);
    string parent = dir.substr(0, pos);
    if (parent.size() > 0 && existing.find(parent) == existing.end()) {
        ret += how_many_create(existing, parent);
    }
    if (existing.find(dir) == existing.end()) {
        existing.insert(dir);
        ret += 1;
    }
    return ret;
}



int main(void)
{
    int no_cases = 0;
    cin >> no_cases;
    for (int c = 1; c <= no_cases; ++c) {
        int already = 0, to_create = 0;
        cin >> already;
        cin >> to_create;

        set<string> existing;
        for (int a = 0; a < already; ++a) {
            string dir;
            cin >> dir;
            existing.insert(dir);
        }
        int created = 0;
        for (int tc = 0; tc < to_create; ++tc) {
            string dir;
            cin >> dir;
            created += how_many_create(existing, dir);
        }
        cout << "Case #" << c << ": " << created << endl;
    }
}
