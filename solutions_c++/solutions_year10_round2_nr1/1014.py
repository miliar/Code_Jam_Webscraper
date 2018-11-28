#include <iostream>
#include <vector>
#include <map>
#include <cctype>
#include <climits>
#include <sstream>
#include <algorithm>
#include <cassert>
#include <cstring>
#include <cstdio>

#define ALL(v) (v).begin(),(v).end()

#define SZ(v) ((int)(v).size()) 

#define FOR(i,a,b) for(int i=(a),_b=(b); i<_b; i++)
#define FORE(i,a,b) for(int i=(a),_b=(b);i<=_b;i++)
#define FORDE(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define FOREACH(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)

#define REP(i,n) FOR(i,0,n)
#define REPSZ(i,v) REP(i,SZ(v)) 

//#define DEBUG 

#define NOP do {} while(0)

#if !defined(DEBUG)

#define dprintf(x...)   NOP
#define DOUT(x)         NOP
#define DCOLL(x)        NOP
#define DARR(x,n)       NOP

#else
#define DC(x) cout << "# "#x" = "
#define dprintf(x,...) printf("# " x "\n", ##__VA_ARGS__)
#define DOUT(x) DC(x) << x << endl;
#define DCOLL(x) do { DC(x); \
        FOREACH(it,x){ cout << *it << " "; } \
        cout << endl; } while(0)
#define DARR(x,n) do { DC(x);                     \
        REP(i,n) { cout << x[i] << " "; } \
        cout << endl; } while(0)
#endif

typedef long long ll;

using namespace std;

static void solve_case(int i);

struct Tree;

struct Tree {
    string name; vector<Tree> subdirs;

    explicit Tree(const string& name):name(name) {}
};


int add_path(string& path, Tree& tree)
{

    REPSZ(i,path){
        if(path[i] == '/')
            path[i] = ' ';
    }
    
    string buf; // Have a buffer string
    stringstream ss(path); // Insert the string into a stream

    vector<string> tokens; // Create vector to hold our words

    while (ss >> buf)
        tokens.push_back(buf);

    int result = 0;

    Tree * t = &tree;
    FOREACH(dir,tokens){
        int idx = -1;
        REP(i,t->subdirs.size()){
            if(t->subdirs.at(i).name == *dir){
                idx = i;
                break;
            }
        }
        if(idx >= 0){
            dprintf("Found %s in %s",(*dir).c_str(), t->name.c_str());
            t = &t->subdirs.at(idx);
            continue;
        } else {
            dprintf("Not found %s in %s",(*dir).c_str(), t->name.c_str());
            result++;
            t->subdirs.push_back(Tree(*dir));
            t = &t->subdirs.back();
        }
    }
    return result;
}

int main(void){
    int N;
    cin >> N;
    for(int i = 0; i < N; i++){
        solve_case(i+1);
    }
    return 0;
}


void solve_case(int cn){
    int N,M;
    string path;
    Tree t("/");
    cin >> N >> M;
    REP(i,N){
        cin >> path;
        add_path(path, t);
    }
    int counter = 0;
    REP(i,M){
        cin >> path;
        counter += add_path(path, t);
    }
    cout << "Case #" << cn << ": " << counter << endl;
}
