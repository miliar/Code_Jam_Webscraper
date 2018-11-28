#include <iostream>
#include <fstream>
#include <set>

using namespace std;

ifstream in("in.txt");
ofstream out("out.txt");

typedef long long LL;
LL gBase[10];

int main() {
    int T;

    in >> T;
    LL a = 1;
    for( int i = 0; i<10; i++ ) gBase[i]=a, a*=10;
    for ( int tcase = 1; tcase <= T; tcase++ ) {
        LL A, B, ans = 0;
        in >> A >> B;
        for( LL num = A; num < B; num++ ) {
            set<pair<LL,LL> > seen;
            LL temp = num;
            LL curD = 1, numD = 0;
            LL base = 10;
            while(temp>0) numD++, temp/=10;

            while( base < num ) {
                LL back = num%base;
                if( back >= base/10) {
                    LL newN = back*gBase[numD-curD] + num/base;
                    pair<LL,LL> newP = make_pair(num,newN);
                    if( newN <= B && newN > num && seen.find(newP) == seen.end() ) {
                        ans++;
                        seen.insert(newP);
                    }
                }
                base *=10;
                curD++;
            }
        }
        out << "Case #" << tcase << ": " << ans << endl;
    }
    return 0;
}
