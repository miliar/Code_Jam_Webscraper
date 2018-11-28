#include<iostream>
#include<string>
#include<algorithm>
#include<map>
#include<memory>

using namespace std;

int f(int s, int q, int* query) {
    bool b[100] = {0};
    int n = 0, count = s;
    
    if(q == 0) return 0;
    
    count--;
    b[query[0]] = true;
    
    for(int i=1; i<q; i++) {
        if(count == 1 and b[query[i]]==false) {
            n++;
            count = s;
            memset(b, 0, sizeof(bool)*s);
        }
        if(not b[query[i]]) {
            count--;
            b[query[i]] = true;
        }
    }
    return n;
}

int main() {
    string buf;
    int query[1000];
    int N;
    cin >> N;
    for(int c=1; c<=N; c++) {
        int s, q;

        map<string, int> server;

        cin >> s;
        getline(cin, buf);
        for(int i=0; i<s; i++) {
            getline(cin, buf);
            server[buf] = i;
        }
        cin >> q;
        getline(cin, buf);
        for(int i=0; i<q; i++) {
            getline(cin, buf);
            query[i] = server[buf];
        }

        cout << "Case #" << c << ": " << f(s, q, query) << endl;
    }
}
