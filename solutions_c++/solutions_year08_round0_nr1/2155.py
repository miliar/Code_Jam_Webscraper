// Solve for optimal strategy of choosing a search engine
//

#include <string>
#include <iostream>
#include <sstream>
#include <vector>
#include <map>
#include <limits>
using namespace std;


int Min(vector<vector<int> >& dp, int row, int col)
{
    int min = numeric_limits<int>::max();
    for (int i = 0; i < (int) dp.size(); i++) {
        if (i == row)
            continue;
        if (dp[i][col] < min)
            min = dp[i][col];
    }
    return min;
}
int MinimizeSwitches (int n, vector<int>& q)
{
    if ((int) q.size() == 0)
        return 0;
    vector<vector<int> > dp(n);
    int m = (int) q.size();
    for(int i = 0; i < n; i++) {
        dp[i] = vector<int>(m, 0);
    }
    dp[q[0]][0] = 1;
    for(int j = 1; j < m; j++) {
        for (int i = 0; i < n; i++) {
            if(q[j] == i) {
                dp[i][j] = Min(dp,i,j-1) + 1;
            }
            else {
                dp[i][j] = dp[i][j-1]; 
            }
        }
    }
    return Min(dp, -1, m-1);
}

int main() 
{
    int nCases, nQueries, nSearchEngines, c = 0;
    string temp;
    vector<int> res;
    getline(cin, temp);
    nCases = atoi(temp.c_str());



    while(c < nCases) {
        vector<int> queries;
        map<string,int> servers;

        getline(cin,temp);
        nSearchEngines = atoi(temp.c_str());
        for (int i = 0; i < nSearchEngines; i++) {
            getline(cin, temp);
            servers[temp] = i;
        }

        getline(cin,temp);
        nQueries = atoi(temp.c_str());
        for (int i = 0; i < nQueries; i++) {
            getline(cin, temp);
            queries.push_back(servers[temp]); 
        }
        res.push_back(MinimizeSwitches(nSearchEngines, queries));
        c++;
    }
    
    for(int i = 0; i < (int) res.size(); i++)
        cout << "Case #" << i+1 << ": " << res[i] << endl;
    
    return 0;
}
