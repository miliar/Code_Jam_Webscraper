#include <vector>
#include <cmath>
#include <queue>
#include <string>
#include <sstream>
#include <fstream>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <set>
#include <map>
#include <cctype>
#include <stack>

using namespace std;

#define fe(i,a,n) for(int i = a, __n = n; i < __n; i++)
#define fi(i,a,n) for(int i = a, __n = n; i <= __n; i++)
#define LL long long
#define ULL unsigned long long
#define VI vector<int>
#define VS vector<string>
#define VD vector<double>
#define SI stack<int>
#define SS stack<string>
#define SD stack<double>
#define ERRO 1e-10
#define INF 1e+99
#define tr(i,s) for(typeof(s.begin()) i = s.begin(); i != s.end(); i++)
#define all(v) v.begin(), v.end()

int getTime(int currentLoc, int expectedLoc) {
    if (currentLoc < expectedLoc) {
        return expectedLoc - currentLoc + 1;
    } else {
        return currentLoc - expectedLoc + 1;
    }
}

int getBestNewLocation(int currentLoc, int expectedLoc, int timeIHave) {
    if (currentLoc < expectedLoc) {
        return currentLoc + timeIHave;
    } else {
        return currentLoc - timeIHave;
    }
}

int getValue(string x, int i) {
    return x[i];
}

int main() {
    int a;
    cin >> a;
    //    string x;
    //    getline(cin, x);

    fe(i,0,a) {
        //        string input;
        //        getline(cin, input);

        int total, pos;
        char color;
        cin >> total;
        VI x;

        fe(j,0,total) {
            cin >> color >> pos;
            x.push_back(color);
            x.push_back(' ');
            x.push_back(pos);
            x.push_back(' ');
        }

        int ret = 0;
        int posBlue = 1;
        int posOrange = 1;
        if (total > 0) {

            for (int element = 0, size = x.size(); element < size; element += 4) {

                int timeCurrElem = 0;
                if (x[element] == 'O') {
                    //time to move Orange element to right location and press the button
                    timeCurrElem = getTime(posOrange, x[element + 2]);
                    posOrange = x[element + 2];

                    //what can the position of other element change in this time
                    // search for the other element
                    for (int otherElement = element; otherElement < size; otherElement += 4) {
                        // if exists, then in the given time, try to proceed it to the best location
                        int timeOtherElem = 0;
                        if (x[otherElement] == 'B') {
                            timeOtherElem = getTime(posBlue, x[otherElement + 2]);
                            if (timeOtherElem <= timeCurrElem) {
                                posBlue = x[otherElement + 2];
                            } else {
                                posBlue = getBestNewLocation(posBlue, x[otherElement + 2], timeCurrElem);
                            }
                            break;
                        }
                    }
//                    cout << "time to move Orange element to right location and press the button = " << timeCurrElem << endl;
//                    cout << "posBlue = " << posBlue << endl;
//                    cout << "posOrange = " << posOrange << endl;

                } else if (x[element] == 'B') {
                    //time to move Blue element to right location and press the button
                    timeCurrElem = getTime(posBlue, x[element + 2]);
                    posBlue = x[element + 2];

                    //what can the position of other element change in this time
                    // search for the other element
                    for (int otherElement = element; otherElement < size; otherElement += 4) {
                        // if exists, then in the given time, try to proceed it to the best location
                        int timeOtherElem = 0;
                        if (x[otherElement] == 'O') {
                            timeOtherElem = getTime(posOrange, x[otherElement + 2]);
                            if (timeOtherElem <= timeCurrElem) {
                                posOrange = x[otherElement + 2];
                            } else {
                                posOrange = getBestNewLocation(posOrange, x[otherElement + 2], timeCurrElem);
                            }
                            break;
                        }
                    }
//                    cout << "time to move Blue element to right location and press the button = " << timeCurrElem << endl;
//                    cout << "posBlue = " << posBlue << endl;
//                    cout << "posOrange = " << posOrange << endl;
                }

                ret += timeCurrElem;

            }
        }

        if (i != a - 1) {
            cout << "Case #" << i + 1 << ": " << ret << endl;
        } else {
            cout << "Case #" << i + 1 << ": " << ret;
        }

    }
    return 0;
}
