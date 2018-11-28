#include <iostream>
#include <fstream>
#include <string>
#include <map>
std::ifstream fin("input.txt");
std::map<std::string, int> nameind;

int N, S, Q;
std::string readstr() {
    char c = fin.get();
    while (c == ' ' || c == '\n') c = fin.get();
    std::string str = "";
    while (c != '\n') {
        str += c;
        c = fin.get();
    }
    return str;
}

int main() {
    fin >> N;
    for (int i=1; i<=N; i++) {
        fin >> S;
        for (int j=0; j<S; j++) {
            nameind.insert(std::pair<std::string, int>(readstr(), j));
        }
        fin >> Q;
        bool used[100];
        int nused = 0,
            count = 0;
        memset(used, 0, 100);
        for (int j=0; j<Q; j++) {
            std::string str = readstr();
            bool *it = &used[nameind[str]];
            //std::cout << nused << ' ';
            if (*it == false) {
                if (nused == S-1) {
                    nused = 0;
                    memset(used, 0, 100);
                    count ++;
                }
                *it = true;
                nused++;
            }
            //std::cout << str << '\t' << it - used << '\t' << nused << '\n';
        }
        //std::cout << nameind.begin()->first << '\t';
        printf("Case #%i: %i\n", i, count);
        nameind.clear();
    }
}

