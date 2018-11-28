#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <set>
using namespace std;

int main()
{
    int n;
    string tmp;
    getline(cin, tmp);
    istringstream iss(tmp.c_str());
    iss >> n;
    for(int i=0;i<n;i++) {
        getline(cin, tmp);
        istringstream iss(tmp.c_str());
        int s;
        iss >> s;
        vector<string> search;
        for(int j=0;j<s;j++) {
            getline(cin, tmp);
            search.push_back(tmp);
        }
        int q;
        getline(cin, tmp);
        istringstream iss2(tmp.c_str());
        iss2 >> q;
        vector<string> query;
        for(int j=0;j<q;j++) {
            getline(cin, tmp);
            query.push_back(tmp);
        }
        set<string> a;
        int cnt = 0;
        for(int j=0;j<q;j++) {
            a.insert(query[j]);
            if(a.size() == s) {
                cnt++;
                a.clear();
                a.insert(query[j]);
            }
        }
        cout << "Case #" << i+1 << ": " << cnt << endl;
    }

    return 0;
}
