#include <iostream>
#include <sstream>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <fstream>
#include <vector>

#define FOR(i, a, b) for(int i = (a); i < (b); ++i)
#define FR(i,a) for(int i = 0; i < (a); ++i)


// #define FILENAME "C-large"
#define FILENAME "C-small-attempt2"
// #define FILENAME "test"
static const char* c_pszInFileName = FILENAME ".in";
static const char* c_pszOutFileName = FILENAME ".out";

using namespace std;

template<class T>
void GetLine(ifstream& ifs, T& t) {
    string line;
    getline(ifs, line);
    stringstream(line) >> t;
}

int main() {
    ifstream ifs(c_pszInFileName);
    ofstream ofs(c_pszOutFileName);
    FILE* pFile = fopen(c_pszOutFileName, "w");

    int N;
    GetLine(ifs, N);
    
    multimap<char, size_t> mm;
    string find("welcome to code jam");
    // wweellccoommee to code qps jam
    // 2 2 2 2 2 2 2 
    // 64 16 8 2 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
    size_t S = find.length();

    FR(f, find.length())
        mm.insert(pair<char,size_t>(find[f], f));

    FR(t, N) {
        vector<unsigned long long> v(S, 0);
        string line;
        getline(ifs, line);
        
        for(int c = line.size() - 1; c >= 0; --c) {
            multimap<char, size_t>::iterator it;
            if ((it = mm.find(line[c])) != mm.end())
                for(; it->first == line[c]; ++it)
                    if (it->second == v.size() - 1)
                        v[it->second] = (v[it->second] + 1) % 1000;
                    else
                        v[it->second] += (v[it->second + 1] % 1000);
        }
        
        FR(s, S)
            cout << v[s] << " ";
        cout << endl;

        fprintf(pFile, "Case #%d: %04d\n", t+1, v[0]);
    }
    fclose(pFile);
    
}
