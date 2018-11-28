#include<iostream>
#include<fstream>
#include<cstring>
#include<cmath>
#include<ctime>
#include<string>
#include<vector>
#include<queue>
#include<deque>
#include<set>
#include<list>
#include<stack>
#include<bitset>
#include<algorithm>
#define INF (1 << 30)
#define pb push_back
#define mkp make_pair
#define pii pair<int, int>
#define ll long long
#define nxt (*it)
#define type int
#define FOR(i,a,b)\
   for(int i=a; i<=b; ++i)
#define FORR(i,a,b)\
   for(int i=a; i>=b; --i)
#define ALLR(g) \
   for(typeof(g.rbegin()) it=g.rbegin(); it!=g.rend(); ++it)
#define ALL(g)\
   for(typeof(g.begin()) it=g.begin(); it!=g.end(); ++it)
#define nMax
using namespace std;

char M[6][6];

bool emptyCell;

int T;


inline int line(int l){
    int x, o, t;
    x = o = t = 0;

    FOR(c,1,4)
        if(M[l][c] == 'T')
            t ++;
        else if(M[l][c] == 'X')
            x ++;
        else if(M[l][c] == 'O')
            o ++;
        else
            emptyCell = true;

    if(x + t == 4)
        return 1;
    if(o + t == 4)
        return 2;
    return 0;
}

inline int col(int c){
    int x, o, t;
    x = o = t = 0;

    FOR(l,1,4)
        if(M[l][c] == 'T')
            t ++;
        else if(M[l][c] == 'X')
            x ++;
        else if(M[l][c] == 'O')
            o ++;
        else
            emptyCell = true;

    if(x + t == 4)
        return 1;
    if(o + t == 4)
        return 2;
    return 0;
}

inline int diagI(){
    int x, o, t;
    x = o = t = 0;

    FOR(i,1,4)
        if(M[i][i] == 'T')
            t ++;
        else if(M[i][i] == 'X')
            x ++;
        else if(M[i][i] == 'O')
            o ++;
        else
            emptyCell = true;

    if(x + t == 4)
        return 1;
    if(o + t == 4)
        return 2;
    return 0;
}

inline int diagII(){
    int x, o, t;
    x = o = t = 0;

    FOR(i,1,4)
        if(M[i][5-i] == 'T')
            t ++;
        else if(M[i][5-i] == 'X')
            x ++;
        else if(M[i][5-i] == 'O')
            o ++;
        else
            emptyCell = true;

    if(x + t == 4)
        return 1;
    if(o + t == 4)
        return 2;
    return 0;
}

int main(){
    cin >> T;
    cin.get();

    FOR(t,1,T){
        FOR(i,1,4)
            cin.getline(M[i] + 1, 6);

        emptyCell = false;

        int res = diagI();
        if(res) goto end;

        res = diagII();
        if(res) goto end;

        FOR(i,1,4){
            res = line(i);
            if(res) break;

            res = col(i);
            if(res) break;
        }

        end:
        cout << "Case #" << t << ": ";
        switch(res){
            case 0:{
                if(emptyCell)
                    cout << "Game has not completed\n";
                else
                    cout << "Draw\n";
            } break;
            case 1: {
                cout << "X won\n";
            } break;
            case 2:{
                cout << "O won\n";
            } break;
        }

        cin.getline(M[0], 5);
    }


    return 0;
}
