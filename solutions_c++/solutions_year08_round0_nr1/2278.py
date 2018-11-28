#include<iostream>
#include<string>
#include<map>
#include<vector>

using namespace std;

int numEngines;
int numSearches;
map<string,int> name2number;
vector<string> number2name;
vector<int> queryNums;
vector< vector<int> > dp;

void play(int engineNo, int queryPos) {
    if (queryPos >= numSearches-1)  {
        if (engineNo != queryNums[queryPos]) 
            dp.at(engineNo).at(queryPos)=0;
        else
            dp.at(engineNo).at(queryPos)=1;
        return;
    }
    if (dp[engineNo][queryPos]>-1) return;
    if (engineNo != queryNums[queryPos]) {
        // don't change
        play(engineNo,queryPos+1);
        dp[engineNo][queryPos] = dp[engineNo][queryPos+1];
    }
    else {
        // try all other engines
        int min = 1000000;
        for (int i=0; i<numEngines; i++) {
            if (i != engineNo) {
                play(i,queryPos+1);
                if (dp[i][queryPos+1] < min) 
                    min=dp[i][queryPos+1];
            }
        }
        dp[engineNo][queryPos]=1+min; // one switch
    }
}

void go(int x) {

    cin >> numEngines;
    cin.get(); // newline
    name2number.clear();
    number2name.clear();
    for (int i=0; i<numEngines; i++) {
        string name;
        getline(cin,name);
        name2number[name] = number2name.size();
        number2name.push_back(name);
    }

    cin >> numSearches;
    cin.get(); // newline
    queryNums.clear();
    for (int i=0; i<numSearches; i++) {
        string query;
        getline(cin,query);
        //cout << query << endl;
        assert(name2number.count(query)>0);
        queryNums.push_back( name2number[query] );
    }
    dp.clear();
    dp.resize(numEngines);
    for (int i=0; i<numEngines; i++) {
        dp.at(i).resize(numSearches,-1);
    }

    int min=100000;
    if (numSearches > 0) {
        // try starting with each different search engine
        for (int i=0; i<numEngines; i++) {
            play(i,0);
            if(dp.at(i).at(0) < min)
                min = dp.at(i).at(0);
        }
    }
    else {
        min=0;
    }
    cout << "Case #" << x << ": " << min << endl;
}

int main() {
    int numCases;
    cin >> numCases;
    for (int i=0; i<numCases; i++) {
        go(i+1);
    }
}
