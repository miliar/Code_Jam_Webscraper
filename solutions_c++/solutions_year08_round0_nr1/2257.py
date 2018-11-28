#include "stdafx.h"
#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;
int main()
{
    int nCases;
    cin >> nCases;
    for(int aCase = 1; aCase <= nCases; ++aCase) {
        int engCount;
        map <string, int> engines;
        int nQueries;
        int cnt = 0;
        cin >> engCount;
        string engName;
        getline(cin, engName);
        while(engCount) {
            getline(cin, engName);
            //if(engName[0] != '\n')
            engines[engName] = 0;
            //cout << engName << endl;
            --engCount;
        }
        /*for(map<string, int>::iterator it = engines.begin();
            it != engines.end(); ++it)
            cout << it->first <<" " << it->second << endl;*/
    
        cin >> nQueries;
        getline(cin, engName);
        vector <string> q;
		if(nQueries == 0) {
			cout << "Case #" << aCase <<": " << cnt << endl; 
			continue;
		}
        for(int aQuery = 0; aQuery < nQueries; ++aQuery) {
            getline(cin, engName);
            q.push_back(engName);
        }
        //for(int i = 0; i < q.size(); ++i) cout << q[i] << endl;
        int m = 0;        
        while(m < q.size()) {
            int m2;
            m2 = 0;
            for(map<string, int>::iterator it = engines.begin();
            it != engines.end(); ++it) {
                it->second = 0;
                for(int i = m; i < q.size(); ++i) {
                    if(it->first == q[i]) break;
					++(it->second);
                    m2 = max(m2, it->second);
                }
            }
            m += m2;
            ++cnt;
        }
        /*int min = 1000000;
        for(map<string, int>::iterator it = engines.begin();
            it != engines.end(); ++it) {
            if(min > it->second) min = it->second;
            //cout << it->first << " " << it->second << endl;
        }*/
        cout << "Case #" << aCase <<": " << cnt - 1 << endl;
        //cout << engines.size() << endl;*/
    }
    return 0;
}