#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;

#define vi vector<int>
#define vii vector< vector<int> >
#define vs vector<string>
#define ii pair<int,int>
#define i64 long long
#define pb push_back
#define FOR(i,j,k) for(int i = (j) ; i <= (k) ; i++ )
#define FORN(i,j,k) for(int i = (j) ; i >= (k) ;i--)
#define FORI(xx,x,it) for(xx::iterator it = x.begin() ; it != x.end() ; it++)
#define FORNI(xx,x,it) for(xx::reverse_iterator it = x.rbegin() ; it != x.rend() ; it++)
#define si size()
#define all(a) (a.begin(),a.end())
#define allr(a) (a.rbegin(),a.rend())
#define MAX 100000
#define INF 2140000000
#define MOD 1000000007

int main() {
    freopen("A-large.in","r",stdin);
    freopen("jam2o.txt","w",stdout);

    int t;
    vector<string> brd(4);

    cin >> t;

    FOR(kk,1,t) {
        bool X = 0, O = 0, IN = 0;
        cin >> brd[0] >> brd[1] >> brd[2] >> brd[3];

        //Horizental
        FOR(i,0,3) {
            int x = 0, o = 0, in = 0, t = 0;
            FOR(j,0,3) {
                if(brd[i][j] == '.')
                    in++;
                else if(brd[i][j] == 'X')
                    x++;
                else if(brd[i][j] == 'O')
                    o++;
                else
                    t++;
            }

            if(in)
                IN = 1;

            if(x == 4 || (x == 3 && t == 1)) {
                X = 1;
                break;
            }
            else if(o == 4 || (o == 3 && t == 1)) {
                O = 1;
                break;
            }
        }

        //Vertical
        FOR(i,0,3) {
            int x = 0, o = 0, in = 0, t = 0;
            FOR(j,0,3) {
                if(brd[j][i] == '.')
                    in++;
                else if(brd[j][i] == 'X')
                    x++;
                else if(brd[j][i] == 'O')
                    o++;
                else
                    t++;
            }

            if(in)
                IN = 1;

            if(x == 4 || (x == 3 && t == 1)) {
                X = 1;
                break;
            }
            else if(o == 4 || (o == 3 && t == 1)) {
                O = 1;
                break;
            }
        }

        //Diagonal
        int x = 0, o = 0, in = 0, t = 0;

        FOR(i,0,3) {
                if(brd[i][i] == '.')
                    in++;
                else if(brd[i][i] == 'X')
                    x++;
                else if(brd[i][i] == 'O')
                    o++;
                else
                    t++;
        }

        if(in)
            IN = 1;

        if(x == 4 || (x == 3 && t == 1)) {
            X = 1;
        }
        else if(o == 4 || (o == 3 && t == 1)) {
                O = 1;
        }


        //2nd Diagonal
        x = 0; o = 0; in = 0; t = 0;

        FOR(i,0,3) {
                if(brd[i][3-i] == '.')
                    in++;
                else if(brd[i][3-i] == 'X')
                    x++;
                else if(brd[i][3-i] == 'O')
                    o++;
                else
                    t++;
        }

        if(in)
            IN = 1;

        if(x == 4 || (x == 3 && t == 1)) {
            X = 1;
        }
        else if(o == 4 || (o == 3 && t == 1)) {
                O = 1;
        }


        cout << "Case #" << kk << ": ";

        if(X)
            cout << "X won\n";
        else if(O)
            cout << "O won\n";
        else if(IN)
            cout << "Game has not completed\n";
        else
            cout << "Draw\n";

    }

	return 0;
}
