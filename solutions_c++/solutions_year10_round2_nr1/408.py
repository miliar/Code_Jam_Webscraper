#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

int n, m;

struct DirNode
{
    map<string, struct DirNode> nodes;
};

typedef map<string, struct DirNode>::iterator TreeIt;

vector<string> dirlist;

DirNode tree;

int addToTree(string& str)
{
    if (str.length() <= 1)
        return 0;
    int h = 1, t = 0;
    DirNode* p = &tree;
    int s = 0;
    do {
        t = str.find_first_of('/', h);
        string subdir = str.substr(h, t == string::npos ? str.length() - h : t - h);
        if (subdir.length() > 0)
        {
            TreeIt it = p->nodes.find(subdir);
            if (it != p->nodes.end())
            {
                p = &(it->second);
            }
            else
            {
                DirNode dn;
                pair<TreeIt, bool> pr = p->nodes.insert(make_pair(subdir, dn));
                p = &pr.first->second;
                ++s;
            }
        }
        h = t + 1;
    } while (t != string::npos);
    return s;
}

void main()
{
    ifstream fin("A-small.in");
    ofstream fout("A.out");
    int T;
    fin >> T;
    string str;
    for (int tt = 1; tt <= T; ++tt)
    {
        fin >> n >> m;
        for (int i = 0; i < n; ++i)
        {
            fin >> str;
            addToTree(str);
        }

        int s = 0;
        dirlist.clear();
        for (int i = 0; i < m; ++i)
        {
            fin >> str;
            dirlist.push_back(str);
        }
        sort(dirlist.begin(), dirlist.end());
        for (int i = 0; i < m; ++i)
        {
            s += addToTree(dirlist[i]);
        }
        fout << "Case #" << tt << ": " << s << endl;
        tree.nodes.clear();
    }
    fout.close();
    fin.close();
}
