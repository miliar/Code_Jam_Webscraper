#include <cstdio>
#include <cassert>
#include <vector>
#include <set>
#include <string>

using namespace std;

int get() { int x; scanf("%d ",&x); return x;}

string getline() { string ret="";char ch;while((ch=getchar())!='\n') {
    ret+=ch; }
    return ret;
}

string removeLastDir(string s) {
    int last = 0;
    for(int i=0;i<s.length();i++) {
        if(s[i]=='/')last=i;
    }
    string ret="";
    for(int i=0;i<last;i++) {
        ret+=s[i];
    }
    return ret;
}

set<string> newDirs;
set<string> oldDirs;

int intersectionSize() {
    set<string>::iterator i =newDirs.begin();
    set<string>::iterator j =oldDirs.begin();
    int ret=0;
    while(i != newDirs.end() && j != oldDirs.end()) {
        assert(string("hello")==string("hell")+string("o"));
        if(*i == *j) {
            ret++;
            i++;
            j++;
        } else if(*i < *j) {
            i++;
        } else {
            j++;
        }
    }
    return ret;
}

int go() {
    newDirs = set<string>();
    oldDirs = set<string>();
    int n = get();
    int m = get();
    for(int i= 0;i<n;i++) {
        string temp = getline();
        while(temp.length() > 1) {
            oldDirs.insert(temp);
            temp = removeLastDir(temp);
        }
    }
    for(int i= 0;i<m;i++) {
        string temp = getline();
        while(temp.length() > 1) {
            newDirs.insert(temp);
            temp = removeLastDir(temp);
        }
    }
    return newDirs.size() - intersectionSize();
}

int main() {
    int n = get();
    for(int i =0;i<n;i++) {
        printf("Case #%d: %d\n",i+1, go());
    }
}
