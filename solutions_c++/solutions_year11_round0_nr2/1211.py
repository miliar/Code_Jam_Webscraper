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

int main() {
    int N;
    fin >>N;
    For(test,1,N) {
        int C;
        string S;
        fin >>C;
        
        map<pair<char,char>, char> combines;
        for (int i=0; i<C; i++) {
            fin >>S;
            combines[MP(S[0], S[1])] = S[2];
            combines[MP(S[1], S[0])] = S[2];
        }
        
        int D;
        fin >>D;
        
        map<pair<char,char>, char> opposes;
        for (int i= 0; i<D; i++) {
            fin >>S;
            opposes[MP(S[0], S[1])] = 1;
            opposes[MP(S[1], S[0])] = 1;
        }
        
        int n;
        string invoke;
        fin >>n >>invoke;
        
        vector<char> result;
        int index = 0;
        while (index < Size(invoke)) {
            char el = invoke[index];
            if (Size(result) == 0) {
                result.push_back(el);
            } else {
                char el1 = result.back();
                
                pair<char,char> elPair = MP(el,el1);
                
                // combine
                if (combines.find(elPair) != combines.end()) {
                    result.pop_back();
                    result.push_back(combines[elPair]);
                } else {
                    bool cleared = false;
                    for (int i=0; i < Size(result); i++) {
                        char el1 = result[i];
                        if (opposes.find(MP(el,el1)) != opposes.end()) {
                            result.clear();
                            cleared = true;
                            break;
                        }
                    }
                    
                    if (!cleared) result.push_back(el);
                }
                /*for (int i = 0; i < Size(result); i++) {
                    if (i != 0) {
                        cout <<", ";
                    }
                    cout <<result[i];
                }
                cout <<endl;*/
            }
            index++;
        }

        fout <<"Case #" <<test <<": [";
        for (int i = 0; i < Size(result); i++) {
            if (i != 0) {
                fout <<", ";
            }
            fout <<result[i];
        }
        fout <<"]" <<endl;
    }

    exit(0);
}