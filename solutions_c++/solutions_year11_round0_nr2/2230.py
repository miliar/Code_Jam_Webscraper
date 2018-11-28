//
//  main.cpp
//  Magicka
//
//  Created by Petro Boychuk on 07.05.11.
//  Copyright 2011 HelloWebApps. All rights reserved.
//

#include <iostream>
#include <map>
#include <set>
#include <stack>
#include <string>
#include <vector>
using namespace std;
#define MP make_pair

map<pair<char, char>, char> combine;
vector< pair<char, char> > opposed;
map<char, int> present;

bool process(stack<char> &sp){
    
    if (sp.size() < 2) {
        return false;
    }
    //Check for combines
    char a = sp.top();
    sp.pop();
    char b = sp.top();
    sp.pop();
    //Try to find pair<a,b> in combine
    if(combine.find(MP(a,b)) != combine.end() ){
        sp.push(combine.find(MP(a,b))->second);
        present[a]--;
        present[b]--;
        return false;
    } else {
        sp.push(b);
        sp.push(a);
    }
    
    //Check for opposed
    //Get last letter
    
    a = sp.top();
    
    for (int i=0; i<opposed.size(); i++) {
        if (opposed[i].first == a) {
            char s = opposed[i].second;
            if (present.find(s) != present.end() && present[s] > 0){
                while (sp.size()) {
                    sp.pop();
                }
                present.clear();
                return false;
            }
        }
    }
    return false;
}

void solve() {
    
    combine.clear();
    opposed.clear();
    present.clear();
    
    stack<char> list;
    stack<char> reversed;
    string spells;
    
    int countCombines;
    int countOpposed;
    
    cin >> countCombines;
    
    for (int i=0; i<countCombines; i++) {
        string temp;
        cin >> temp;
        
        combine.insert(MP(MP(temp[0], temp[1]), temp[2]));
        if (temp[0] != temp[1]) {
            combine.insert(MP(MP(temp[1], temp[0]), temp[2]));
        }
    }
    
    cin >> countOpposed;
    for(int i=0; i<countOpposed; i++){
        string temp;
        cin >> temp;
        opposed.push_back(MP(temp[0], temp[1]));
        if (temp[0] != temp[1]) {
            opposed.push_back(MP(temp[1], temp[0]));
        }
    }
    
    
    int countLetters;
    cin >> countLetters;
    cin >> spells;
    
    
    for (int i=0; i<countLetters; i++) {
        list.push(spells[i]);
        if(present.find(spells[i]) != present.end()) {
            present[spells[i]]++;
        } else{
            present[spells[i]] = 1;
        }
        while (process(list));
    }
    
    while (list.size()) {
        reversed.push(list.top());
        list.pop();
    }
    cout << "[";
    while (reversed.size()) {
        cout << reversed.top() ;
        reversed.pop();
        if (reversed.size() != 0) {
            cout << ", ";
        }
    }
    cout << "]";
    
    
    
}

int main (int argc, const char * argv[])
{
    
    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);
    
    int tests;
    cin >> tests;
    for (int test=1; test <= tests; test++) {
        
        cout << "Case #" << test << ": ";
        solve();
        cout << endl;
    }
    
    return 0;
}

