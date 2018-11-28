#include <iostream>

using namespace std;

int C, D, N;
string c[100];
string d[100];
string m;
string r;
int s[128];

void print_result()
{
    cout << "[";
    bool first = true;
    for(int i = 0; i < r.size(); i++) {
        if(first) {
            first = false;
        } else {
            cout << ", ";
        }
        cout << r.at(i);
    }
    cout << "]";
}

void read_input()
{
    cin >> C;
    for(int j = 0; j < C; j++) {
        cin >> c[j];
    }
    cin >> D;
    for(int j = 0; j < D; j++) {
        cin >> d[j];
    }
    cin >> N;
    cin >> m;
}

void clear_s()
{
    for(int i = 0; i < 128; i++) {
        s[i] = 0;
    }
}

void combine()
{
    char c1 = r.at(r.size()-2);
    char c2 = r.at(r.size()-1);
    for(int i = 0; i < C; i++) {
        if((c[i][0] == c1 && c[i][1] == c2) || (c[i][1] == c1 && c[i][0] == c2)) {
            r.erase(r.size()-1);
            r.at(r.size()-1) = c[i][2];
            s[c1]--;
            s[c2]--;
            s[c[i][2]]++;
            return;
        }
    }
}

void opposed()
{
    char c1 = r.at(r.size()-1);
    for(int i = 0; i < D; i++) {
        if((d[i][0] == c1 && s[d[i][1]] > 0) || (d[i][1] == c1 && s[d[i][0]] > 0)) {
            r.clear();
            clear_s();
            return;
        }
    }
    s[c1]++;
}

void solve()
{
    r.clear();
    clear_s();
    for(int i = 0; i < m.size(); i++) {
        r += m.at(i);
        if(r.size() > 1) {
            combine();
        }
        opposed();
    }
}

int main()
{
    int T;
    cin >> T;
    for(int i = 0; i < T; i++) {
        cout << "Case #" << i+1 << ": ";
        read_input();
        solve();
        print_result();
        cout << endl;
    }
    return 0;
}
