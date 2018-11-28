// codejam1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
//============================================================================
// Name        : helloworld.cpp
// Author      : TioBorracho
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C, Ansi-style
//============================================================================

#include <iostream>
#include <algorithm>
#include <vector>
#include <deque>
#include <string>
using namespace std;
typedef vector<vector<int> > vvint;
typedef vector<int> vint;
typedef vector<string> vs;
typedef vector<vs> vvs;
typedef deque<char> dc;

//#define _ DEBUG

int changes(vs &ses, vs &q){
    //voy buscando la se que me permita meter mas queries
    int changes = 0;
    int pos = 0;
    while (pos < q.size()) {
        //obtengo la posicion para cada se desde la posicion
        int pb = -1;
        int cb = -1;
        for (int i = 0; i < ses.size(); ++i) {
            int tp = pos;
            while (tp < q.size() && q[tp] != ses[i]) ++tp;
            if (pb == -1 || cb < tp) {
                pb = i; cb = tp; }
            if (tp == q.size())
                i  = ses.size();
            
        }
        //elijo la mejor
        pos = cb;
        if (cb == q.size()) {

        } else changes++;

    }

    return changes;
}

int main(void) {
	string s;
	getline(cin, s);
	int casos = atoi(s.c_str());
 	for (int i = 0; i < casos; ++i) {
		getline(cin, s);
        int se = atoi(s.c_str());
        vs ses;
        ses.resize(se);
        for (int j = 0; j < se; ++j) {
            getline(cin, s);
            ses[j] = s;
        }
        getline(cin, s);
        int nq = atoi(s.c_str());
        vs q;
        q.resize(nq);
        for (int j = 0; j < nq; ++j) {
            getline(cin, s);
            q[j] = s;
        }
        int ret = changes(ses, q);


		cout << "Case #" << i+1 << ": " << ret << endl;


	}

 	return 0;
}
