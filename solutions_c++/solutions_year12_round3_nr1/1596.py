#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <fstream>
#include <string>
#include <vector>
#include <map>

using namespace std;

#define NMAX 1005

int nr = 0;

void dfs(vector<int> G[NMAX], int node, int target){
	for(unsigned i = 0; i < G[node].size(); ++i){
		if(G[node][i] == target){
            nr++;
        }
        dfs(G, G[node][i], target);
    }
}

bool solve(vector<int> G[NMAX], int no){
    for(int i = 1; i <= no; ++i)
        for(int j = 1; j <= no; ++j)
            if(i != j){
                nr = 0;
                dfs(G, i, j);
                //cout << i << " " << j << " " << nr << endl;
                if(nr >= 2)
                    return true;
            }

    return false;
}


int main(){
    ifstream in("A-small-attempt1.in");
    ofstream out("A-small-attempt1.out");
    int T;
    in >> T;
    for(int caseNum = 1; caseNum <= T; ++caseNum){
        int M, no;
        vector<int> G[NMAX];
        in >> M;
        for(int i = 0; i < M; ++i){
            int x;
            in >> no;
            for(int j = 1; j <= no; ++j){
                in >> x;
                G[i+1].push_back(x);
            }
        }
        /*for(int i = 1; i <= M; ++i){
            for(int j = 0; j < G[i].size(); ++j)
                cout << G[i][j]  << " ";
            cout << endl;
        }*/

        bool b = solve(G, M);
        if(b)
            out << "Case #" << caseNum << ": Yes" << endl;
        else
            out << "Case #" << caseNum << ": No" << endl;
    }

    return 0;
}
