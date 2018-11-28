#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class dir {
public:
    string name;
    vector<int> childs;
    dir() {}
    dir(string n) {
        name = n;
    }
};

vector<string> split(string& str) {
    string cur = "";
    vector<string> result;
    for(int i=1; i<str.size(); ++i) {
        if(str[i] == '/') {
            result.push_back(cur);
            cur = "";
        }else {
            cur += str[i];
        }   
    }
    result.push_back(cur);
    return result;
}

int find(vector<dir>& dirs, int curdir, string &folder) {
    for(int i=0; i<dirs[curdir].childs.size(); ++i) {
        //printf("LOL, |%s|\t", dirs[dirs[curdir].childs[i]].name.c_str());
        if(dirs[dirs[curdir].childs[i]].name == folder)
            return dirs[curdir].childs[i];
    }
    return -1;
}

int add_folder(vector<dir>& dirs, int curdir, string& folder) {
    dirs.push_back(dir(folder));
    dirs[curdir].childs.push_back(dirs.size()-1);
    return dirs.size()-1;
}

int create_dir(vector<dir>& dirs, string path) {
    vector<string> folders = split(path);
    //for(int i=0; i<folders.size(); ++i) printf("%s\t", folders[i].c_str());
    int curdir = 0, count = 0;
    for(int i=0; i<folders.size(); ++i) {
        int next = find(dirs, curdir, folders[i]);
        //printf("folder = |%s|, next = %d, curdir = %d\n", folders[i].c_str(), next, curdir);
        if(next==-1) {
            ++count;
            curdir = add_folder(dirs, curdir, folders[i]);
        } else {
            curdir = next;
        }
    }
    return count;
}


int main() {
    
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    
    int t; scanf("%d", &t);
    for(int ic=1; ic<=t; ++ic) {
        vector<dir> dirs; dirs.push_back(dir("root"));
        int N, M; scanf("%d %d", &N, &M);
        for(int i=0; i<N; ++i) {
            char buff[128]; scanf("%s", buff);
            create_dir(dirs, string(buff));
        }
        int count = 0;
        for(int i=0; i<M; ++i) {
            char buff[128]; scanf("%s", buff);
            count += create_dir(dirs, string(buff));
        }
        printf("Case #%d: %d\n", ic, count); 
    }
    return 0;
}
