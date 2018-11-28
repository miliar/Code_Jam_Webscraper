#include <iostream>
#include <string>
#include <map>
using namespace std;

map<string, char> cbmap;
map<char, char> opmap;

string id(char a, char b) {
    string str;
    if (a > b) {
        str += b; str += a;
        return str;
    } else {
        str += a; str += b;
        return str;
    }
}

string compute(string key)
{
    int len = key.length(),reslen, pos;
    string idk, res;
    int i;
    for (i = 0; i < len; i++) {
        if (res == ""){
            res += key[i];
            continue;
        }
        reslen = res.length();
        string idk = id(res[reslen-1], key[i]);
        if (cbmap.find(idk) != cbmap.end()){
            res[reslen-1] = cbmap[idk];
            continue;
        }
        if (opmap.find(key[i]) == opmap.end()){
            res += key[i];
            continue;
        }
        char opchar = opmap[key[i]];
        if (res.find(opchar) != string::npos)
            res = "";
        else
            res += key[i];
    }
    return res;
}

int main()
{
    int T, t;
    cin >> T;
    for (t = 0; t < T; t++) {
        int C, D, N, len;
        string key;
        cin >> C;
        for (int c = 0; c < C; c++) {
            cin >> key;
            cbmap[id(key[0], key[1])] = key[2];
        }
        cin >> D;
        for (int d = 0; d < D; d++) {
            cin >> key;
            opmap[key[0]] = key[1];
            opmap[key[1]] = key[0];
        }

        cin >> N >> key;

        string res = compute(key);
        cout << "Case #" << t+1 << ": [";
        len = res.length();
        for (int i = 0; i < len-1; i++)
            cout << res[i] << ", ";
        if (len) cout << res[len-1];
        cout << "]\n";

        cbmap.clear();
        opmap.clear();
    }
}
