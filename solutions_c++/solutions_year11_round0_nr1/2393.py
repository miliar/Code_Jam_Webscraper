#include<cstdio>
#include<cstring>
#include<vector>
using namespace std;
int seq[105];

int main() {
    int ntc;
    scanf("%d", &ntc);
    for( int TC = 1; TC <= ntc; TC++ ) {
        int N;
        scanf("%d", &N);
        vector<int> v[3];
        v[0].clear(), v[1].clear();
        for( int i=0, t; i<N; i++ ) {
            char st[5];
            scanf("%s %d", st, &t);
            if ( strcmp( st, "B" ) == 0 ) v[0].push_back( t );
            else v[1].push_back( t );
            seq[i] = ( strcmp( st, "B" ) == 0 ) ? 0 : 1;
        }
        int B = 1, O = 1, Bidx = 0, Oidx = 0, ans = 1, idx = 0;
        
        while( idx < N ) {
            if ( seq[idx] == 0) {
                if ( B == v[0][Bidx] ) {
                    Bidx++, idx++;
                } else {
                    if ( v[0][Bidx] < B ) B--;
                    else B++;
                }
                
                if ( Oidx < v[1].size() ) {
                    if ( O != v[1][Oidx] ) {
                        if ( v[1][Oidx] < O ) O--;
                        else O++;
                    }
                }
            } else {
                if ( O == v[1][Oidx] ) {
                    Oidx++, idx++;
                } else {
                    if ( v[1][Oidx] < O ) O--;
                    else O++;
                }
                
                if ( Bidx < v[0].size() ) {
                    if ( B != v[0][Bidx] ) {
                        if ( v[0][Bidx] < B ) B--;
                        else B++;
                    }
                }
            }
            ans++;
        }
        printf("Case #%d: %d\n", TC, ans - 1);
    }
    return 0;
}
