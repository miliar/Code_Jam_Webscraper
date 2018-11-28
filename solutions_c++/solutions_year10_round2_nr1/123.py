#include <cstdio>

#include <string>
#include <map>
#include <vector>

using namespace std;

typedef vector<string> TPath;

class TTreeItem {
public:
    typedef map<string, TTreeItem*> TChildren;
    TChildren Children;
    bool Before;

    void Add(const TPath& path, size_t index, bool before) {
        if (index < path.size()) {
            TChildren::const_iterator toChild = Children.find(path[index]);
            if (toChild == Children.end()) {
                TTreeItem* nw = new TTreeItem();
                nw->Before = before;
                Children.insert( TChildren::value_type(path[index], nw) );
                toChild = Children.find(path[index]);
            }
            toChild->second->Add(path, index + 1, before);
        }
    }

    ~TTreeItem() {
        for (TChildren::const_iterator toChild = Children.begin(); toChild != Children.end(); ++toChild)
            delete toChild->second;
    }

    int Count() const {
        int res = (Before) ? 0 : 1;
        for (TChildren::const_iterator toChild = Children.begin(); toChild != Children.end(); ++toChild)
            res += toChild->second->Count();
        return res;
    }
};

void Split(const string& s, TPath* result) {
    result->clear();
    size_t begin = 0;
    for (size_t i = 1; i < s.length(); ++i) {
        if (s[i] == '/') {
            result->push_back( s.substr(begin, i - begin) );
            begin = i;
        }
    }
    result->push_back( s.substr(begin, s.length() - begin) );
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int nT;
    scanf("%d", &nT);
    for (int test = 0; test < nT; ++test) {
        int n, m;
        scanf("%d%d", &n, &m);
        TTreeItem root;
        root.Before = true;
        for (int i = 0; i < n + m; ++i) {
            char buffer[1000];
            scanf("%s", buffer);
            TPath path;
            Split(buffer, &path);
            root.Add(path, 0, i < n);
        }
        printf("Case #%d: %d\n", test + 1, root.Count());
    }

    return 0;
}
