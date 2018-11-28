/**
   File: C.cpp

   (c) Copyright Albert Graells Rovira

   $Id$
*/

#include <iostream>
#include <vector>
#include <cmath>
#include <map>
#include <set>
#include <queue>

using namespace std;

typedef pair<int, int> pii;

int calcResult() {
    int N;
    cin >> N;

    map<int, int> mapa;
    set<pii> s;

    for (int i = 0; i < N; i++) {
        int a, b; cin >> a >> b;
        mapa[a] = b;
        s.insert(pii(b, a));
    }

    int iMoves = 0;

    while (1) {
/*
        for (int i = -10; i < 10; i++) {
            if (mapa.find(i) != mapa.end()) cout << mapa[i] << " ";
            else cout << 0 << " ";
        }
        cout << endl;
*/
        set<pii>::iterator si = s.end(); si--;
        pii last = *si;
        s.erase(si);
        mapa.erase(last.second);

        if (last.first == 1) break;

        std::map<int, int>::iterator it;

        it = mapa.find(last.second - 1);
        if (it == mapa.end()) {
            s.insert(pii(1, last.second - 1));
            mapa[last.second - 1] = 1;
        }
        else {
            s.erase(pii(it->second, it->first));
            it->second++;
            s.insert(pii(it->second, it->first));
        }

        it = mapa.find(last.second + 1);
        if (it == mapa.end()) {
            s.insert(pii(1, last.second + 1));
            mapa[last.second + 1] = 1;
        }
        else {
            s.erase(pii(it->second, it->first));
            it->second++;
            s.insert(pii(it->second, it->first));
        }

        if (last.first - 2 != 0) {
            mapa[last.second] = last.first - 2;
            s.insert(pii(last.first - 2, last.second));
        }

        iMoves++;
    }

    return iMoves;
}

int main()
{
    int N;
    cin >> N;
    for (int k = 1; k <= N; k++) {
        cout << "Case #" << k << ": ";
        int iResult = calcResult();
        cout << iResult << endl;
    }
    return 0;
}
