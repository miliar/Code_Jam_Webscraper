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
        int buttonsNumber;
        fin >>buttonsNumber;
        char color;
        int pos;
        vector<char> path;
        vector<int> blue, orange;
        for (int i= 0; i<buttonsNumber; i++) {
            fin >>color >>pos;
            path.push_back(color);
            if (color == 'O') {
                orange.push_back(pos);
            } else {
                blue.push_back(pos);
            }
        }
        int result = 0;
        int orangePos = 1;
        int bluePos = 1;
        int blueIndex = 0;
        int orangeIndex = 0;
        int index = 0;
        int orangePath, bluePath;
        while (index < Size(path)) {
            if (orangeIndex < Size(orange)) {
                orangePath = orange[orangeIndex] - orangePos;
            }
            if (blueIndex < Size(blue)) {
                bluePath =  blue[blueIndex] - bluePos;
            }
            
            //cout <<path[index] <<": b:" <<blue[blueIndex] <<" o:" <<orange[orangeIndex] <<" --> ";
            
            if (path[index] == 'O') {
                if (orangePath == 0) {
                    orangeIndex++;
                    index++;
                    if (bluePath != 0) {
                        if (bluePath < 0) {
                            bluePos--;
                        } else {
                            bluePos++;
                        }
                    }
                    result++;
                } else {
                    orangePos = orange[orangeIndex];
                    orangeIndex++;
                    index++;
                    if (abs(orangePath) + 1 > abs(bluePath)) {
                        if (blueIndex < Size(blue)) {
                            bluePos = blue[blueIndex];
                        }
                    } else {
                        if (bluePath == 0) { // together
                            blueIndex++;
                            index++;
                        } else if (bluePath < 0) {
                            bluePos -= (abs(orangePath) + 1);
                        } else {
                            bluePos += (abs(orangePath) + 1);
                        }
                    }
                    result += abs(orangePath) + 1;
                }
            } else {
                if (bluePath == 0) {
                    blueIndex++;
                    index++;
                    if (orangePath != 0) {
                        if (orangePath < 0) {
                            orangePos--;
                        } else {
                            orangePos++;
                        }
                    }
                    result++;
                } else {
                    bluePos = blue[blueIndex];
                    blueIndex++;
                    index++;
                    if (abs(bluePath) + 1 > abs(orangePath)) {
                        if (orangeIndex < Size(orange)) {
                            orangePos = orange[orangeIndex];
                        }
                    } else {
                        if (orangePath == 0) { // together
                            orangeIndex++;
                            index++;
                        } else if (orangePath < 0) {
                            orangePos -= (abs(bluePath) + 1);
                        } else {
                            orangePos += (abs(bluePath) + 1);
                        }
                    }
                    result += abs(bluePath) + 1;
                }
            }
            
            //cout <<"b:" <<bluePos <<" o:" <<orangePos <<" ==> " <<result <<" ind:" <<index <<endl;
        }
        

        fout <<"Case #" <<test <<": " <<result <<endl;
    }

    exit(0);
}