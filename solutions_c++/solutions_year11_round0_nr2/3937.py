#include <stdio.h>
#include <iostream>
#include <vector>
#include <list>
#include <string>

using namespace std;

vector<string> combine;
vector<string> oppose;
string tempStr;

vector<char> v;

int main()
{
    freopen("E:\\B-large.in", "r", stdin);
    freopen("E:\\output.txt", "w", stdout);

    int TC, tc, temp, i, j, k;
    int C, D, N;
    char ch;

    cin >> TC;

    for(tc=1; tc<=TC; tc++) {
        cin >> C;
        for(i=1; i<=C; i++) {
            cin >> tempStr;
            combine.push_back(tempStr);
        }
        cin >> D;
        for(i=1; i<=D; i++) {
            cin >> tempStr;
            oppose.push_back(tempStr);
        }

        cin >> N;

        cin >> ch;
        v.push_back(ch);

        for(i=1; i<N; i++) {
            cin >> ch;
            v.push_back(ch);

            bool isCombined = false;
            bool isOpposed = false;

            if(v.size() >= 2) {
                for(j = 0; j<C; j++) {
                    if((v[v.size()-2] == combine[j][0] && v[v.size()-1] == combine[j][1]) ||
                       (v[v.size()-2] == combine[j][1] && v[v.size()-1] == combine[j][0])) {
                        v.pop_back();   v.pop_back();
                        v.push_back(combine[j][2]);
                        isCombined = true;
                        break;
                    }
                }
            }

            isOpposed = false;
            if(isCombined != true) {
                for(j=0; j<D; j++) {
                    if(ch == oppose[j][0])
                        for(k=0; k<v.size(); k++) {
                            if(v[k] == oppose[j][1]) {
                                v.clear();
                                isOpposed = true;
                                break;
                            }
                        }
                    else if(ch == oppose[j][1])
                         for(k=0; k<v.size(); k++) {
                            if(v[k] == oppose[j][0]) {
                                v.clear();
                                isOpposed = true;
                                break;
                            }
                        }
                    if(isOpposed == true) break;
                }

            }
        }

        cout << "Case #" << tc << ": ";

        if(v.size() == 0) {
           cout << "[]\n";
        }
        else {
            cout << "[";
            cout << v[0];
            for(j=1; j<v.size(); j++) {
                cout << ", " << v[j];
            }
            cout << "]\n";
        }

        v.clear();
        combine.clear();
        oppose.clear();
    }


    return 0;
}
