#include <iostream>
#include <vector>
#include <string.h>
#include <map>
#include <algorithm>
#include <cassert>
#include <sstream>
using namespace std;
#define FOR(a,b,c) for(int a = b; a < c; a++)
#define REP(i,n) FOR(i,0,n)
#define GI ({int _; scanf("%d", &_); _;})
#define sz size()
#define pb push_back
#define mkp make_pair
#define INF 1e8
#define MAX 1000
typedef vector<int> VI;

class node {
public:
    double wt;
    int f;    
    node *l, *r;
    node(double w=0, node *ll=NULL, node *rr=NULL) {
        wt = w, f=-1, l = ll, r = rr;
    }
};

node *root;
map <string, int> mp;
int cnt, yes[MAX];
stringstream s;
    double wt;
    string f;
    char c;

node * input() {
    s >> c;
    //cout << c << endl;
    assert(c == '(');

    s >> wt >> f;
    node *cur = new node(wt);    
    //cout << "wt -> " << wt <<" f-> "<< f << endl;
    if(f[0] != ')') {
        mp[f] = cnt++;
        cur->f = mp[f];
        
        cur->l = input();
        cur->r = input();
        s >> c;
        assert(c == ')');
    }        
    return cur;
}
double go(node *cur) {
    if(cur == NULL) return 1.0;
    
    if(yes[cur->f]) {
        return cur->wt * go(cur->l);
    }
    else {
        return cur->wt * go(cur->r);
    }


}
void print(node *c) {
    if(!c) return;
    cout << c->wt <<", "<< c->f <<"\n";
    cout <<"left -> \n";
    print(c->l);
    cout <<"right -> \n";
    print(c->r);
    

}
int main() {
    int kases = GI;
    FOR(kase, 1, kases+1) {
        cnt=1;
        mp.clear();
        int lines = GI;
        cin.ignore();
        string line, inp = "";
        REP(i,lines) {
            getline(cin,line);
            inp += line;
        }
        string inpp = "";
        REP(i,inp.sz) {
            if(inp[i] == '(' || inp[i] == ')') {
                inpp += " ";
            }
            inpp += inp[i];
            if(inp[i] == '(' || inp[i] == ')') {
                inpp += " ";
            }
        }

        s << inpp;
        
        root = input();
        //print(root);
        printf("Case #%d:\n", kase);
        double ans;
        int tmp = GI;        
        while(tmp--) {
            string name, feat;
            int feats;
            memset(yes,0,sizeof(yes));
            cin >> name;
            cin >> feats;
            while(feats--) {
                cin >> feat;
                if(mp.count(feat))
                yes[mp[feat]]++;
            }
            printf("%.8lf\n", go(root));   
        
        }
            

    }











}
