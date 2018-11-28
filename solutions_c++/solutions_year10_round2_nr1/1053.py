/*
 * =====================================================================================
 *
 *       Filename:  fixit.cpp
 *
 *    Description:  #
 *
 *         Author:  Victor Carbune (victor.carbune@gmail.com)
 *	     Info:  Grupa 325, Seria CA
 *
 * =====================================================================================
 */

#include <iostream>
#include <string>
#include <vector>
#include <string.h>

using namespace std;

typedef struct _node node, *pnode;

struct _node
{
    string dir;
    vector<node> children;
};

void insert(pnode root, string path) {
    string currdir, nextdir = "";
    node n;
    int i, found = 0;
    if (path.find('/', 1) != string::npos) {
        currdir = path.substr(1, path.find('/', 1)-1);
        nextdir = path.substr(path.find('/', 1), path.size() - path.find('/', 1));
    } else {
        currdir = path.substr(1);
        nextdir = "";
    }

    for (i = 0; i < root->children.size(); i++) {
        if (root->children[i].dir == currdir) {
            found = 1;
            if (nextdir != "") 
                insert(&root->children[i], nextdir);
        }
    }

    if (!found) {
        root->children.push_back(n);
        root->children[root->children.size()-1].dir = currdir;
        if (nextdir != "")
            insert (&root->children[root->children.size()-1], nextdir);
    }
}

void show(node r, int l) {
    int i;

    for (i = 0; i < l; i++)
        cout << " ";
    cout << r.dir << endl;

    for (i = 0; i < r.children.size(); i++) {
        show(r.children[i], l+1);
    }
}

int mkdir(pnode root, string path) {
    string currdir, nextdir = "";
    node n;
    int i, found = 0;
    if (path.find('/', 1) != string::npos) {
        currdir = path.substr(1, path.find('/', 1)-1);
        nextdir = path.substr(path.find('/', 1), path.size() - path.find('/', 1));
    } else {
        currdir = path.substr(1);
        nextdir = "";
    }

    for (i = 0; i < root->children.size(); i++) {
        if (root->children[i].dir == currdir) {
            found = 1;
            if (nextdir != "") 
                return mkdir(&root->children[i], nextdir);
            else {
                return 0;
            }
        }
    }

    if (!found) {
        root->children.push_back(n);
        root->children[root->children.size()-1].dir = currdir;
        if (nextdir != "")
            return 1 + mkdir(&root->children[root->children.size()-1], nextdir);
        else {
            return 1;
        }
    }
}

int main() {
    int mkdirs, tc, i, j, n, m;
    char *p;
    string path;
    
    cin >> tc;

    for (i = 0; i < tc; i++) {
        cin >> n >> m;
        mkdirs = 0;
        
        node root;
        root.dir = "/";
        
        for (j = 0; j < n; j++) {
            cin >> path;
            insert(&root, path);
        }

        for (j = 0; j < m; j++) {
            cin >> path;
            mkdirs += mkdir(&root, path);
        }
        cout << "Case #" << i+1 << ": " << mkdirs << "\n";
//        show(root, 0);
    }
}
