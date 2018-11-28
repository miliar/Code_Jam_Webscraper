#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>
#include <queue>
#include<cstring>
using namespace std;
typedef vector<int> VI;
typedef vector<vector<int> > VVI;
typedef pair<int,int> PII;
typedef long long int64;
typedef unsigned long long uint64;
//template<typename T> int size(const T& c) { return int(c.size()); }
//template<typename T> T abs(T x) { return x < 0 ? -x : x; }
template<typename T> T sqr(T x) { return x*x; }
#define FOR(i, a, b) for (int i(a), _b(b); i <= _b; ++i)
#define FORD(i, a, b) for (int i(a), _b(b); i >= _b; --i)
#define REP(i, n) for (int i(0), _n(n); i < _n; ++i)
#define REPD(i, n) for (int i((n) - 1); i >= 0; --i)
class Tree {
public:
    string name;
    list<Tree*> child;
    Tree(string _name):name(_name){
        child = list<Tree*>();
    }
    Tree* addChild(string name) {
        Tree *t=new Tree(name);
        child.push_back(t);
        return t;
    }
    int insert(list<string> &dirs) {
        int ans = 0;
        Tree *cur = this;
        for(list<string>::iterator it = dirs.begin(); it != dirs.end(); it++) {
            list<Tree*>::iterator childit = cur->child.begin();
            for(; childit!=cur->child.end(); childit++)
                if((*childit)->name.compare(*it) == 0)
                    break;
            if(childit==cur->child.end()) {
                ans++;
                cur = cur->addChild(*it);
            }
            else
                cur = *childit;
        }
        return ans;
    }
    ~Tree() {
        for(list<Tree*>::iterator childit = child.begin(); childit!=child.end(); childit++)
            delete (*childit);
    }
};
void parse(const string &path,list<string> &dirs) {
    int i=1,j=1;
    while(j<path.size()) {
        if(path[j] == '/') {
            dirs.push_back(path.substr(i,j-i));
            i=j+1;
        }
        j++;
    }
    dirs.push_back(path.substr(i,j-i));
    /*for(list<string>::iterator it = dirs.begin(); it != dirs.end(); it++) {
        cout << *it << endl;
    }
    cout << endl;*/
}
int main() {
    //char finname[] = "A_test.in";
    //char finname[] = "A-small-attempt0.in";
    //char finname[] = "A-small-attempt1.in";
    //char finname[] = "A-small-attempt2.in";
    char finname[] = "A-large.in";    
    FILE *fp;
    if((fp=fopen(finname,"r")) == NULL) {
        printf("File not found\n");
        exit(0);
    }
    fclose(fp);
    freopen(finname,"r",stdin);
    freopen(strcat(finname,".outFile"),"w",stdout);
    int tc,n,m,r,k,ans;
    string epaths[100],newpaths[100];
    list<string> dirs;
    scanf("%d",&tc);    
    for(int tci=0;tci<tc;tci++) {
        scanf("%d%d",&n,&m);
        ans=0;
        Tree root("/");
        REP(i,n) {
            cin >> epaths[i];
            //cout << epaths[i] << endl;
            dirs.clear();
            parse(epaths[i],dirs);
            root.insert(dirs);
        }
        //printf("\n");
        REP(i,m) {
            cin >> newpaths[i];
            //cout << newpaths[i] << endl;
            dirs.clear();
            parse(newpaths[i],dirs);
            ans+=root.insert(dirs);
        }

        printf("Case #%d: %d\n",tci+1,ans);
    }
    return 0;
}
