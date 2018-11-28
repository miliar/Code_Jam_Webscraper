#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
#include <deque>

#define REP(i, n) for ( int i = 0; i < (n); i++ ) 
#define FOR(i, a, b) for ( int i = (a); i < (b); i++ ) 

using namespace std;

const int MAX_R = 15;

int data[MAX_R][MAX_R];
int d[MAX_R][MAX_R];

const int EMPTY = 0;
const int BLOCK = 1;

const int dirX[] = {1, -1, 0, 0};
const int dirY[] = {0, 0, 1, -1};
const int GOAL = 2;

int R, C;

struct sit {
    vector< pair<int, int> > boxes;
    int cost, p;

    sit() {
        cost = 0;
        p = 0;
    }

    sit(vector< pair<int, int> > b, int c, int pp) : boxes(b), cost(c), p(pp) {
    }

    bool operator<(const sit& x) const {
//        if ( cost != x.cost ) return cost < x.cost;
        if ( boxes != x.boxes ) return boxes < x.boxes;
        return p < x.p;
    }

    bool isFree(int x, int y) {
        if ( x < 0 or y < 0 or x >= R or y >= C ) return false;
        if ( data[x][y] == BLOCK ) return false;
        for ( int i = 0; i < boxes.size(); i++ ) {
            if ( boxes[i].first == x and boxes[i].second == y ) return false;
        }
        return true;
    }

    bool doP() {
        set< pair<int, int> > got;
        for ( int i = 0; i < boxes.size(); i++ ) {
            got.insert( boxes[i] );
        }

        set< pair<int, int> > vis;
        
        deque< pair<int, int> > Q;
        Q.push_back( boxes[0] );

        while ( Q.size() > 0 ) {
            pair<int, int> A = Q.front();
            Q.pop_front();

            if ( got.find(A) == got.end() ) continue;

            vis.insert(A);
            for ( int dir = 0; dir < 4; dir++ ) {
                int nx = A.first + dirX[dir];
                int ny = A.second + dirY[dir];

                if ( nx < 0 or ny < 0 or nx >= R or ny >= C ) continue;
                if ( got.find( make_pair(nx, ny) ) != got.end() ) {
                    if ( vis.find( make_pair(nx, ny) ) == vis.end() )
                        Q.push_back(make_pair(nx, ny));
                } 
            }
        }

        if ( vis.size() == got.size() ) {
            p = 0;
            return true;
        } else {
            if ( p == 1 ) {
                return false;
            } else {
                p = 1;
                return true;
            }
        }
    }
};


bool checkCorrect(sit& A) {
    for ( int i = 0; i < A.boxes.size(); i++ ) {
        if ( data[A.boxes[i].first][A.boxes[i].second] != GOAL ) return false;
    }
    return true;
}

void fun(int cs) {
    scanf("%d %d", &R, &C);

    sit start;
    REP(i, R) REP(j, C) {
        char c;
        scanf(" %c", &c);
        if ( c == '.' ) data[i][j] = EMPTY;
        else if ( c == '#' ) data[i][j] = BLOCK;
        else if ( c == 'x' ) data[i][j] = GOAL;
        else if ( c == 'o' ) {
            data[i][j] = EMPTY;
            start.boxes.push_back( make_pair(i, j) );
        } else if ( c == 'w' ) {
            data[i][j] = GOAL;
            start.boxes.push_back( make_pair(i, j) );
        }
    }

    deque<sit> Q;
    Q.push_back(start);
    set<sit> used;
    used.insert(start);

    int tres = -1;

    while ( Q.size() > 0 ) {
        sit A = Q.front();
        Q.pop_front();

        for ( int i = 0; i < A.boxes.size(); i++ ) {
//            printf("(%d, %d) ", A.boxes[i].first, A.boxes[i].second);
        }
//        printf("\n");
//        if ( used.find(A) == used.end() ) continue;
        used.insert(A);

        if ( checkCorrect(A) ) {
            tres = A.cost;
            break;
        }

        // ruchy
        for ( int b = 0; b < A.boxes.size(); b++ ) {
            for ( int dir = 0; dir < 4; dir++ ) {
                int nx = A.boxes[b].first + dirX[dir];
                int ny = A.boxes[b].second + dirY[dir];

                int ax = A.boxes[b].first - dirX[dir];
                int ay = A.boxes[b].second - dirY[dir];

                if ( ! A.isFree(nx, ny) ) continue;
                if ( ! A.isFree(ax, ay) ) continue;

                sit B(A.boxes, A.cost+1, A.p);
                B.boxes[b] = make_pair(nx, ny);
                sort(B.boxes.begin(), B.boxes.end());


                if ( B.doP() ) {
                    if ( used.find(B) != used.end() ) continue;
                    used.insert(B);
                    Q.push_back(B);
                }
            }
        }
    }

    printf("Case #%d: %d\n", cs, tres);
    fflush(stdout);
}

int main() {
    int TT;
    scanf("%d", &TT);
    REP(i, TT) fun(i+1);

    return 0;
}
