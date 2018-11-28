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
#include <iomanip>
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

int main() {
    freopen("output.txt", "wt", stdout);

    int N;
    fin >>N;
    For(test,1,N) {
        double result = 0;
        int N, C;
        fin >>N;
        
        vector<int> data;
        for (int i=0; i < N; i++) {
            fin >>C;
            data.push_back(C);
        }
        
        //vector<vector<int> > matrix;
        set<int> visited;
        
        int i = 0;
        while (Size(visited) != N) {
            int current = data[i];
            
            if (visited.find(current) == visited.end()) {
                if (current != i+1) {
                    int j = i;
                    vector<int> connected;
                    while (visited.find(current) == visited.end() && current != j+1) {
                        visited.insert(current);
                        connected.push_back(current);
                        
                        j = current - 1;
                        current = data[j];
                        
                        //cout <<current <<endl;
                    }
                    
                    if (Size(connected) != 0) {
                        //matrix.push_back(connected);
                        
                        result += Size(connected);
                    }
                } else {
                    visited.insert(current);
                }
            }
            i++;
        }
        
        /*for (int i=0; i < Size(matrix); i++) {
            for (int j = 0; j < Size(matrix[i]); j++) {
                cout <<matrix[i][j] <<" ";
            }
            cout <<endl;
        }*/
        
        printf("Case #%d: %.6f\n", test, result);
    }

    exit(0);
}