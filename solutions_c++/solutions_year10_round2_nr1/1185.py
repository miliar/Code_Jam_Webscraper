#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int countx(string x) {
    const char *xc = x.c_str();
    int c = 0;
    for (int i = 0; i < x.size(); i ++) {
        if (xc[i] == '/') {
            c ++;
        }
    }
    return c;
}

int main() {
    int t, n, m;
    cin >> t;
    vector<string> earr;
    vector<string> marr;
    for (int i = 0; i < t; i ++) {
        cin >> n;
        cin >> m;
        earr.clear(); 
        marr.clear(); 
        for (int j = 0; j < n; j ++) {
            string dir;
            cin >> dir;
            earr.push_back(dir);
        }
        for (int j = 0; j < m; j ++) {
            string dir;
            cin >> dir;
            marr.push_back(dir);
        }
        // now solve the mkdir problem
        sort(earr.begin(), earr.end());
        sort(marr.begin(), marr.end());

        int count = 0;
        for (int j = marr.size() - 1; j >= 0; j--) {
            string dir = marr[j];
            int dir_size = dir.size();
            int max_edir_size = 0;
            string max_edir;
            int break_here = 0;
            for (int k = earr.size() -1; k >= 0; k--) {
                string edir = earr[k];
                if (edir.size() == dir_size && dir.compare(edir) == 0) {
                    break_here = 1;
                    break;
                } else if (edir.size() > dir_size && edir.compare(0, dir_size, dir) == 0 && edir[dir_size] == '/') {
                    break_here = 1;
                    break;
                }  else {
                    string eedir = edir;
                    while (eedir.size() > 0) {
                        if (dir.compare(0, eedir.size(), eedir) == 0 && dir[eedir.size()] == '/') {
                            // path to create
                            if (max_edir_size < eedir.size()) {
                                max_edir_size = eedir.size();
                                max_edir = eedir;
                            }
                        }
                        int rid = (int)eedir.rfind("/");
                        eedir = eedir.substr(0, rid);
                        //cout << eedir << endl;
                    }
                }
            }
            if (!break_here) {
                if (max_edir_size != 0) {
                    string newdir = dir.substr(max_edir.size());
                    //cout << "new dir" << newdir << endl;
                    count += countx(newdir);
                } else {
                    // have to run all
                    //cout << "comp dir" << dir << endl;
                    count += countx(dir);
                }
            }
            earr.push_back(dir);
        }

        cout << "Case #" <<  i + 1 << ": " << count << endl;
    }
}
