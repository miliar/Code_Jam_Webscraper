#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
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
#include <cctype> 
#include <string> 
#include <cstring> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <ctime> 
#include <limits>

using namespace std;

typedef long long ll;

set<string> attrs;

struct node {
    string label;
    double prob;
    node* n1;
    node* n2;
};

node* parse(stringstream& ss)
{
    char ch;
    node* cur = new node;
    ss >> ch;
    ss >> cur->prob;
    ss >> ch;
    if (ch == ')')
    {
        cur->label = "";
        cur->n1 = 0;
        cur->n1 = 0;
        return cur;
    }
    cur->label = ch;
    if (!isspace(ss.peek()))
    {
        string s;
        ss >> s;
        cur->label += s;
    }
    cur->n1 = parse(ss);
    cur->n2 = parse(ss);
    ss >> ch;
    return cur;
}

double prob(node* c)
{
    double p = 1.0;
    while (true)
    {
        p *= c->prob;
        if (c->label == "")
            break;
        if (attrs.find(c->label) != attrs.end())
            c = c->n1;
        else
            c = c->n2;
    }
    return p;
}

int main()
{
    int t, L, A, an;
    cin >> t;
    for (int tt = 1; tt <= t; ++tt)
    {
        string s, tmp;
        cin >> L;
        getline(cin, tmp);
        for (int i = 0; i < L; ++i)
        {
            getline(cin, tmp);
            s += tmp;
        }

        stringstream ss(s);
        node* root = parse(ss);

        cin >> A;
        cout << "Case #" << tt << ":" << endl;
        for (int i = 0; i < A; ++i)
        {
            cin >> tmp >> an;
            attrs.clear();
            for (int j = 0; j < an; ++j)
            {
                cin >> tmp;
                attrs.insert(tmp);
            }
            cout << fixed << setprecision(10) << prob(root) << endl;
        }
    }
    return 0;
}