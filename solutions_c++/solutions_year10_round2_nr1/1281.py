#include <iostream>
#include <string>
#include <sstream>
#include <map>
#include <vector>

using namespace std;


struct node {
    typedef map<string, node*> map_t;
    map_t mp;
    int add_path(const vector<string>& v, int ind) {
        int res=0;
        map_t::iterator it = mp.find(v[ind]);
        if (it == mp.end()) {
            node* nn = new node();
            mp[v[ind]] = nn;
            res = 1;
            if (ind+1 < v.size())
                res += nn->add_path(v, ind+1);
        } else {
            if (ind+1 < v.size())
                res = it->second->add_path(v, ind+1);
        }
        return res;
    }
};

int main() {
    int T;
    cin >> T;
    for (int cs=1; cs<=T; ++cs) {
        node root;
        int N, M, res=0;
        cin >> N >> M;
        for (int i=0; i<N; ++i) {
            string path;
            cin >> path;
            int a=1, b, s=path.size();
            vector<string> vs;
            for (b=1; b<=s; ++b) {
                if (path[b] == '/' || path[b] == '\0') {
                    vs.push_back(path.substr(a, b-a));
                    a = b+1;
                }
            }
            root.add_path(vs, 0);
        }

        for (int i=0; i<M; ++i) {
            string path;
            cin >> path;
            int a=1, b, s=path.size();
            vector<string> vs;
            for (b=1; b<=s; ++b) {
                if (path[b] == '/' || path[b] == '\0') {
                    vs.push_back(path.substr(a, b-a));
                    a = b+1;
                }
            }
            res += root.add_path(vs, 0);
        }
        cout << "Case #" << cs << ": " << res << "\n";
    }
}
