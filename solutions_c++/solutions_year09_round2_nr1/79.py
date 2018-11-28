#include <string>
#include <sstream>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <algorithm>
#include <set>
#include <iostream>
#include <cassert>
#include <utility>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i++)

struct vertex
{
	double p;
    string f;
    int lf;
    int rg;

    vertex(): p(0.0), f(""), lf(-1), rg(-1) {};
};

vertex v[100000];
int nv;
int root;

int parse(const string& s, int begin, int end)
{
	while (begin < end && s[begin] <= ' ')
    	begin++;

    if (begin >= end)
    	return -1;

    string p;

    assert(s[begin] == '(');
    begin++;

	while (begin < end && s[begin] <= ' ')
    	begin++;

    if (begin >= end)
    	return -1;

    while (begin < end && s[begin] != ' ')
    	p += s[begin++];

    assert(1 == sscanf(p.c_str(), "%lf", &v[nv].p));

	while (begin < end && s[begin] <= ' ')
    	begin++;

    if (begin >= end)
    	return nv++;

    p = "";
    while (begin < end && s[begin] != ' ')
    	p += s[begin++];
    if (p == ")")
    	return nv++;

    v[nv].f = p;

	while (begin < end && s[begin] <= ' ')
    	begin++;
    assert(s[begin] == '(');
    int mid = -1;
    int x = 0;
    for (int i = begin; i != end; i++)
    {
    	if (s[i] == '(')
        	x++;
        if (s[i] == ')')
        	x--;

        if (x == 0 && s[i] == ')')
        {
        	mid = i + 1;
            break;
        }
    }
    assert(mid != -1);

    int idx = nv++;

    v[idx].lf = parse(s, begin, mid);
    assert(v[idx].lf != -1);

    while (s[end - 1] == ' ')
    	end--;
    end--;

    v[idx].rg = parse(s, mid, end);
    assert(v[idx].rg != -1);

    return idx;
}

double calc(int idx, const set<string>& f, double p = 1.0)
{
	assert(idx >= 0);

	p *= v[idx].p;

    if (v[idx].f.length() == 0)
    	return p;

    if (f.count(v[idx].f))
    	return calc(v[idx].lf, f, p);
    else
    	return calc(v[idx].rg, f, p);
}

int main()
{
	freopen("input.txt", "rt", stdin);
	//freopen("output.txt", "wt", stdout);

    string s;

    int tt;
    cin >> tt;
    getline(cin, s);

    forn(tx, tt)
    {
    	int m;
    	cin >> m;
        getline(cin, s);

        string tree;

        forn(i, m)
        {
        	getline(cin, s);
            tree += " " + s;
        }

        forn(i, nv * 2 + 1)
        	v[i] = vertex();
        nv = 0;
        root = parse(tree, 0, tree.length());
        //assert(nv == m);

        int n;
        cin >> n;
        getline(cin, s);
        vector<double> d;

        forn(i, n)
        {
        	getline(cin, s);
            stringstream ss;
            ss << s;

            string name;
            ss >> name;

            int size;
            ss >> size;

            set<string> f;

            forn(j, size)
            {
            	string e;
                ss >> e;
                f.insert(e);
            }

            d.push_back(calc(root, f));
        }

        cout << "Case #" << tx + 1 << ":" << endl;

        forn(i, d.size())
        {
        	printf("%.10lf\n", d[i]);
        }
    }

    fclose(stdin);
    fclose(stdout);
	return 0;
}
