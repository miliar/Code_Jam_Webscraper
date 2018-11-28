#include <iostream>
#include <vector>
#include <string>
#include <set>

using namespace std;

#define REP(i,n) FOR(i,0,n)
#define FOR(i,a,b) for (int i = a; i < b; i++)

int tree_insert (set<string> & tree, string path);

int main() {
    int t, n, m;
    long long int ans;
    string path;
    set<string> tree;

    cin >> t;
    REP(z,t) {
        ans = 0;
        cin >> n >> m;

        tree.clear();
        REP(i,n) {
            cin >> path;
            tree.insert(path);
        }

 //       set<string>::iterator iter;
  //      cout << "de\n";
  //      for (iter = tree.begin(); iter!=tree.end(); ++iter) cout << *iter << endl;
  //      cout << "ed\n";

        REP(i,m) {
            cin >> path;
            ans += tree_insert (tree, path);
        }

        cout << "Case " << "#" << z+1 << ": " << ans << endl;
    }
    return 0;
}
//int abc = 0;
int tree_insert (set<string> & tree, string path) {
 //   abc++; if (abc >= 10) return 0;
 //   cout << "path = " << path << endl;

    if (path.length() == 0 || (path.length()!=0 && tree.find(path) != tree.end()) )
        return 0;

    string t;
    int loc, ret = 0, j;

    for (j = path.length()-1; j>=0; j--) {
        if (path[j] == '/') {
            loc = j;
            break;
        }
    }
    t.clear();
    REP(i,loc) t += path[i];

    ret = tree_insert (tree, t);
    tree.insert (path);
    ret++;
 //   cout << "\ninserting path = " << path << endl;
    return ret;
}
