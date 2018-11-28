
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cstring>

using namespace std;

class TreeNode {
public:
    string path;
    bool exists;
    vector<TreeNode*> children;

    TreeNode() { exists = true; }
    TreeNode* findNode(string &content) {
        TreeNode *p;
        for(int i = 0; i < children.size(); ++i) {
            p = children[i];
            if (p->path == content) return p;
        }
        return NULL;
    }
    TreeNode* createNode(string &content, bool markexist) {
        TreeNode *node = new TreeNode();
        node->path = content;
        this->children.push_back(node);
        node->exists = markexist;
        return node;
    }
    ~TreeNode() {
        for(int i = 0; i < children.size(); ++i) {
            delete children[i];
        }
    }
    int countNonExists() {
        int num = 0;
        if (!exists) ++num;
        for(int i = 0; i < children.size(); ++i) {
            num += children[i]->countNonExists();
        }
        return num;
    }
};


class Tree {
public:
    TreeNode *rootNode;

    void insertPath(const string &fullpath, bool markexist) {
        char tempbuf[128];
        strcpy(tempbuf, fullpath.c_str());
        char *p = strtok(tempbuf, "/");
        TreeNode *node = rootNode;
        string tempstr;
        while (true) {
            if (!p) break;
            tempstr = p;
            if (markexist)
                node = insertExistNode(node, tempstr);
            else
                node = insertNonExistNode(node, tempstr);
            p= strtok(NULL, "/");
        }
    }

    int countNonExists() {
        return rootNode->countNonExists();
    }

    TreeNode* insertExistNode(TreeNode *parent, string &content) {
        TreeNode* node = parent->findNode(content);
        if (node != NULL) return node;
        return parent->createNode(content, true);
    }
    TreeNode* insertNonExistNode(TreeNode *parent, string &content) {
        TreeNode* node = parent->findNode(content);
        if (node != NULL) return node;
        return parent->createNode(content, false);
    }

    Tree() {
        rootNode = new TreeNode();
        rootNode->path = "/";
        rootNode->exists = true;
    }
    ~Tree() {
        delete rootNode;
    }
};

int main() {
    char inputfilename[] = "A-large.in";
    ifstream ifs(inputfilename);
    int ntestcases, nexists, ntocreate, result;
    ifs>>ntestcases;
    char pathbuf[101];
    string str;
    for (int i = 0; i < ntestcases; ++i) {
        Tree *tree = new Tree();
        ifs>>nexists>>ntocreate;
        for (int j = 0; j < nexists; ++j) {
            ifs>>pathbuf;
            str = pathbuf;
            tree->insertPath(str, true);
        }
        for (int j = 0; j < ntocreate; ++j) {
            ifs>>pathbuf;
            str = pathbuf;
            tree->insertPath(str, false);
        }
        result = tree->countNonExists();
        cout<<"Case #"<<(i+1)<<": "<<result<<endl;
        delete tree;
    }
}

