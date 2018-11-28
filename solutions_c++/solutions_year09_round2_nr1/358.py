#include <iostream>
#include <set>
#include <sstream>
#include <map>
#include <vector>

using namespace std;

struct Node {
    double w;
    string feature;
    int yesPt;
    int noPt;
};

Node nodes[1000];
int nodept=0;

int newnode() {
    return nodept++;
}


void print(int r, int s){ 
    if (r==-1) return;
    for(int i=0; i<s; i++) cout << ' ';
    cout << nodes[r].w << " " << nodes[r].feature<<endl;
    print(nodes[r].yesPt, s+1);
    print(nodes[r].noPt, s+1);
}

int parse() {
    char bracket;
    double w;
    int my = newnode();

    cin >> bracket; if(bracket != '(') cout <<" BAD BRACKET"<<endl;
    cin >> w;
    nodes[my].w = w;
    nodes[my].yesPt=-1; nodes[my].noPt=-1; nodes[my].feature="";

    while(cin.peek() == ' ') cin.get();
    if (cin.peek() != ')') {
        string feat;
        cin >> feat;
        nodes[my].feature=feat;
        nodes[my].yesPt = parse();
        nodes[my].noPt = parse();
    }

    cin >> bracket; if (bracket != ')') cout << " BAD ) bracket" << endl;
    return my;
}

int main() {
    int cases;
    cin >> cases;

    for(int c=0; c<cases; c++) {
        cout << "Case #" << (c+1)<<":"<<endl;
        nodept=0;

        int linen;
        cin >> linen;

        int root = parse();
        //print(root,0);
        

        int acnt, fcnt;
        cin >> acnt;
        for(int i=0; i<acnt; i++){ 
            string animal, feat;
            cin >> animal >> fcnt;

            set<string> features;
            for(int i=0; i<fcnt; i++) {
                cin >> feat;
                features.insert(feat);
            }

            double ans=1;
            int pt = root;
            while(pt!=-1) {
                ans *= nodes[pt].w;
                string f = nodes[pt].feature;

                if (f!="" && features.count(f)) { pt = nodes[pt].yesPt;  }
                else { pt = nodes[pt].noPt;  }
            }
            printf("%.7f\n", ans);
        }
    }
}
