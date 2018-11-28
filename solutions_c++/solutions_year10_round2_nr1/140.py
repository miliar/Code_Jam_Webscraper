#include <iostream>
#include <sstream>
#include <set>
#include <vector>

using namespace std;

vector<string> split(string path) {
    istringstream ist(path);

    vector<string> ret;
    string part;
    while(getline(ist, part, '/')) {
        ret.push_back(part);
    }
    return ret;
}

int main() {
    int cases;
    cin >> cases;

    for(int c=0; c<cases; c++) {
        set<string> paths;
        int N,M;
        cin >> N >> M;

        paths.insert("/");
        for(int i=0; i<N; i++) {
            string path;
            cin >> path;
            vector<string> parts = split(path);
            string pp = "";
            for(int j=0; j<parts.size(); j++) {
                pp += parts[j] + "/";
                paths.insert(pp);
                //cout << "A: " << pp << endl;
            }
        }

        int ans=0;
        for(int i=0; i<M; i++) {
            string path;
            cin >> path;
            //cout << "Creating path: " << path << endl;
            vector<string> parts = split(path);
            string pp = "";
            for(int j=0; j<parts.size(); j++) {
                pp += parts[j] + "/";
                if (paths.count(pp) == 0) {
                    paths.insert(pp);
                    //cout << "B: " << pp << endl;
                    ans++;
                }
            }
        }
        cout << "Case #" <<(c+1) << ": " << ans << endl;
    }
}
