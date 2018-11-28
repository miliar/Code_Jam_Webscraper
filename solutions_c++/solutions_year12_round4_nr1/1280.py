#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <algorithm>
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <stack>

using namespace std;

#define FOR(i, A, B) for(int i=(A); i<(B); i++)
#define REP(i, N) for(int i=0; i<(N); i++)
#define SZ(v) ((int)(v).size())
#define ALL(v) (v).begin(), (v).end()
#define SORT(v) sort(ALL(v))
#define MP make_pair
#define PB push_back
#define VI vector<int>
#define VS vector<string>
#define PII pair<int, int>
#define X first
#define Y second

int aabs(int a) { return (a<0)?-a:a; }
int mmax(int a, int b) { return (a>b)?a:b; }
int mmin(int a, int b) { return (a<b)?a:b; }

int D, N;
PII arr[10100];

int best[10100];

int main()
{
    int T;
    cin >> T;
    
    REP(caso, T) {
        
        cin >> N;
        REP(i, N) {
            cin >> arr[i].X >> arr[i].Y;
            best[i] = 0;
        }
        cin >> D;
        
        set< PII > mark;
        set< PII > added;
        queue< PII > q;
        
        q.push(MP(0, arr[0].X));
        added.insert(MP(0, arr[0].X));
        best[0] = arr[0].X;
        
        bool ok = false;
        while(!q.empty()) {
            
            PII p = q.front();
            q.pop();
            
            //cout << p.X << " //// " << p.Y << endl;
            
            if(mark.find(p) != mark.end() or best[p.X] != p.Y) continue;
            mark.insert(p);
            
            if(arr[p.X].X+p.Y >= D) {
                ok = true;
                break;
            }
            
            int i = p.X+1;
            while(i < N and arr[i].X <= arr[p.X].X + p.Y) {
                int len = mmin(arr[i].Y, arr[i].X-arr[p.X].X);
                PII pp = MP(i, len);
                if(added.find(pp) == added.end() and len > best[i]) {
                    best[i] = len;
                    q.push(pp);
                    added.insert(pp);
                }
                i++;
            }
            
            
        }
        
        
        //int pos=0, len=arr[0].X;
        //bool ok=true;
        //while(ok) {
        //    //cout << pos << " " << len << endl;
        //    if(arr[pos].X+len>=D) break;
        //    if(pos == N-1 or arr[pos].X+len < arr[pos+1].X) { ok = false; break; }
        //    
        //    int i=pos+1, best = i;
        //    while(i < N and arr[i].X <= arr[pos].X+len) {
        //        if(arr[i].X+mmin(arr[i].Y, arr[i].X-arr[pos].X) >= arr[best].X+mmin(arr[best].Y, arr[best].X-arr[pos].X)) best=i;
        //        i++;
        //    }
        //    
        //    len = mmin(arr[best].Y, arr[best].X-arr[pos].X);
        //    pos = best;
        //}
        
        cout << "Case #" << caso+1 << ": ";
        if(ok) cout << "YES\n";
        else cout << "NO\n";
    }
    
    return 0;
}