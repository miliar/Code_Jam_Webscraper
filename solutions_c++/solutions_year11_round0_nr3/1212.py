#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <ctime>
using namespace std;

typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;

#define _CRT_SECURE_NO_WARNINGS
#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define Rep(i,n) for (int i(0),_n(n); i < _n; ++i)
#define Repd(i,n) for (int i((n)-1); i >= 0; --i)
#define Fill(a,c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))
#define All(v) (v).begin(), (v).end()

template<typename T, typename S> T cast(S s) {
	stringstream ss;
	ss << s;
	T res;
	ss >> res;
	return res;
}

template<typename T> inline T sqr(T a) { return a*a; }
template<typename T> inline int Size(const T& c) { return (int)c.size(); }
template<typename T> inline void checkMin(T& a, T b) { if (b < a) a = b; }
template<typename T> inline void checkMax(T& a, T b) { if (b > a) a = b; }

ifstream fin("input.txt");
ofstream fout("output.txt");

int cmp(const int64 &a, const int64 &b) {
    if (a < b) {
        return 1;
    } else if (a > b) {
        return -1;
    }
    return 0;
}

int64 patrickSum(int64 a, int64 b) {
    int aa, bb;
    int64 pos = 1;
    int64 res = 0;
    while (a > 0 || b > 0) {
        aa = a % 2;
        bb = b % 2;
        
        a /= 2;
        b /= 2;
        
        if (aa + bb == 1) {
            res += pos;
        }
        pos *= 2;
    }
    
    return res;
}

int main() {
    int N;
    fin >>N;
    For(test,1,N) {
        int N;
        int64 C;
        int64 sum = 0;
        fin >>N;
        
        vector<int64> data;
        for (int i=0; i < N; i++) {
            fin >>C;
            data.push_back(C);
            sum += C;
        }
        
        sort(data.begin(), data.end(), cmp);
        
        vector<int> mask(N);
        mask[0] = 1;
        
        int64 seanPile = 0;
        int64 maxSeanPile = 0;
        int counter = 1;
        
        while (counter < pow(2,N)) {                    
            seanPile = 0;
            for (int i=0; i < N; i++) {
                if (mask[i] == 1) {
                    seanPile += data[i];
                }
            }
            if (sum - seanPile != 0 && seanPile > maxSeanPile) {
                int64 pile1 = 0;
                int64 pile2 = 0;
                
                for (int i=0; i < N; i++) {
                    if (mask[i] == 1) {
                        pile1 = patrickSum(pile1, data[i]);
                    } else {
                        pile2 = patrickSum(pile2, data[i]);
                    }
                }
                if (pile1 == pile2) {
                    maxSeanPile = seanPile;
                    
                    /*
                    for (int i=0; i < Size(mask); i++) {
                        cout <<mask[i];
                    };
                    cout <<" --> " <<maxSeanPile;
                    cout <<" patrick: " <<pile1 <<" vs " <<pile2;
                    cout <<endl;
                    //---*/
                }
            }
            
            if (mask[0] == 0) {
                mask[0] = 1;
            } else {
                for (int i=0; i < N; i++) {
                    if (mask[i] == 1) {
                        mask[i] = 0;
                    } else {
                        mask[i] = 1;
                        break;
                    }
                }
            }
            
            counter++;
        }
        
        fout <<"Case #" <<test <<": ";
        if (maxSeanPile != 0) {
            fout <<maxSeanPile;
        } else {
            fout <<"NO";
        }
        fout <<endl;
    }

    exit(0);
}