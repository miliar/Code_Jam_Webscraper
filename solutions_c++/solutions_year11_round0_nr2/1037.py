#include <iostream>
#include <cstdio>
#include <map>
#include <vector>

using namespace std;

int main(){
    int t = 0;
    int count = 1;
    // Bases: Q W E R A S D F
    map<pair<char, char>, char > combine;
    map<pair<char, char>, char > opposed;
    cin >> t;
    while(t > 0){
        combine.clear();
        opposed.clear();
        int comb, opp;
        cin >> comb;
        for(int i = 0; i < comb; i++) {
            string c;
            cin >> c;
            int e1 = c[0];
            int e2 = c[1];
            int e3 = c[2];
            combine[make_pair(e1, e2)] = e3;
            combine[make_pair(e2, e1)] = e3;
        }

        cin >> opp;
        for(int i = 0; i < opp; i++) {
            string c;
            cin >> c;
            int e1 = c[0];
            int e2 = c[1];
            opposed[make_pair(e1, e2)] = 'a';
            opposed[make_pair(e2, e1)] = 'a';
        }

        int size;
        cin >> size;
        string str;
        cin >> str;

        vector<char> final;
        int nelmt = 0;
        for(int i = 0; i < size; i++){
            char c = str[i];
            bool stop = false;
            if(nelmt > 0){
                char previous = final.at(nelmt-1);
                map<pair<char, char>, char>::iterator it = combine.find(make_pair(c, previous));
                if(it != combine.end()){
                    final.pop_back();
                    final.push_back(it->second);
                    continue;
                }
                
                for(int j = nelmt; j > 0; j--){
                    previous = final.at(j-1);
                    it = opposed.find(make_pair(c, previous));
                    if(it != opposed.end()){
                        final.clear();
                        nelmt = 0;
                        stop = true;
                        break;
                    }
                }
                
                if(!stop){
                    final.push_back(c);
                    nelmt++;
                }
            }
            else{
                final.push_back(c);
                nelmt++;
            }
        }

        cout << "Case #" << count << ": [";
        for(int i = 0; i < nelmt; i++){
            cout << final.at(i);
            if(i != nelmt-1) cout << ", ";
        }
        cout << "]" << endl;

        count++;
        t--;
    }

}
