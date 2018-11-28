#include "stdafx.h"
#include <iostream>
#include <stdio.h>
#include <fstream>
#include <string>
#include <math.h>
#include <sstream>
#include <algorithm>
#include <vector>

using namespace std;

char buff[110];
int getInt(ifstream& in) {
    in.getline(buff, 110);
    istringstream ss(buff);
    int n;
    ss >> n;
    return n;
}

string getStr(ifstream& in) {
    in.getline(buff, 110);
    return string(buff);

}

int getCount(int* arr, int* dep, int na, int nd) {
    std::sort(arr, arr + na);
    std::sort(dep, dep + nd);
    int j = 0;
    int k = 0;
    int cd = 0;
    for(;k != nd;) {
        if (j < na && arr[j] <= dep[k]) {
            j++;
            k++;
        } else {
            k++;
            cd++;
        }
    }
    return cd;
}

int main(int argc, char* argv[]) {
    string name = argv[1];
    string outName = name + ".out";
    ifstream in(name.c_str());
    ofstream out(outName.c_str());
    int n;
    in >> n;
    in.getline(buff, 110);
    for (int i = 0; i < n ; i++) {
        int na, nb, t;
        in >> t >> na >> nb;

        in.getline(buff, 110);
        int as[101];
        int ae[101];
        int bs[101];
        int be[101];
        for (int j = 0; j < na; ++j) {
            in.getline(buff, 110);
            int a,b,c,d;
            sscanf(buff, "%d:%d %d:%d", &a, &b, &c, &d);
            as[j] = a * 60 + b;
            ae[j] = c * 60 + d + t;
            cout << a << ":" << b << " " << c << ":" << d << endl;
        }

        for (int j = 0; j < nb; ++j) {
            in.getline(buff, 110);
            int a,b,c,d;
            sscanf(buff, "%d:%d %d:%d", &a, &b, &c, &d);
            bs[j] = a * 60 + b;
            be[j] = c * 60 + d + t;
            cout << a << ":" << b << " " << c << ":" << d << endl;
        }
        
        int cb = getCount(ae, bs, na, nb);
        int ca = getCount(be, as, nb, na);

        out << "Case #" << i + 1 << ": " << ca << " " << cb << endl;
    }
}

