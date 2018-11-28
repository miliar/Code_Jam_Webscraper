/* 
 * File:   main.cpp
 * Author: wintokk
 *
 * Created on May 23, 2010, 12:08 AM
 */

#include <stdlib.h>
#include <iostream>
#include <vector>
#include <map>
using namespace std;

#define MAX_NODE 60000
typedef map<string, int> themap;

themap tree[MAX_NODE];
int N, count;

vector<string> split_string(string s, const char * deli)
{
    vector<string> vs;
    int pos = 1, i;
    s += '/';
    while (pos < s.size())
    {
        i = s.find_first_of(deli, pos);
        if (i > pos)
            vs.push_back(s.substr(pos, i - pos));
        pos = i + 1;
    }
    return vs;
}

void init()
{
    // root is 0
    N = 1;
    for (int i = 0; i < MAX_NODE; i++)
        tree[i].clear();
    count = 0;
}

void check(int &node, string name, int add)
{
    if (tree[node].find(name) != tree[node].end())
        node = tree[node][name];
    else
    {
        //cout << node << ' ' << name << endl;//d
        tree[node][name] = N;
        node = N++;
        count += add;
    }
}

/*
 * 
 */
int main(int argc, char** argv) {
    int task, tt, old_n, new_n;
    string path;
    freopen("a.in", "r", stdin);
    cin >> task;
    for (int tt = 1; tt <= task; tt++)
    {
        cout << "Case #" << tt << ": ";
        cin >> old_n >> new_n;
        init();
        for (int i = 0; i < old_n; i++)
        {
            cin >> path;
            vector<string> dirs = split_string(path, "/");
            int node = 0;
            for (int j = 0; j < dirs.size(); j++)
            {
                //cout << '/' << dirs[j]; //d
                check(node, dirs[j], 0);
            }
            //cout << endl; //d
        }
        for (int i = 0; i < new_n; i++)
        {
            cin >> path;
            vector<string> dirs = split_string(path, "/");
            int node = 0;
            for (int j = 0; j < dirs.size(); j++)
            {
                //cout << '/' << dirs[j]; //d
                check(node, dirs[j], 1);
            }
            //cout << endl; //d
        }
        cout << count << endl;
    }

    return (EXIT_SUCCESS);
}

