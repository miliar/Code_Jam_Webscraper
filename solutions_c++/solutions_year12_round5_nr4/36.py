#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <string>
#include <vector>
#include <map>
#include <set>
using namespace std;

int tot, n;
string str;

void getAllWord(set<string> &s, string str, int pos) {
    // cout << str << " " << pos << endl;
    if (pos == str.size()) {
        s.insert(str);
        return ;
    }
    if (str[pos] == 'o') {
        getAllWord(s, str, pos+1);
        str[pos] = '0';
        getAllWord(s, str, pos+1);
        return ;
    }
    if (str[pos] == 'i') {
        getAllWord(s, str, pos+1);
        str[pos] = '1';
        getAllWord(s, str, pos+1);
        return ;
    }
    if (str[pos] == 'e') {
        getAllWord(s, str, pos+1);
        str[pos] = '3';
        getAllWord(s, str, pos+1);
        return ;
    }
    if (str[pos] == 'a') {
        getAllWord(s, str, pos+1);
        str[pos] = '4';
        getAllWord(s, str, pos+1);
        return ;
    }
    if (str[pos] == 's') {
        getAllWord(s, str, pos+1);
        str[pos] = '5';
        getAllWord(s, str, pos+1);
        return ;
    }
    if (str[pos] == 't') {
        getAllWord(s, str, pos+1);
        str[pos] = '7';
        getAllWord(s, str, pos+1);
        return ;
    }
    if (str[pos] == 'b') {
        getAllWord(s, str, pos+1);
        str[pos] = '8';
        getAllWord(s, str, pos+1);
        return ;
    }
    if (str[pos] == 'g') {
        getAllWord(s, str, pos+1);
        str[pos] = '9';
        getAllWord(s, str, pos+1);
        return ;
    }
    getAllWord(s, str, pos+1);
}

int main() {
    freopen("d.in", "r", stdin);
    freopen("d.out", "w", stdout);
    cin >> tot;
    int now = 0;
    while (now < tot) {
        ++now;
        printf("Case #%d: ", now);
        cin >> n;
        cin >> str;
        set<string> all;
        for (int i = 0; i < str.size()-n+1; ++i) {
            getAllWord(all, str.substr(i, n), 0);
        }
        //for (set<string>::iterator i = all.begin(); i != all.end(); ++i)
        //    cout << *i << endl;
        if (n == 1)
            printf("%d\n", all.size());
        else {
            set<char> charset;
            map<char, int> d, o;
            for (set<string>::iterator i = all.begin(); i != all.end(); ++i) {
                char x = (*i)[0];
                char y = (*i)[1];
                if (d.count(x) != -1)
                    d[x]++;
                else
                    d[x] = 1;
                if (d.count(y) == -1)
                    d[y] = 0;
                if (o.count(y) != -1)
                    o[y] ++;
                else
                    o[y] = 1;
                if (o.count(x) == -1)
                    o[x] = 0;
            }
            int ans = all.size();
            int oc = 0, dc = 0;
            for (map<char, int>::iterator i = d.begin(); i != d.end(); ++i) {
                if (i->second > o[i->first])
                   dc += i->second - o[i->first];
                if (i->second < o[i->first])
                   oc += o[i->first] - i->second;
            }
            if (dc == 0)  ++dc;
            if (oc == 0)  ++oc;
            if (dc > oc)
               ans += dc;
            else
               ans += oc;
            printf("%d\n", ans);
        }
    }
}
