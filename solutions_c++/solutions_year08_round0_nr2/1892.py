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
vs Tokenize(string s, string ch) {
	vs ret;
	for (unsigned int p = 0, p2; p < s.size(); p = p2+1) {
		p2 = s.find_first_of(ch, p);
		if (p2 == -1) p2 = s.size();
		if (p2-p > 0) ret.push_back(s.substr(p, p2-p));
	}
	return ret;
}

vint TokenizeInt(string s, string ch) {
	vint ret;
	vs p = Tokenize(s,ch);
	for (unsigned int i = 0; i < p.size(); ++i )
		ret.push_back(atoi(p[i].c_str()));
	return ret;
}
        vint da, db, aa, ab;
        vint ca, cb, ua, ub;
        int tot ;

int sumar(int a, int b) {
    int ret = a +b;
    if (ret % 100 >= 60)
    ret += 40;
    return ret;
}
vint trains(){
    //voy cubriendo primero los de B con los de A, pero necesito hacerlo desde el más temprano, hay que ordenar los vectores sin perder la identif.... bah, para que?
    //no me importa cual es cual
    sort(ab.begin(), ab.end());
    sort(db.begin(), db.end());
    for (int i = 0; i < ab.size(); ++i) if (ua[i] == 0)
    {
        int valor = sumar(ab[i], tot);
        for (int j = 0; j < db.size() && ua[i] == 0; ++j) if (!cb[j] && valor <= db[j]) {
            cb[j] = 1;
            ua[i] = 1;
        }
    }

    sort(aa.begin(), aa.end());
    sort(da.begin(), da.end());
    for (int i = 0; i < aa.size(); ++i) if (ub[i] == 0)
    {
        int valor = sumar(aa[i], tot);
        for (int j = 0; j < da.size() && ub[i] == 0; ++j) if (!ca[j] && valor <= da[j]) {
            ca[j] = 1;
            ub[i] = 1;
        }
    }
    int adic1 = 0, adic2 = 0;
    if (ca[0] == 1 && cb[0] == 1) {
        if (da[0] < db[0]) adic1 = 1; else adic2= 1;
    }


    vint ret;
    int temp = 0 + adic1;
    for (int i = 0; i < ca.size(); ++i) if (ca[i]==0) ++ temp;
    ret.push_back(temp);
    temp = 0 + adic2;
    for (int i = 0; i < cb.size(); ++i) if (cb[i]==0) ++ temp;
    ret.push_back(temp);

    return ret;

}

int main(void) {
	string s;
	getline(cin, s);
	int casos = atoi(s.c_str());
 	for (int i = 0; i < casos; ++i) {
		getline(cin, s);
        tot = atoi(s.c_str());
        getline(cin, s);
        vint na = TokenizeInt(s, " ");
        da.resize(na[0]);
        ab.resize(na[0]);
        db.resize(na[1]);
        aa.resize(na[1]);

        ca.resize(na[0], 0);
        ua.resize(na[0], 0);
        cb.resize(na[1], 0);
        ub.resize(na[1], 0);
        for (int j = 0; j < na[0]; ++j) {
            getline(cin, s);
            vs sched = Tokenize(s, " ");
            vint hora = TokenizeInt(sched[0], ":");
            da[j] = 100 * hora[0] + hora[1];
            hora = TokenizeInt(sched[1], ":");
            ab[j] = 100 * hora[0] + hora[1];
            ca[j] = 0;
            ua[j] = 0;
        }
        for (int j = 0; j < na[1]; ++j) {
            getline(cin, s);
            vs sched = Tokenize(s, " ");
            vint hora = TokenizeInt(sched[0], ":");
            db[j] = 100 * hora[0] + hora[1];
            hora = TokenizeInt(sched[1], ":");
            aa[j] = 100 * hora[0] + hora[1];
            cb[j] = 0;
            ub[j] = 0;
        }


        vint ret = trains();


		cout << "Case #" << i+1 << ": " << ret[0] << " " << ret[1] <<  endl;


	}

 	return 0;
}
