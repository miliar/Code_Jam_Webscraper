#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstring>
using namespace std;

char trans[26];
bool used[26];

string getNew(string s) {
    string ans = "";
    for (int i = 0; i < s.size(); ++i) {
        if (s[i] == ' ')
            ans += ' ';
        else if (s[i] >= 'a' && s[i] <= 'z')
            ans += trans[s[i]-'a'];
    }
    return ans;
}

void setTrans(char x, char y) {
    trans[x-'a'] = y;
    used[y-'a'] = true;
}

int main() {
    int n;
    ifstream fin;
    fin.open("input.txt");
    fin >> n;
    string content[n];
    getline(fin, content[0]);
    for (int i = 0; i < n; ++i) {
        getline(fin, content[i]);
    }
    fin.close();
    for (int i = 0; i < 26; ++i)
        trans[i] = '-';
    memset(used, 0, sizeof(used));
    setTrans('a', 'y');
    setTrans('b', 'h');
    setTrans('c', 'e');
    setTrans('d', 's');
    setTrans('e', 'o');
    setTrans('f', 'c');
    setTrans('g', 'v');
    setTrans('h', 'x');
    setTrans('i', 'd');
    setTrans('j', 'u');
    setTrans('k', 'i');
    setTrans('l', 'g');
    setTrans('m', 'l');
    setTrans('n', 'b');
    setTrans('o', 'k');
    setTrans('p', 'r');
    setTrans('q', 'z');
    setTrans('r', 't');
    setTrans('s', 'n');
    setTrans('t', 'w');
    setTrans('u', 'j');
    setTrans('v', 'p');
    setTrans('w', 'f');
    setTrans('x', 'm');
    setTrans('y', 'a');
    setTrans('z', 'q');
    string order;
    while (true) {
        for (int i = 0; i < n; ++i) {
            cout << content[i] << endl;
            cout << getNew(content[i]) << endl;
        }
        cin >> order;
        if (order == "end")
            break;
        if (order == "out") {
            ofstream out;
            out.open("output.txt");
            for (int i = 0; i < n; ++i)
                out << "Case #" << (i+1) << ": " << getNew(content[i]) << endl;
            out.close();
        }
        if (order.size() < 2)
            continue;
        if (trans[order[0]-'a'] != '-' || used[order[1]-'a'])
            cout << "wrong trans" << endl;
        else
            setTrans(order[0], order[1]);
    }
}
