#include <iostream>
#include <vector>
#include <cmath>
#include <queue>
#include <string>
#include <sstream>


using namespace std;

#define NMAX 150

// tool
long sgn(long x) { return x==0?0:(x>0?1:-1); }

// simulate
struct robot {
    int pos, next;
    bool dopress, nowpress;
    string last;
    queue<int> Q;

    robot() { reset(); }
    void reset() { pos=1; next=0; dopress=nowpress=false; last=(string)"";}

    bool active() { return (pos!=next && next>0) || nowpress; }
    bool step() {
        stringstream ss;
        // anything to do?
        if(active()) {
            // right place, just need to press
            if(nowpress) {
                ss << "pressed " << pos;
                nowpress = false;
                last = ss.str();
                return true;
            }else 
            if(pos!=next && next>0) {
                // still has to move
                pos += sgn(next-pos);
                ss << "moved to " << pos;
                if(pos==next) {
                    ss << " goal";
                    next = 0;
                    if(dopress) {
                        dopress = false;
                        nowpress = true;
                        ss << ", will press";
                    }
                }
                else 
                    ss << " towards " << next;
                last = ss.str();
                return true;
            }else{
                ss<<"?";
                last = ss.str();
                return false;
            }
        }else{
            // nothing
            next = 0;
            ss << "stay at " << pos;
            last = ss.str();
            return false;
        }
    }

    bool pop() {
        if(!Q.empty()) { Q.pop(); return true; }
        else return false;
    }
    void push(long x) { Q.push(x); }

    void prepare(bool toclick=false) {
        dopress = false; nowpress = false;
        if(!Q.empty()) { 
            next = Q.front(); 
            dopress = toclick;
            if(dopress && next==pos) {
                nowpress = true;
                dopress = false;
                next = 0;
            }
        }
        else 
            next = 0;
    }

    friend ostream & operator<< (ostream &out, const robot &r) {
        /*if(r.pos==r.next || r.next==0) return out<<"("<<r.pos<<"*)";
        else return out<<"("<<r.pos<<"->"<<r.next<<")";*/
        return out<<"("<<r.last<<")";
    }

} B, O;
long tim;

void step() {
    bool moved = false;
    if(B.step()) moved = true;
    if(O.step()) moved = true;
    if(moved) ++tim;
    //cerr<<"  ["<<tim<<"] O"<<O<<", B"<<B<<endl;
}

long Solve() {
    long n; cin>>n;
    queue<int> Q;

    // in
    char c; int x;
    while(n-->0) {
        cin>>c>>x;
        (c=='B'?B:O).push(x);
        Q.push((c=='B'?-x:x));
    }

    // robot tasks
    B.reset(); O.reset(); tim=0;
    while(!Q.empty()) {
        // next task
        x = Q.front();
        Q.pop();
        //cerr<<"move "<<(x<0?'B':'O')<<" "<<(x<0?-x:x)<<endl;

        // move of B
        if(x<0) {
            B.prepare(true);
            B.pop();
            if(!O.active()) O.prepare();
            while(B.active()) step();
        }
        // or O
        else{
            O.prepare(true);
            O.pop();
            if(!B.active()) B.prepare();
            while(O.active()) step();
        }
    }

    return tim;
}

int main() {
    ios_base::sync_with_stdio(0);
    long Cases;
    cin>>Cases;
    for(int iCase=1; iCase<=Cases; ++iCase) {
        long odp;
        odp = Solve();
        cout<<"Case #"<<iCase<<": "<<odp<<endl;
    }
    return 0;
}

/*
3
4 O 2 B 1 B 2 O 4
3 O 5 O 8 B 100
2 B 2 B 1

==
Case #1: 6
Case #2: 100
Case #3: 4


*/
