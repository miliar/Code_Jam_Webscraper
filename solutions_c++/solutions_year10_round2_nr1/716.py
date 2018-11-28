/* 
 * File:   main.cpp
 * Author: Neil
 *
 * Created on May 22, 2010, 11:36 AM
 */

#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

/*
 * 
 */

class Dir {
public:
    Dir(string strname);
    string name;
    vector<Dir *> chl;

    Dir * addchl(string childname);
    Dir * findchild(string childname);
};

Dir * Dir::findchild(string childname){
    for(size_t i = 0; i < chl.size(); i++){
            if(chl[i]->name.compare(childname) == 0)
                return chl[i];
    }
    return NULL;
}

Dir * Dir::addchl(string childname) {
        Dir * chld = new Dir(childname);
        chl.push_back(chld);
        return chld;
}

Dir::Dir(string strname) {
    this->name = strname;
}

int createDir(Dir * root, string path){
    Dir * par = root;
    Dir * child;
    int count = 0;
    unsigned int pos1 = 0;
    unsigned int pos2 = 0;
    while (pos2 < path.length()) {
        pos2 = path.find("/", pos1 + 1);
        string childname = path.substr(pos1 + 1, pos2 - pos1 - 1);
        child = par->findchild(childname);
        if(child == NULL){
            child = par->addchl(childname);
            count++;
        }
        pos1 = pos2;
        par = child;
    }
    return count;
}

void createExitDir(Dir * root, string path) {
    Dir * par = root;
    Dir * child;
    unsigned int pos1 = 0;
    unsigned int pos2 = 0;
    while (pos2 < path.length()) {
        pos2 = path.find("/", pos1 + 1);
        string childname = path.substr(pos1 + 1, pos2 - pos1 - 1);
        child = par->findchild(childname);
        if(child == NULL){
            child = par->addchl(childname);
        }
        pos1 = pos2;
        par = child;
    }
}

int main(int argc, char** argv) {
    ifstream fin("A-large.in", ios::in);
    if (!fin.is_open()) {
        cout << "can not open input file" << endl;
        exit(-1);
    }

    ofstream fout("A-large.out", ios::out);
    if (!fout.is_open()) {
        cout << "can not open output file" << endl;
        exit(-1);
    }

    int testnum;
    fin >> testnum;

    
    int exinum, crenum;

    for (int i = 0; i < testnum; i++) {
		Dir * root = new Dir("/");
        fin >> exinum >> crenum;

        string strExiDir;
        for (int j = 0; j < exinum; j++) {
            fin >> strExiDir;
            createExitDir(root, strExiDir);
        }

        int sum = 0;
        string strToCreDir;
        for(int j = 0; j < crenum; j++){
            fin >> strToCreDir;
            int count = createDir(root, strToCreDir);
            sum += count;
        }

        fout << "Case #" << i+1<< ": " << sum << endl;
    }
    fin.close();
    fout.close();
    
    return (EXIT_SUCCESS);
}

