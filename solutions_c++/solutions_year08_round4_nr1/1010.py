#include <iostream>
#include <map>
#include <vector>

using namespace std;

typedef long long int LLI;

struct Node {
    Node(int idd, bool iia, bool cc, Node *pp) : id(idd), ia(iia), c(cc), v(false), p(pp) {
        oia = ia;
        cs[0] = 0;
        cs[1] = 0;
    }
    Node(int idd, bool vv, Node *pp) : id(idd), ia(false), c(false), v(vv), p(pp) {
        oia = ia;
        cs[0] = 0;
        cs[1] = 0;
    }
    friend ostream &operator<<(ostream &os, const Node &n) {
        os << n.id << " " << n.c << " " << n.ia << " " << n.v << " ";
        if (n.p != 0) os << "p" << n.p->id << " ";
        if (n.cs[0] != 0) os << "c0 " << n.cs[0]->id << " ";
        if (n.cs[1] != 0) os << "c1 " << n.cs[1]->id;
        return os;
    }
    static bool sum(Node *n) {
        if (n->cs[0] == 0) {
            return n->v;
        }
        bool v0 = sum(n->cs[0]);
        bool v1 = sum(n->cs[1]);
        if (n->ia) {
            return v0 && v1;
        } else {
            return v0 || v1;
        }
    }
    int id;
    bool c;
    bool ia;
    bool oia;
    bool v;
    Node *p;
    Node *cs[2];
};

main() {
    LLI nc;
    cin >> nc;
    for (LLI ic=1; ic<=nc; ic++) {
        Node *cp=0;
        int m;
        bool v;
        cin >> m >> v;
        // cout << "mv" << m << " " << v << endl;
        vector<Node *> ns;
        vector<Node *> cns;
        for (int i=0; i<m; i++) {
            bool ip = (i<(m-1)/2);
            Node *p = 0;
            if (i>0) p = ns[(i+1)/2-1];
            Node *n;
            if (!ip) {
                bool v;
                cin >> v;
                n = new Node(i+1, v, p);
            } else {
                bool c;
                bool g;
                cin >> g >> c;
                n = new Node(i+1, g, c, p);
                if (c) {
                    cns.push_back(n);
                }
            }
            if (p != 0) p->cs[(i+1)%2] = n;
            ns.push_back(n);
        }
        LLI bits;
        LLI max = 1<<cns.size();
        int minb = max;
        for (LLI im=0; im<max; im++) {
            int bc = 0;
            for (int j=0; j<cns.size(); j++) {
                Node *n = cns[j];
                if ((im&(1<<j)) != 0) {
                    bc++;
                    n->ia = !n->oia;
                } else {
                    n->ia = n->oia;
                }
            }
            bool vv = Node::sum(ns[0]);
            if (vv == v) {
                minb <?= bc;
                // cout << im << " " << bc << endl;
            }
        }
        /*
        for (int i=0; i<m; i++) {
            cout << *ns[i] << endl;
        }
        */
        if (minb == max) {
            cout << "Case #" << ic << ": IMPOSSIBLE" << endl;
        } else {
            cout << "Case #" << ic << ": " << minb << endl;
        }
    }
}
