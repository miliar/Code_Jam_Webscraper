#include <algorithm>
#include <deque>
#include <set>
#include <utility>
#include <cstring>
#include <iostream>
#include <fstream>

#define foreach( i, c )\
typedef __typeof__( c ) c##_CONTAINERTYPE;\
for( c##_CONTAINERTYPE::iterator i = c.begin(); i != c.end(); ++i )


// TODO: don't do this
using namespace std;

int main() {
    ifstream fin("in.txt");
    int nCases;
    fin >> nCases;
    for (int caseNum = 1; caseNum <= nCases; ++caseNum) {
        int nButtons;
        fin >> nButtons;
        deque<int> oPresses, bPresses;
        deque<pair<char,int> > presses;
        for (int i = 0; i < nButtons; ++i) {
            char colour;
            int num;
            fin >> colour >> num;
            presses.push_back(make_pair(colour, num));
            if (colour == 'O') {
                oPresses.push_back(num);
            } else {
                bPresses.push_back(num);
            }
        }

        int steps = 0;
        int bPos = 1, oPos = 1;
        foreach(it, presses) {
            char curColour = it->first;
            int targetPos = it->second;
            int* pos1;
            int* pos2;
            deque<int>* vec1;
            deque<int>* vec2;
            if (curColour == 'O') {
                pos1 = &oPos;
                pos2 = &bPos;
                vec1 = &oPresses;
                vec2 = &bPresses;
            } else {
                pos1 = &bPos;
                pos2 = &oPos;
                vec1 = &bPresses;
                vec2 = &oPresses;
            }
            while (*pos1 != vec1->front()) {
                *pos1 += (*pos1 > vec1->front() ? -1 : 1);
                if (*pos2 > vec2->front()) {
                    (*pos2)--;
                } else if (*pos2 < vec2->front()) {
                    (*pos2)++;
                }
                steps++;
            }

            if (*pos2 > vec2->front()) {
                (*pos2)--;
            } else if (*pos2 < vec2->front()) {
                (*pos2)++;
            }

            // button pushing
            steps++;
            vec1->pop_front();
        }

        cout << "Case #" << caseNum << ": " << steps << endl;
    }

    return 0;
}

