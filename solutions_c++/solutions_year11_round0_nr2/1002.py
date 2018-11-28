// -*- C++ -*-
// Copyright (c) Calypto Design Systems 2010-2011 
/// @(#)bt.cc
///
///
/// @date   05/07/11 11:15:39
/// @author Srihari Yechangunja (syechan@calypto.com)
///
/// @brief  
/// *** DELETE THIS LINE AFTER ADDING COMMENTS HERE ****
/// 
/// $Id$

#include <iostream>
#include <string>
#include <utility>
#include <map>
#include <set>
#include <list>

//#define DEBUG
//#define DEBUG1

using namespace std;

typedef pair<char, char> basePair;

static map<basePair, char> combiners;
static map<char, set<char> > opposers;
static map<char, unsigned> elementsMap;
static list<char> elementsList;

void printElementList() {
    // Print it out in the right format
    cout << "[";
    if (!elementsList.empty()) {
        list<char>::iterator eli = elementsList.begin(), ele = elementsList.end();
        cout << *eli;
        for (++eli; eli != ele; ++eli) {
            cout << ", " << *eli;
        }
    }
    cout << "]";
}

void addCombination(char a, char b, char c) {
#ifdef DEBUG1
    cerr << "addCombination(" << a << ", " << b << ", " << c << ")" << endl;
#endif
    // Add both orders to map
    basePair combiningElements1(a, b);
    combiners[combiningElements1] = c;

    basePair combiningElements2(b, a);
    combiners[combiningElements2] = c;
}

void addOpposition(char a, char b) {
#ifdef DEBUG1
    cerr << "addOpposition(" << a << ", " << b << ")" << endl;
#endif
    // Add both orders to set
    opposers[a].insert(b);
    opposers[b].insert(a);
}

void addElement(char newElem) {
    //     add element to end of list and increment count in map
    elementsList.push_back(newElem);
    ++elementsMap[newElem];
#ifdef DEBUG
    cerr << "After elementAddtion: count[" << newElem << "] = " << elementsMap[newElem] << endl;
    printElementList(); cout << endl;
#endif
}

void removeLastElement() {
    char el = elementsList.back();
    elementsList.pop_back();
    --elementsMap[el];
}

char performCombinations(char el) {
#ifdef DEBUG1
    cerr << "performCombinations(" << el << ")" << endl;
#endif
    bool combRequired = false;
    // Recursively check for combinations and replace the last one
    do {
        basePair tryComb(el, elementsList.back());
        combRequired = (combiners.find(tryComb) != combiners.end());
        if (combRequired) {
            el = combiners[tryComb];
            removeLastElement();
        }
    } while (combRequired);

    return el;
}

bool performOppositions(char el) {
#ifdef DEBUG1
    cerr << "performOppostions(" << el << ")" << endl;
#endif
    // Check for oppositions and clear if found
    set<char> &oppSet = opposers[el];

    list<char>::iterator eli = elementsList.begin(), ele = elementsList.end();
    for (; eli != ele; ++eli) {
        if (oppSet.count(*eli) > 0) {
            elementsList.clear();
            elementsMap.clear();
            return false;
        }
    }
    return true;
}

void performInvocation(char newElem) {
#ifdef DEBUG1
    cerr << "performInvocation("  << newElem << ")" << endl;
#endif
    //     perform combination reactions
    char combinedElem = performCombinations(newElem);
    //     perform opposition reactions
    bool noOppositions = performOppositions(combinedElem);
    // add the element if required
    if (noOppositions) {
        addElement(combinedElem);
    }
#ifdef DEBUG
    cerr << "After invocation of " << newElem << endl;
    printElementList(); cout << endl;
#endif
}

void printTestResult(int test) {
    cout << "Case #" << test << ": ";
    printElementList();
    cout << endl;
}

void cleanupForTest() {
    combiners.clear();
    opposers.clear();
    elementsList.clear();
    elementsMap.clear();
}

void doTest(int test) {
    // read list of combiners
    unsigned C = 0U;
    cin >> C;
#ifdef DEBUG
    cerr << "The " << C << " combiners are:" << endl;
#endif
    string buff;
    for (unsigned c=0U; c<C; ++c) {
        cin >> buff;
#ifdef DEBUG
        cerr << c << " : " << buff << endl;
        assert(buff.length() == 3);
#endif
        addCombination(buff[0], buff[1], buff[2]);
    }

    // read list of opposers
    unsigned D = 0U;
    cin >> D;
#ifdef DEBUG
    cerr << "The " << D << " opposers are:" << endl;
#endif
    for (unsigned d=0U; d<D; ++d) {
        cin >> buff;
#ifdef DEBUG
        cerr << d << " : " << buff << endl;
        assert(buff.length() == 2);
#endif
        addOpposition(buff[0], buff[1]);
    }

    // read invocation sequence
    unsigned N = 0U;
    cin >> N;
    cin >> buff;
#ifdef DEBUG
    cerr << "The " << N << " elements to be invoked are: " << buff << endl;
    assert(buff.length() == N);
#endif
    // for each element in sequence {
    //     perform invocation on current element
    // }
    for (unsigned n=0; n<N; ++n) {
        performInvocation(buff[n]);
    }

    // dump final element list
    printTestResult(test);
    // cleanup before next test
    cleanupForTest();
}

int main() {
    int T = 0;

    cin >> T;
#ifdef DEBUG
    cerr << "T = " << T << endl;
#endif

    for (int t=1; t<=T; ++t) {
        doTest(t);
    }

    return 0;
}

