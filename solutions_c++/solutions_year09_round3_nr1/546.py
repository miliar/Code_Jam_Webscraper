#include <iostream>
#include <fstream>
#include <map>

using namespace std;

unsigned long long int pow(unsigned long long int b, unsigned long long int p) {
    unsigned long long int a = 1;
    for (int i = 0; i < p; i++)
        a *= b;
    return a;
}

int main() {
    ifstream fin("A-large.in");
    ofstream fout("A-large.out");

    int t;
    fin >> t;
    int total = t;
    fin.get();
    while (t) {
        unsigned long long int a = 0;
        int base = 2;
        map<char, int> key;
        string temp;
        getline(fin, temp);
        int next = 1, d[64], l = temp.length();
        for (int i = 0; i < l; i++) {
            if (i == 0) {
                key[temp[i]] = next;
                next = 0;
                d[i] = key[temp[i]];
            }
            else if (key.count(temp[i]) == 0) {
                key[temp[i]] = next;
                if (!next)
                    next++;
                next++;
                d[i] = key[temp[i]];
            }
            else {
                d[i] = key[temp[i]];
            }
        }
        if (next > base)
            base = next;
        for (int i = 0; i < l; i++)
            a += (unsigned long long int) d[i] * pow(base, l - i - 1);
        fout << "Case #" << total - t + 1 << ": " << a << endl;
        t--;
    }
}
