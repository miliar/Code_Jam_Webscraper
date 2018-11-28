/*
 * Author: liyue
 * Created Time:  2012/4/14 14:51:01
 * File Name: a.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>
#include <fstream>
#include <cstdlib>
#include <algorithm>
#include <sstream>
#include <vector>
using namespace std;
#define out(v) cerr << #v << ": " << (v) << endl
#define SZ(v) ((int)(v).size())
const int maxint = -1u>>1;
template <class T> bool get_max(T& a, const T &b) {return b > a? a = b, 1: 0;}
template <class T> bool get_min(T& a, const T &b) {return b < a? a = b, 1: 0;}
ofstream fout("a.out");
string s1 , s2;

string convertToString(double x) {
    ostringstream o;
    if(o << x)
            return o.str();
    return "conversion error";
}

bool judge() {
    int i;
    bool flag = false;
    if(s1.length() != s2.length()) return false;
    for(i = 0 ; i < s1.length(); i++) {
            s1 = s1 + s1[0];
            s1.erase(s1.begin());
            if(s1 == s2) {flag = true; break;}
    }
    if(flag == true) return true;
    else return false;
}

int main() {
    int t , a , b , cnt , i , j , k = 1;
    cin >> t;
    while(t--) {
            cnt = 0;
            cin >> a >> b;
            for(i = a ; i <= b ; i++) 
                    for(j = i+1 ; j <= b ; j++) {
                            s1 = convertToString(i);
                            s2 = convertToString(j);
                            if(judge()) cnt++;
                    }
            fout << "Case #" << k++ <<": "<<cnt << endl;
    }
    return 0;
}

