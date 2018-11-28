/*
Name: Jordan Moldow
ID: jormol1
LANG: C++
Program: A.cpp
Alien Language
Contest: Google Jam 2009 Qualifying Round
*/
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>

using namespace std;

class dict {
    public: 
        dict(int i = 0, int j = 0) {
            set_size(i);
            set_pos(j);
        }
        dict& operator= (const dict &d) {
            this->words = d.words;
            this->set_size(d.s);
            return *this;
        }
        void add(string word) {
            words.insert(word);
            s++;
        }
        void keep(vector<char> v) {
            set<string>::iterator IT = words.begin();
            for (set<string>::iterator it = IT; it != words.end(); it = IT) {
                IT++;
                bool out = true;
                for (int i = 0; i < v.size(); ++i) {
                    if ((*it)[pos] == v[i]) {
                        out = false;
                        break;
                    }
                }
                if (out) {
                    words.erase(*it);
                    --s;
                }
            }
            pos++;
        }
        void keep(char c) {
            set<string>::iterator IT = words.begin();
            for (set<string>::iterator it = IT; it != words.end(); it = IT) {
                IT++;
                if (!((*it)[pos] == c)) {
                    words.erase(*it);
                    --s;
                }
            }
            pos++;
        }
        void print() {
            for (set<string>::iterator it = words.begin(); it != words.end(); ++it) {
                if ((*it) != " ") {
                    cout << (*it) << "\n";
                }
            }
        }
        int size() {
            return s;
        }
        
        void set_size(int i) {
            s = i;
        }
        void set_pos(int i) {
            pos = i;
        }
        std::set<string> words;
    private:
        int s;
        int pos;
};

int main() {
    ofstream fout ("A-large.out");
    ifstream fin ("A-large.in");
    int l, d, n;
    fin >> l >> d >> n;
    const int L = l, D = d, N = n;
    vector<dict> dics;
    for (n = 0; n < N; ++n) {
        dict temp;
        dics.push_back(temp);
    }
    for (d = 0; d < D; ++d) {
        string temp;
        fin >> temp;
        for (n = 0; n < N; ++n)
            dics[n].add(temp);
    }
    for (n = 0; n < N; ++n) {
        for (l = 0; l < L; ++l) {
            char c;
            fin >> c;
            if (c != '(') {
                dics[n].keep(c);
            }
            else {
                fin >> c;
                vector<char> v;
                while(c != ')') {
                    v.push_back(c);
                    fin >> c;
                }
                dics[n].keep(v);
            }
        }
        fout << "Case #" << (n+1) << ": " << dics[n].size() << "\n";
    }
    return 0;
}

