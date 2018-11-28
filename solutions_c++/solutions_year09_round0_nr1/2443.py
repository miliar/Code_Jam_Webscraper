#include <iostream>
#include <fstream>
#include <string>
#include <stack>

using namespace std;

int main() {
    ifstream in("A-small-attempt0.in");
    ofstream out("A-small-attempt0.out");
    int L, D, N, i, j, k, l, flag;
    in >> L >> D >> N;
    string words[D], patterns[N], cons;
    for(i=0; i<D; i++)
        in >> words[i];
    for(i=0; i<N; i++)
        in >> patterns[i];
    deque <string> matches, temp;

    for(i=0; i<N; i++) {
        matches.clear();
        for(j=0; j<patterns[i].length(); j++) {
            temp.clear();
            if(patterns[i][j] != '(') {
                for(k=j; patterns[i][k]!='('&&k<patterns[i].length(); k++)
                    ;
                if(matches.empty())
                    matches.push_back(patterns[i].substr(j, k-j));
                else {
                    while(!matches.empty()) {
                        cons.assign(matches.back());
                        matches.pop_back();
                        cons.append(patterns[i],j,k-j);
                        temp.push_back(cons);
                    }
                    matches.assign(temp.begin(),temp.end());
                }
                j=k-1;
            }
            else if(patterns[i][j] == '(') {
                for(k=j; patterns[i][k]!=')'&&k<patterns[i].length(); k++)
                    ;
                if(matches.empty())
                    for(l=j+1; l<k; l++)
                        matches.push_back(patterns[i].substr(l, 1));
                else {
                    while(!matches.empty()) {
                        cons.assign(matches.back());
                        matches.pop_back();
                        for(l=j+1; l<k; l++) {
                            cons.append(patterns[i],l,1);
                            temp.push_back(cons);
                            cons.erase(cons.end()-1);
                        }
                    }
                    matches.assign(temp.begin(), temp.end());
                }
                j = k;
            }
            temp.clear();
            while(!matches.empty()) {
                cons.assign(matches.back());
                matches.pop_back();
                for(k=0; k<D; k++) {
                    flag = 0;
                    if(cons == words[k].substr(0, cons.length())) {
                        flag = 1;
                        break;
                    }
                }
                if(flag)
                    temp.push_back(cons);
            }
            matches.assign(temp.begin(), temp.end());
            if(matches.size() == 0)
                break;
        }
        out << "Case #" << i+1 << ": " << matches.size() << endl;
    }
    in.close();
    out.close();
    return 0;
}

