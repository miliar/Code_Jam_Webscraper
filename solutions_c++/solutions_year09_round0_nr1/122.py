#include <cmath>
#include <string>
#include <iostream>
#include <fstream>
using namespace std;

int l;
int d;
int n;

string words[5000];

fstream in, out;

bool match(int t, string x) {
    int count = 0;
    bool paren;
    if (x.at(0) == '(') {
        paren = true;
    } else {
        paren = false;
    }
    for (int i = 0; i < l; i++) {
        if (!paren) {
            if (words[t].at(i) != x.at(count)) {
                return false;
            } else {
				if (i < l - 1) {
					count++;
					if (x.at(count) == '(') {
						paren = true;
					} else {
						paren = false;
					}
				}
            }
        } else {
            bool found = false;
            while (x.at(count) != ')') {
                if (words[t].at(i) == x.at(count)) {
                    found = true;
                }
                count++;
            }
            if (!found) {
                return false;
            } else {
				if (i < l - 1) {
					count++;
					if (x.at(count) == '(') {
						paren = true;
					} else {
						paren = false;
					}
				}
            }
        }
    }
    return true;
}

int run(string x) {
    int ret = 0;
    for (int i = 0; i < d; i++) {
        if (match(i, x)) {
            ret++;
        }
    }
    return ret;
}

int main() {
	in.open("prob1.in", fstream::in);
	out.open("prob1.out", fstream::out);

	in >> l >> d >> n;

    for (int i = 0; i < d; i++) {
        in >> words[i];
    }
    
    string temp;
    for (int ii = 0; ii < n; ii++) {
        in >> temp;
        out << "Case #" << ii + 1 << ": " << run(temp) << endl;
    }

	in.close();
	out.close();

	return 0;
}
