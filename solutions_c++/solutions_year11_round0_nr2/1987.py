#include <iostream>
#include <sstream>
#include <cstring>
#include <vector>
#include <stack>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <ctime>
#include <cstdio>
#include <cstdlib>

using namespace std;

//#define debug

#define DPRINT printf
#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
#define MP(a,b) make_pair(a,b)


int main (void) {
    int T;
    cin >> T;
    REP(i, T) {
        int C, D, N;
        map<char, map<char,char>* > combine;
        map<char, set<char>* > opposed;
        char elements[101];
        set<char> *opposedFlag[101];
        memset(opposedFlag, 0, sizeof(set<char>*) * 101);

        cin >> C;
        REP(j, C) {
            char tmp[4];
            cin >> tmp;
            if (combine.find(tmp[0]) == combine.end()) {
                map<char,char>* t = new map<char,char>();
                combine.insert(MP(tmp[0],t));
            }
            if (combine.find(tmp[1]) == combine.end()) {
                map<char,char>* t = new map<char,char>();
                combine.insert(MP(tmp[1],t));
            }
            combine[tmp[0]]->insert(MP(tmp[1],tmp[2]));
            combine[tmp[1]]->insert(MP(tmp[0],tmp[2]));
        }
        cin >> D;
        REP(j, D) {
            char tmp[3];
            cin >> tmp;
            if (opposed.find(tmp[0]) == opposed.end()) {
                set<char>* t = new set<char>();
                opposed.insert(MP(tmp[0],t));
            }
            if (opposed.find(tmp[1]) == opposed.end()) {
                set<char>* t = new set<char>();
                opposed.insert(MP(tmp[1],t));
            }
            opposed[tmp[0]]->insert(tmp[1]);
            opposed[tmp[1]]->insert(tmp[0]);
        }
        cin >> N >> elements;
        REP(j,N) {
            map<char,set<char>* >::iterator itr = opposed.find(elements[j]);
            if (itr != opposed.end()) {
                opposedFlag[j] = itr->second;
            } else {
                opposedFlag[j] = NULL;
            }
        }

#ifdef debug
        foreach(combine, itr) {
            cout << '(' << itr->first;
            foreach(*(itr->second), itritr) {
                cout << ',' << itritr->first;
                cout << "=>" << itritr->second;
            }
            cout << ')';
        }
        cout << ' ';
        foreach(opposed, itr) {
            cout << '(' << itr->first;
            foreach(*(itr->second), itritr) {
                cout  << ','<< *itritr;
            }
            cout << ')';
        }
        cout << ' ';
        REP(j,N) {
            cout << '(';
            if (opposedFlag[j] != NULL) {
                foreach(*(opposedFlag[j]),itr) {
                    cout << *itr;
                }
            }
            cout << ')';
        }
        cout << ' ';
        cout << elements << endl;
#endif

        REP(j,N - 1) {
            map<char,map<char,char>*>::iterator itr = combine.find(elements[j]);
            if (itr != combine.end()) {
                map<char,char>::iterator conv = itr->second->find(elements[j+1]);
                if (conv != itr->second->end()) {
                    elements[j] = '0';
                    elements[j + 1] = conv->second;
                    opposedFlag[j] = opposedFlag[j + 1] = NULL;
                    j++;
                }
            }
            REP(k,j + 1) {
                set<char>* opposedList = opposedFlag[k];
                if ((opposedList != NULL) &&
                    (opposedList->find(elements[j+1]) != opposedList->end())) {
                    for (int l = 0; l <= j + 1; l++) {
                        elements[l] = '0';
                        opposedFlag[l] = NULL;
                    }
                }
            }
        }
        cout << "Case #" << i+1 << ": [";
        bool first = true;
        REP(j,N) {
            if (elements[j] != '0') {
                if (!first) cout << ", ";
                cout << elements[j];
                first = false;
            }
        }
        cout << "]" << endl;
    }
    return 0;
}
