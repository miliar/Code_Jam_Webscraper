#include <iostream>
#include <string>
#include <vector>
#include <map>
using namespace std;

int main() {
    int T;
    int M,N;
    string s;

    map<char, string> mm;
    mm['0']="0000"; mm['1']="0001"; mm['2']="0010"; mm['3']="0011";
    mm['4']="0100"; mm['5']="0101"; mm['6']="0110"; mm['7']="0111";
    mm['8']="1000"; mm['9']="1001"; mm['A']="1010"; mm['B']="1011";
    mm['C']="1100"; mm['D']="1101"; mm['E']="1110"; mm['F']="1111";

    cin >> T;
    for(int cc=1;cc<=T;cc++) {
        vector<string> v;
        cin >> M >> N;
        string row;
        for(int i=0;i<M;i++) {
            cin >> s;
            row = "";
            for(int i=0;i<s.size();i++) {
                row += mm[s[i]];
            }
            v.push_back(row);
        }


        map<int, int> m2;

        for(int sz=min(M,N);sz>=1;sz--) {
            for(int i=0;i+sz<=M;i++) {
                for(int j=0;j+sz<=N;j++) {

                    bool f=true;
                    for(int ii=i;ii<i+sz;ii++) {
                        for(int jj=j;jj<j+sz;jj++) {
                            if(v[ii][jj] == 'a') { f=false; break; }
                            if(ii-1>=i && v[ii-1][jj]==v[ii][jj]) { f=false; break; }
                            if(ii+1<i+sz  && v[ii+1][jj]==v[ii][jj]) { f=false; break; }
                            if(jj-1>=j && v[ii][jj-1]==v[ii][jj]) { f=false; break; }
                            if(jj+1<j+sz  && v[ii][jj+1]==v[ii][jj]) { f=false; break; }
                        }

                        if(f==false) break;
                    }
                    if(f==true) {
                        m2[sz]++;
                        for(int ii=i;ii<i+sz;ii++) {
                            for(int jj=j;jj<j+sz;jj++) {
                                if(ii-1>=i) v[ii-1][jj] = 'a';
                                if(ii+1<i+sz) v[ii+1][jj] = 'a';
                                if(jj-1>=j) v[ii][jj-1] = 'a';
                                if(jj+1<j+sz) v[ii][jj+1] = 'a';
                            }
                        }

                    }

                }
            }
        }

        printf("Case #%d: %d\n", cc, (int)m2.size());
        for(map<int,int>::reverse_iterator it = m2.rbegin();it!=m2.rend(); ++it) {
            printf("%d %d\n", it->first, it->second);
        }
            
    }

    return 0;
}
