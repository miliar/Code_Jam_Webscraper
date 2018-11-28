#include <iostream>
using namespace std;

typedef unsigned long int usint;
struct timehm{
    timehm(int& h_in, int& m_in) {
        h = h_in;
        m = m_in;
    }
    timehm(){}
    usint h;
    usint m;
};

inline timehm timeadd (timehm t1, timehm t2) {
    int hr = t1.h + t2.h;
    int min = t1.m + t2.m;
    if (min >= 60) {
        min -= 60;
        hr++;
    }
    return timehm(hr, min);
}

int main() {
    usint numcases;
    cin >> numcases;

    for (usint nc = 1; nc <= numcases; nc++) {
        int ad[1500] = {0};
        int bd[1500] = {0};
        timehm tatime;
        cin >> tatime.m;
        tatime.h=0;
        usint na, nb;
        cin >> na >> nb;
        timehm at[na];
        timehm ab[nb];
        char discardchar;
        for (int itr = 0; itr < na; itr++) {
            timehm dep, arv, arv2;
            cin >> dep.h >> discardchar >> dep.m >>
                arv2.h >> discardchar >> arv2.m;
            arv = timeadd(arv2, tatime);
            ad[dep.h*60+dep.m]--;
            bd[arv.h*60+arv.m]++;
        }
        for (int itr = 0; itr < nb; itr++) {
            timehm dep, arv, arv2;
            cin >> dep.h >> discardchar >> dep.m >>
                arv2.h >> discardchar >> arv2.m;
            arv = timeadd(arv2, tatime);
            bd[dep.h*60+dep.m]--;
            ad[arv.h*60+arv.m]++;
        }

        int amax = 0;
        int bmax = 0;
        int atot = 0;
        int btot = 0;
        for (int itr = 0; itr<1500; itr++) {
            atot += ad[itr];
            btot += bd[itr];
            if (atot < amax) amax = atot;
            if (btot < bmax) bmax = btot;
        }
        cout << "\nCase #" << nc << ": " << -amax << " " << -bmax;
    }
}
