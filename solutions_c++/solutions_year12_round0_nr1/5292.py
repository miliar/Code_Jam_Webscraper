/*
 * Author: liyue
 * Created Time:  2012/4/14 14:51:01
 * File Name: a.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <fstream>
#include <cstdlib>
#include <algorithm>
#include <vector>
using namespace std;
#define out(v) cerr << #v << ": " << (v) << endl
#define SZ(v) ((int)(v).size())
const int maxint = -1u>>1;
template <class T> bool get_max(T& a, const T &b) {return b > a? a = b, 1: 0;}
template <class T> bool get_min(T& a, const T &b) {return b < a? a = b, 1: 0;}
ofstream fout("a.out");

int main() {
    char s[200] , k[26];
    int cnt = 0 , table[26] = {24,12,3,5,-2,17,5,-6,2,11,4,1,11,5,-10,6,9,-2,-15,-2,-11,-15,-3,-16,-24,-9} , t , l , i;
    cin >> t;
    cin.get();
    for(i = 0 ; i < 26 ; i++)
            k[(table[i]+'a'+i)-'a'] = char('a'+i);
    //for(i = 0 ; i < 26 ; i++)
            //cout << k[i] << ' ';
    while(t--) {
            cin.getline(s , 200);
            l = strlen(s);
            fout << "Case #" << ++cnt << ": ";
            for(i = 0 ; i < l ; i++) {
                    if(s[i] >= 'a' && s[i] <= 'z') fout << k[s[i]-'a'];
                    else fout << s[i];
            }
            fout << endl;
    }
    return 0;
}

