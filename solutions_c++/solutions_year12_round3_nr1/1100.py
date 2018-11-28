#include <iostream>
#include <vector>
#include <queue>
#include <stdio.h>
#include <algorithm>
using namespace std;

int main()
{
    size_t tests;
    cin >> tests;
    vector< vector<size_t> > tree;
    vector<bool> inode;
    queue<size_t> BFS;
    for(size_t i = 1;i<=tests; ++i){
        size_t nodes_count, adj_count, adj;
        bool cycle = false;
        cin >> nodes_count;
        tree.clear();
        tree.resize(nodes_count+1);
        inode.clear();
        inode.resize(nodes_count+1, false);
        for (size_t j=1; j<=nodes_count; ++j ){
            cin >> adj_count;
            for (size_t k=0; k < adj_count; ++k){
                cin >> adj;
                tree[adj].push_back(j);
            }
            if (adj_count == 0) { tree[0].push_back(j); }
        }
        for(vector<size_t>::iterator it0=tree[0].begin(); it0!=tree[0].end(); ++it0){
            while(!BFS.empty()) BFS.pop();
            BFS.push(*it0);
            fill(inode.begin(), inode.end(), false);
            while (!BFS.empty() && !cycle){
                adj = BFS.front();
                BFS.pop();
                for(vector<size_t>::iterator it=tree[adj].begin(); it!=tree[adj].end(); ++it){
                    if (inode[*it]){
                        cycle = true;
                        break;
                    } else {
                        inode[*it] = true;
                        BFS.push(*it);
                    }
                }
            }
            if (cycle) break;

        }
        cout << "Case #" << i << ": ";
        if (cycle) cout << "Yes";
        else cout << "No";
        cout << endl;
    }
    return 0;
}
