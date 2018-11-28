#include <cstdio>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <utility>
#include <cstring>

using namespace std;

long long Asum[105];
long long Acount[105];
int Atype[105];
long long Bsum[105];
long long Bcount[105];
long long accum;
int Btype[105];
int Anum;
int Bnum;
long long amount;

map < pair <long long, long long>, long long > seen;

long long recurse(long long pos1, long long pos2){
    int Aindex = lower_bound(Asum, Asum+Anum, pos1) - Asum;
    int Bindex = lower_bound(Bsum, Bsum+Bnum, pos2) - Bsum;
    int typea = Atype[Aindex];
    int typeb = Btype[Bindex];
    long long best = 0;
    long long difference;

    if (pos1 == 0 || pos2 == 0){
        return 0;
    }
    
    if (seen.count(make_pair(pos1, pos2))){
        return seen[make_pair(pos1, pos2)];
    }

    if (typea == typeb){
        // current location is the same!
        difference = min(Aindex? pos1 - Asum[Aindex-1]:pos1,
                         Bindex? pos2 - Bsum[Bindex-1]:pos2);
        best = max(best, difference + recurse(pos1-difference, pos2-difference));
    } else {
        // decrement A
        if (Aindex)
            best = max(best, recurse(Asum[Aindex-1], pos2));

        // Decrement B
        if (Bindex)
            best = max(best, recurse(pos1, Bsum[Bindex-1]));
    }
    //printf ("%lld %lld -> %lld\n", pos1, pos2, best);
    seen[make_pair(pos1, pos2)] = best;
    return best;
}

int main(){
    int cases;
    scanf("%d", &cases);
    for (int j = 0; j < cases; j++){
        seen.clear();
        scanf("%d%d", &Anum, &Bnum);
        memset(Asum, 0, 105*sizeof(long long));
        memset(Bsum, 0, 105*sizeof(long long));
        accum = 0;
        for (int i = 0; i < Anum; i++){
            scanf("%lld%d", &amount, &Atype[i]);
            accum  += amount;
            Acount[i] = amount;
            Asum[i] = accum;
        }
        accum = 0;
        for (int i = 0; i < Bnum; i++){
            scanf("%lld%d", &amount, &Btype[i]);
            accum  += amount;
            Bcount[i] = amount;
            Bsum[i] = accum;
        }
        printf ("Case #%d: %lld\n", j+1, recurse(Asum[Anum-1], Bsum[Bnum-1]));
    }
    return 0;
}
