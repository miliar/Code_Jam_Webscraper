//============================================================================
// Name        : BitTest.cpp
// Author      : lala
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <math.h>
#include <gmpxx.h>
#include <algorithm>
#include <vector>


using namespace std;


int main() {
	long problems;
	long numberOfEvents;
	cin >> problems;
	for(long i = 0; i < problems; i++){
		cin >> numberOfEvents;
		vector<mpz_class> events;
		events.reserve(numberOfEvents);
		for(long j = 0; j < numberOfEvents; j++){
//			string str;
			mpz_class event;
			cin >> event;
/*			cin >> str;
			event = str;
*/			events.push_back(event);
		}
		sort(events.begin(),events.end());
		/* Not all the events were different... you cheaters :P :) */
		vector<mpz_class>::iterator it;
		it = unique(events.begin(),events.end());
		events.resize(it - events.begin());

		/* Assuming there are at least 2 different events */
		mpz_class diff_0 = events[1] - events[0];
		mpz_class diff_1;
		mpz_class gcd_ev;

		if(events.size() == 2)
			gcd_ev = diff_0;
		else
			for(long j = 2; j < events.size(); j++){
				diff_1 = events[j] - events[j-1];
				mpz_gcd(gcd_ev.get_mpz_t(), diff_0.get_mpz_t(),diff_1.get_mpz_t());
				diff_0 = diff_1;
			}

		mpz_class rest = events[0]%gcd_ev;
		mpz_class time = (gcd_ev - rest)%gcd_ev;
		cout << "Case #" << i+1 <<": "<< time << endl;
	}
	return 0;
}
