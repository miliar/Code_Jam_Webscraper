/* 
 * File:   main.cpp
 * Author: sharad
 *
 * Created on 13 February, 2011, 2:47 PM
 */

#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <string>

using namespace std;

bool no_of_2s_range(int inp,int reqd) {
    if(reqd == 0) {
        return true;
    } else if(reqd == 1) {
        return (inp >= 2);
    } else {
        return (inp >= 4);
    }   
}

bool no_of_5s_range(int inp,int reqd) {
    if(reqd == 0) {
        return true;
    } else if(reqd == 1) {
        return (inp >= 5);
    } else {
        return (inp >= 25);
    }
}

int no_of_2s_exact(int inp) {
    if(inp % 4 == 0) {
        return 0;
    } else if(inp %2 ==0) {
        return 1;
    } else {
        return 2;
    }
}

int no_of_5s_exact(int inp) {
    if(inp % 25 == 0) {
        return 0;
    } else if(inp % 5 ==0) {
        return 1;
    } else {
        return 2;
    }
}

int gcd(int a) {
    int b = 100,rem = -1;
    while (true){
        rem = b%a;
        if(rem==0){
            return a;
        }
        b=a;
        a=rem;
    }
}

int gcdized(int x) {
    x = 100 / gcd(x);
    return x;
}

int main(int argc, char** argv) {
    int n_testCases = 0;
    cin >> n_testCases;

    for(int i=0; i < n_testCases; ++i) {
        string intN;
        int Pd,Pg;
        cin >> intN;
        cin >> Pd;
        cin >> Pg;
        int strLenN = intN.length();
        int N;


        bool bBroken = false;

        if(Pg == 100 && Pg > Pd) {
            bBroken = true;
        } else if(Pg == 0 && Pd > Pg) {
            bBroken = true;
        } else if(strLenN >=3) {
            
        } else if(Pd == 0) {
        }
        else {
            N = atoi(intN.c_str());
            Pd = gcdized(Pd);
            if(Pd > N) {
                bBroken = true;
            }
        }

        cout << "Case #" << (i+1) << ": "<< (bBroken ? "Broken" : "Possible") << endl;

    }

    return 0;
}

