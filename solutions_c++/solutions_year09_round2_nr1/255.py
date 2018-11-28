#include <iostream>
#include <vector>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <stack>
using namespace std;


typedef long long ll;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<bool> VB;
typedef vector<VB> VVB;
typedef vector<ll> VL;
typedef vector<VL> VVL;
typedef vector<char> VC;
typedef vector<VC> VVC;
typedef vector<string> VS;
typedef vector<VS> VVS;
typedef pair<int, int> PII;
const int INF = 1000000000;

struct Nodo {
    string s;
    int hi, hd;
    double peso;
};

Nodo G[1000000];
int num;
string in;
int pos;

int lee() {
    bool izq = false, der = false;
    while (pos < in.size() and in[pos] != '(') ++pos;
    ++pos;
    if (pos >= in.size()) return -1;
    string s;
    while (not isdigit(in[pos])) ++pos;
    while (in[pos] != ' ' and in[pos] != ')' and in[pos] != '(') {
        s += in[pos];
        ++pos;
    }
    stringstream iss(s);
    double x;
    iss >> x;
    s.clear();
    while (in[pos] != '(' and in[pos] != ')') {
        if (isalpha(in[pos])) s+= in[pos];
        ++pos;
    }
    int res = num;
    G[res].peso = x;
    G[res].s = s;
    ++num;
    if (in[pos] == '(') {
        G[res].hi = lee();
        izq = true;
    }
    while (pos < in.size() and in[pos] != ')' and in[pos] != '(') ++pos;
    if (in[pos] == '(') {
        G[res].hd = lee();
        der = true;
    }
    if (not izq) G[res].hi = -1;
    if (not der) G[res].hd = -1;
    while (pos < in.size() and in[pos] != ')') ++pos;
    ++pos;
    return res;
}

double prob(set<string>& visto, int a) {
    if (a == -1) return 1;
    double res = G[a].peso;
    if (visto.count(G[a].s)) {
        return res*prob(visto, G[a].hi);
    }
    else return res*prob(visto, G[a].hd);
}

int main() {
    cout.setf(ios::fixed);
    cout.precision(7);
    int k, caso = 1;
    cin >> k;
    while (k--) {
        int linias;
        cin >> linias;
        cin.ignore();
        in.clear();
        string s;
        pos = 0;
        for (int i = 0; i < linias; ++i) {
            getline(cin, s);
            in += s;
        }
        num = 0;
        int temp = lee();
        int n;
        cin >> n;
        cout << "Case #" << caso++<< ":" << endl;
        for (int i = 0; i < n; ++i) {
            cin >> s;
            int a;
            cin >> a;
            string aux;
            set<string> visto;
            for (int j = 0; j < a; ++j) {
                cin >> aux;
                visto.insert(aux);
            }
            cout << prob(visto, temp) << endl;
        }
    }
}
