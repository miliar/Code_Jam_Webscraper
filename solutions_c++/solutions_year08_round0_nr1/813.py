#include <stdio.h>
#include <assert.h>

#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;


typedef vector<int>     IV;
typedef vector<IV>      VV;
typedef vector<string>  SV;

typedef unsigned int uint;

class matrix {
public:
    matrix(int qs, int ss) {
        IV  dummy;
        dummy.resize(ss, 0);
        _data.resize(qs, dummy);
    }
    VV  _data;
};

int solve(SV& engines, SV& str_queries) {
    if (engines.size() == 0 || str_queries.size() == 0) return 0;
    IV qs;
    for(uint i=0; i<str_queries.size(); i++) {
        int idx = find(engines.begin(), engines.end(), str_queries[i])-engines.begin();
        qs.push_back(idx);
    }

    matrix m(qs.size(), engines.size());
    for (int i=qs.size()-1; i>=0; i--) {
        for (int j=0; j<engines.size(); j++) {
            int price = qs[i] == j ? 1 : 0;
            if (i != qs.size()-1) {
                if (qs[i+1] == j) {
                    // forced to switch - choose the minimal price ..
                    price += 1 + *min_element(m._data[i+1].begin(), m._data[i+1].end());
                }
                else {
                    price += m._data[i+1][j];
                }
            }
            m._data[i][j] = price;
        }
    }

    int min_price = *min_element(m._data[0].begin(), m._data[0].end());
    
    //printf("\n%10s", " ");
    //for (int j=0; j<engines.size(); j++) {
    //    if (engines[j].length()>9) { engines[j] = engines[j].substr(0, 9); }
    //    printf("%10s", engines[j].c_str());
    //}
    //printf("\n");

    //for (int i=0; i<qs.size(); i++) {
    //    if (str_queries[i].length()>9) { str_queries[i] = str_queries[i].substr(0, 9); }
    //    printf("%10s", str_queries[i].c_str());
    //    for (int j=0; j<engines.size(); j++) {
    //        printf("%10d%c", m._data[i][j], qs[i] == j ? '*' : ' ');
    //    }
    //    printf("\n");
    //}
    //printf("\n");


    return min_price;
}



void main(int argc, char** argv) {
    vector<string> engines;
    vector<string> str_queries;


    int N = 0;
    cin >> N;

    for (int i=0; i<N; i++) {
        string str;

        engines.clear();
        str_queries.clear();
        int S;
        cin >> S;   getline(cin, str);

        for (int j=0; j<S; j++) {
            getline(cin, str);
            engines.push_back(str);
        }
        int Q;
        cin >> Q;      getline(cin, str);
        for (int j=0; j<Q; j++) {
            getline(cin, str);
            str_queries.push_back(str);
        }
        int x = solve(engines, str_queries);
        printf("Case #%i: %d\n", i+1, x);

    }
    return;
}

