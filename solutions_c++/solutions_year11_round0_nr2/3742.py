#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

// index, target
pair<int,int> get_combiner(const vector<string>& v, char c) {
    for (int i = 0 ; i < int(v.size()) ; ++i) {
        if(v[i][0] == c ) { 
            return make_pair(i, v[i][1]);
        }
        if(v[i][1] == c ) {
            return make_pair(i, v[i][0]);
        }
    }
    return make_pair(-1, 0);
}

int is_opposed(const vector<string>& v, char c) {
    for (int i = 0 ; i < int(v.size()) ; ++i) {
        if(v[i][0] == c ) {
            return v[i][1];
        }
        if(v[i][1] == c) {
            return v[i][0];
        }
    }
    return 0;
}

int main(int argc, char *argv[]) {
    int lines;
    cin >> lines;
    for (int i = 0 ; i < lines ; ++i) {
        int C;
        cin >> C;
        vector<string> combines;
        //cerr << "combines: " << C << endl;
        for (int j = 0 ; j < C ; ++j) {
            string s;
            cin >> s;
            combines.push_back(s);
            //cerr << s << endl;
        }

        int D;
        cin >> D;
        vector<string> opposed;
        //cerr << "opposed: " << D << endl;
        for (int j = 0 ; j < D ; ++j) {
            string s;
            cin >> s;
            opposed.push_back(s);
            //cerr << s << endl;
        }

        int N;
        cin >> N;
        string spell;
        cin >> spell;

        //cerr << "spell: " << spell << endl;
        vector<char> result;
        for (int j = 0 ; j < N ; j++ ) {
            char c = spell[j];

            if( result.empty() ) {
                result.push_back(c);
                //cerr << "first: " << c << endl;
                continue;
            }

            // combines ?
            pair<int,int> cc = get_combiner( combines, c );
            if( cc.first != -1 ) {
                if( result.back() == cc.second ) {
                    result.pop_back();
                    result.push_back(combines[cc.first][2]);
                    //cerr << "combines: " << c << combines[cc.first] << endl;
                    continue;
                }
            }

            // opposed ?
            int o = is_opposed( opposed, c );
            if(find(result.begin(), result.end(), o) != result.end()) {
                result.clear();
                //cerr << "opposed: " << endl;
                continue;
            }

            result.push_back(c);
            //cerr << "no event: " << c <<endl;
        }

        cout << "Case #" << (i+1) << ": [";
        for(int j = 0; j < result.size() ; j++ ) {
            if( j!= 0 ) { cout << ", "; }
            cout << result[j];
        }
        cout << "]\n";
    }
    
    return 0;
}
