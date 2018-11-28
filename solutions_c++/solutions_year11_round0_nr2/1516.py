#include <iostream>
#include <vector>
#include <string>
#include <map>
using namespace std;

int T, C, D, N;
string sc;
bool op[51][51];
int cb[51][51];
char f[51];
map<char, int> mp;


void init() {
    cin >> C;
    mp.clear();
    mp['Q'] = 1, mp['W'] = 2, mp['E'] = 3, mp['R'] = 4,
    mp['A'] = 5, mp['S'] = 6, mp['D'] = 7, mp['F'] = 8;
    memset(f, 0, sizeof(f));
    f[1] = 'Q', f[2] = 'W', f[3] = 'E', f[4] = 'R',
    f[5] = 'A', f[6] = 'S', f[7] = 'D', f[8] = 'F'; 
    memset(op, false, sizeof(op));
    memset(cb, 0, sizeof(cb));
    for( int i = 0; i < C; i++ ) {
         string tmp;
         cin >> tmp;
         if( mp.find(tmp[2]) == mp.end() ) {
             int sz = mp.size();
             mp[tmp[2]] = sz+1;
             f[sz+1] = tmp[2];
         }
         cb[mp[tmp[0]]][mp[tmp[1]]] = mp[tmp[2]];
         cb[mp[tmp[1]]][mp[tmp[0]]] = mp[tmp[2]];
    }
    cin >> D;
    for( int i = 0; i < D; i++ ) {
        string tmp;
        cin >> tmp;
        op[mp[tmp[0]]][mp[tmp[1]]] = true;
        op[mp[tmp[1]]][mp[tmp[0]]] = true;
    }
    sc.clear();
    cin >> N;
    cin >> sc;
}

void solve(int tc) {
    char ret[110];
    int tail = 0;
    for( int j = 0; j < sc.size(); j++ ) {
        ret[tail++] = sc[j];
        int it = tail-2;
        while( it > -1 ) {
            int ce = cb[mp[ret[it+1]]][mp[ret[it]]];
            if( ce > 0 ) {
                tail -= 2;
                ret[tail++] = f[ce];
                it = tail-2;
            }
            else break;
        }
        for( int i = 0; i < tail-1; i++ ) {
            if( op[mp[ret[i]]][mp[ret[tail-1]]] ) {
                tail = 0;
                break;
            }
        }
    }
    printf("Case #%d: [",tc);
    for( int i = 0; i < tail; i++ ) {
        if( i > 0 ) printf(", %c", ret[i]);
        else printf("%c",ret[i]);
    }
    printf("]\n");
}

int main() {
    cin >> T;
    for( int k = 0; k < T; k++ ) {
        init();
        solve(k+1);
    }
    //system("pause");
    return 0;
}
